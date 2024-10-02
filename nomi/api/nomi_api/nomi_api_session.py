# =============================================================================
# ============================ nomi_session.py ================================
# =============================================================================
# =============== Contains Low-Level Requests to the Nomi API =================
# =============================================================================
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for Any purpose, commercial or non-commercial, and by Any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate Any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF Any KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR Any CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>

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
    