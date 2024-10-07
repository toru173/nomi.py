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

from nomi.requests.base_nomi_requests import BaseNomiRequests
from nomi.api import NomiSession as Session
from nomi.api.nomi_api.nomi_api_endpoints import *

class NomiInformationRequests(BaseNomiRequests):

    _nomis_json_key = "nomis"

    def __init__(self, session: Session) -> None:
        super().__init__(session)
        
    def get_all_nomis(self) -> dict:
        response = self.do_request(endpoint = GET_ALL_NOMIS)
        if not self._nomis_json_key in response.body: raise RuntimeError("Unable to decode response from JSON")
        return response.body[self._nomis_json_key]
        
    def get_nomi_information(self, nomi_id: str = None) -> dict:
        if not isinstance(nomi_id, str):
            raise TypeError("nomi_id must be an str")
        
        url_parameters = {
            "nomi_id" : nomi_id
        }

        response = self.do_request(endpoint = GET_NOMI_INFORMATION, url_parameters = url_parameters)

        if "error" not in response.body.items():
            return response.body