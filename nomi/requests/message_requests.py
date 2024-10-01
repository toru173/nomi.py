# =============================================================================
# ========================== message_requests.py ==============================
# =============================================================================
# ============ Used for sending and receiving 1-1 Nomi messages ===============
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

import json

from nomi.requests.base_nomi_requests import BaseNomiRequests
from nomi.api.nomi_api.nomi_api_session import NomiSession as Session
from nomi.api.nomi_api.nomi_api_endpoints import *

class MessageRequests(BaseNomiRequests):

    _max_message_length = 600

    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def send_message(self, nomi_id: str = None, message: str = None) -> dict:
        if not isinstance(nomi_id, str):
            raise TypeError("nomi_id must be an str")

        if not isinstance(message, str):
            raise TypeError("message must be a str")
        
        if len(message) > self._max_message_length:
            raise ValueError(f"message must be less than {self._max_message_length} characters long")
        
        url_parameters = {
            "nomi_id" : nomi_id
        }

        try:
            payload = json.dumps(
                {
                    "messageText" : message,
                }
            )
        except TypeError: raise RuntimeError("Unable to encode payload to JSON")

        return self.session.do_request(endpoint = SEND_MESSAGE, url_parameters = url_parameters, payload = payload)