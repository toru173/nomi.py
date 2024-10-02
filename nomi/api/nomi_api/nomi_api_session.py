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

from __future__ import annotations
from typing import Optional, Union, List, Any

import json

from nomi.api.base_api.base_api_session import BaseSession

class NomiSession(BaseSession):

    _host = "api.nomi.ai"

    def __init__(self, api_token: Optional[str] = None, use_webhook_for_all: bool = False, use_webhook_for_POST_PUT_DELETE: bool = False) -> None:
        if api_token is not None and not isinstance(api_token, str): raise TypeError("api_token must be a str")
        
        self._api_token = api_token
        
        super().__init__(host = self._host,
                         use_webhook_for_all = use_webhook_for_all,
                         use_webhook_for_POST_PUT_DELETE = use_webhook_for_POST_PUT_DELETE)

    def _get_default_headers(self) -> dict[str, str]:
        headers = super()._get_default_headers()
        if self._api_token is None: raise TypeError("api_token cannot be None")
        
        headers["Authorization"] = f"{self._api_token}"

        return headers
    
    def _do_GET(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Union[dict, bytes, None]:
        status, headers, body = super()._do_GET(url, headers, expected_status)

        # Check for JSON in the response
        content_type = dict(headers).get('Content-Type', '')
        if 'application/json' in content_type:
            try: return json.loads(body)
            except json.JSONDecodeError: raise RuntimeError("Unable to decode response from JSON")
        else:
            return body  
    
    def _do_POST(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Union[dict, List[Any], bytes, None]:
        # In most cases we're sending JSON to the API, so default to that
        if headers is None:
            headers = self._get_default_headers()
            headers["Content-Type"] = "application/json"
                    
        status, headers, body = super()._do_POST(url, headers, body, expected_status)

        # Check for JSON in the response
        content_type = dict(headers).get('Content-Type', '')
        if 'application/json' in content_type:
            try: return json.loads(body)
            except json.JSONDecodeError: raise RuntimeError("Unable to decode response from JSON")
        else:
            return body    
    
    def _do_PUT(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Union[dict, bytes, None]:
        # In most cases we're sending JSON to the API, so default to that
        if headers is None:
            headers = self._get_default_headers()
            headers["Content-Type"] = "application/json"

        status, headers, body = super()._do_PUT(url, headers, body, expected_status)

        # Check for JSON in the response
        content_type = dict(headers).get('Content-Type', '')
        if 'application/json' in content_type:
            try: return json.loads(body)
            except json.JSONDecodeError: raise RuntimeError("Unable to decode response from JSON")
        else:
            return body

    def _do_DELETE(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Union[dict, bytes, None]:
        status, headers, body = super()._do_DELETE(url, headers, expected_status)

        # Check for JSON in the response
        content_type = dict(headers).get('Content-Type', '')
        if 'application/json' in content_type:
            try: return json.loads(body)
            except json.JSONDecodeError: raise RuntimeError("Unable to decode response from JSON")
        else:
            return body
    
    def _do_file_upload(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Union[dict, bytes, None]:
        raise NotImplementedError("File upload is not implemented")

    def _do_request(self, method: str, *args, **kwargs) -> Union[dict, bytes, None]:
        return super()._do_request(method, *args, **kwargs)

    def do_request(self, endpoint: dict[str, any], url_parameters: Optional[dict[str, Any]] = None, payload: Optional[Any] = None) -> Union[dict, bytes, None]:
        return super().do_request(endpoint = endpoint, url_parameters = url_parameters, payload = payload)
    