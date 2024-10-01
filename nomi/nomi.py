# =============================================================================
# ================================ nomi.py ====================================
# =============================================================================
# ========================= Represents a Nomi Object ==========================
# =============================================================================
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>

from __future__ import annotations

from typing import Dict

from nomi.models.nomi_model import NomiModel
from nomi.models.message_model import MessageModel

from nomi.requests.message_requests import MessageRequests
from nomi.requests.nomi_information_requests import NomiInformationRequests

from nomi.session import Session

import json

class Nomi(NomiModel):

    _sent_message_key = "sentMessage"
    _reply_message_key = "replyMessage"

    def __init__(self) -> None:
        raise RuntimeError("Use 'Nomi.from_uuid()' instead of directly calling __init__")

    @classmethod
    def from_uuid(cls, session: Session, uuid: str) -> Nomi:
        nomi_json = session._nomi_information_requests.get_nomi_information(uuid)
        nomi = Nomi.from_json(nomi_json)
        nomi._session = session
        nomi._message_requests = MessageRequests(session = nomi._session)
        nomi._nomi_information_requests = NomiInformationRequests(session = nomi._session)
        return nomi
    
    @classmethod
    def from_json(cls, nomi_json: Dict) -> Nomi:
        nomi = Nomi.__new__(cls)
        nomi._parse_json(nomi_json)
        return nomi

    def send_message(self, message: str) -> dict:
        if self._session is None: raise RuntimeError("This Nomi was not created with a Session object and cannot send messages")

        response_json = self._message_requests.send_message(nomi_id = self.uuid, message = message)

        sent_message = MessageModel.from_json(response_json[self._sent_message_key])
        message_reply = MessageModel.from_json(response_json[self._reply_message_key])

        return sent_message, message_reply
        
