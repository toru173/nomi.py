# Copyright (c) 2024-present toru173 and contributors
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted (subject to the limitations in the disclaimer 
# below) provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, 
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation 
#   and/or other materials provided with the distribution.
# * Neither the name of the copyright holder nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY 
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND 
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT 
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER 
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import annotations

from nomi.models.nomi_model import NomiModel
from nomi.models.message_model import MessageModel

from nomi.requests.message_requests import MessageRequests
from nomi.requests.nomi_information_requests import NomiInformationRequests

from nomi.session import Session

class Nomi(NomiModel):

    _sent_message_key = "sentMessage"
    _reply_message_key = "replyMessage"

    @classmethod
    def from_uuid(cls, session: Session, uuid: str) -> Nomi:
        response_json = session._nomi_information_requests.get_nomi_information(uuid)
        nomi = Nomi(response_json)
        nomi._session = session
        nomi._message_requests = MessageRequests(session = nomi._session)
        nomi._nomi_information_requests = NomiInformationRequests(session = nomi._session)
        return nomi

    def send_message(self, message: str) -> dict:
        if self._session is None: raise RuntimeError("This Nomi was not created with a Session object and cannot send messages")

        response_json = self._message_requests.send_message(nomi_id = self.uuid, message = message)

        sent_message = MessageModel(response_json[self._sent_message_key])
        message_reply = MessageModel(response_json[self._reply_message_key])

        return sent_message, message_reply
        
