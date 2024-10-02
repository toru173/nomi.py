# =============================================================================
# =============================== session.py ==================================
# =============================================================================
# ======================= Represents a Session Object =========================
# =============================================================================
#
# Copyright (c) 2024-present toru173 and contributors
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted (subject to the limitations in the disclaimer 
# below) provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, 
# this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice, 
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution.
# * Neither the name of InterDigital Communications, Inc nor the names of its 
# contributors may be used to endorse or promote products derived from this 
# software without specific prior written permission.
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

from typing import Optional, List

from nomi.api.nomi_api.nomi_api_session import NomiSession
from nomi.requests.nomi_information_requests import NomiInformationRequests
from nomi.models.nomi_model import NomiModel

class Session(NomiSession):
    def __init__(self, api_token: Optional[str] = None, use_webhook_for_all: bool = False, use_webhook_for_POST_PUT_DELETE: bool = False) -> None:
        super().__init__(api_token = api_token,
                         use_webhook_for_all = use_webhook_for_all,
                         use_webhook_for_POST_PUT_DELETE = use_webhook_for_POST_PUT_DELETE)
        
        self._nomi_information_requests = NomiInformationRequests(session = self)

        self._nomis = []
        
        for nomi_json in self._nomi_information_requests.get_all_nomis():
            self._nomis.append(NomiModel.from_json(nomi_json))

    @property
    def nomis(self) -> List:
        return self._nomis