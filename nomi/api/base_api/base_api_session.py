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
# * Neither the name of InterDigital Communications, Inc nor the names of its 
#   contributors may be used to endorse or promote products derived from this 
#   software without specific prior written permission.
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
from typing import Optional, List, Tuple, Any

import http.client
import socket

try: from nomi.api.base_api.base_api_debug import WEBHOOK_UUID
except: WEBHOOK_UUID = None

class BaseSession:
    def __init__(self, host: str, use_webhook_for_all: bool = False, use_webhook_for_POST_PUT_DELETE: bool = False) -> None:
        if not isinstance(host, str): raise TypeError("host must be a str")

        self.use_webhook_for_all = use_webhook_for_all
        self.use_webhook_for_POST_PUT_DELETE = use_webhook_for_POST_PUT_DELETE

        if self.use_webhook_for_all:
            if WEBHOOK_UUID is None: raise RuntimeError("Unable to load webhook.site UUID")
            self.host = "webhook.site"
        else:
            self.host = host

        self.http_methods = {
            "GET" : self._do_GET,
            "HEAD" : self._do_HEAD,
            "POST" : self._do_POST,
            "PUT" : self._do_PUT,
            "DELETE" : self._do_DELETE,
            "CONNECT" : self._do_CONNECT,
            "OPTIONS" : self._do_OPTIONS,
            "TRACE" : self._do_TRACE,
            "PATCH" : self._do_PATCH
        }

    def _get_default_headers(self) -> dict[str, str]:
        # Absolutely minimal headers in base class
        return {
                "Host" : self.host,
                "Accept-Encoding" : "identity"
        }

    def _do_GET(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        if not isinstance(url, str): raise TypeError("url must be a str")
        if headers is not None and not isinstance(headers, dict): raise TypeError("headers must be a dictionary or None")
        if expected_status is not None and not isinstance(expected_status, int): raise TypeError("expected_status must be a integer or None")

        if self.use_webhook_for_all:
            url = f"/{WEBHOOK_UUID}{url}"

        connection = http.client.HTTPSConnection(host = self.host)

        if headers is None:
            headers = self._get_default_headers()

        try:
            connection.request(method = "GET", url = url, headers = headers)
            response = connection.getresponse()
            status = response.status
            headers = response.getheaders()
            response_body = response.read()
                                
        except http.client.HTTPException as e: raise RuntimeError(f"An HTTP error occurred: {e}")
        except socket.timeout: raise RuntimeError("The request timed out")
        except socket.error as e: raise RuntimeError(f"A network error occurred: {e}")
        except Exception as e:raise RuntimeError(f"An unexpected error occurred: {e}")

        finally:
            connection.close()

        if expected_status is not None and status != expected_status:
                raise RuntimeWarning(f"Unexpected response status. Expected {expected_status}, got {status}")
                    
        if status == 204 or response_body == b'':
            return status, headers, None
        else:
            return status, headers, response_body
        
    def _do_HEAD(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        raise NotImplementedError("HEAD requests are not implemented")

    def _do_POST(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        if not isinstance(url, str): raise TypeError("url must be a str")
        if headers is not None and not isinstance(headers, dict): raise TypeError("headers must be a dictionary or None")
        if body is not None and not isinstance(body, str): raise TypeError("body must be a string or None")        
        if expected_status is not None and not isinstance(expected_status, int): raise TypeError("expected_status must be a integer or None")
    
        if self.use_webhook_for_POST_PUT_DELETE:
            url = f"/{WEBHOOK_UUID}{url}"
            connection = http.client.HTTPSConnection(host = "webhook.site")
        else:
            connection = http.client.HTTPSConnection(host = self.host)

        if headers is None:
            headers = self._get_default_headers()

        if body is None:
            body = ""

        try:                        
            connection.request(method = "POST", url = url, headers = headers, body = body)
            response = connection.getresponse()
            status = response.status
            headers = response.getheaders()
            response_body = response.read()
                        
        except http.client.HTTPException as e: raise RuntimeError(f"An HTTP error occurred: {e}")
        except socket.timeout: raise RuntimeError("The request timed out")
        except socket.error as e: raise RuntimeError(f"A network error occurred: {e}")
        except Exception as e:raise RuntimeError(f"An unexpected error occurred: {e}")

        finally:
            connection.close()

        if expected_status is not None and status != expected_status:
            raise RuntimeWarning(f"Unexpected response status. Expected {expected_status}, got {status}")
                    
        if status == 204 or response_body == b'':
            return status, headers, None
        else:
            return status, headers, response_body
    
    def _do_PUT(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        if not isinstance(url, str): raise TypeError("url must be a str")
        if headers is not None and not isinstance(headers, dict): raise TypeError("headers must be a dictionary or None")
        if body is not None and not isinstance(body, str): raise TypeError("body must be a string or None")
        if expected_status is not None and not isinstance(expected_status, int): raise TypeError("expected_status must be a integer or None")      

        if self.use_webhook_for_POST_PUT_DELETE:
            url = f"/{WEBHOOK_UUID}{url}"
            connection = http.client.HTTPSConnection(host = "webhook.site")
        else:
            connection = http.client.HTTPSConnection(host = self.host)

        if headers is None:
            headers = self._get_default_headers()
            headers["Content-Type"] = "application/json"

        try:            
            connection.request(method = "PUT", url = url, headers = headers, body = body)
            response = connection.getresponse()
            status = response.status
            headers = response.getheaders()
            response_body = response.read()
                                
        except http.client.HTTPException as e: raise RuntimeError(f"An HTTP error occurred: {e}")
        except socket.timeout: raise RuntimeError("The request timed out")
        except socket.error as e: raise RuntimeError(f"A network error occurred: {e}")
        except Exception as e:raise RuntimeError(f"An unexpected error occurred: {e}")

        finally:
            connection.close()

        if expected_status is not None and status != expected_status:
                raise RuntimeWarning(f"Unexpected response status. Expected {expected_status}, got {status}")

        if status == 204 or response_body == b'':
            return status, headers, None
        else:
            return status, headers, response_body

    def _do_DELETE(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        if not isinstance(url, str): raise TypeError("url must be a str")
        if headers is not None and not isinstance(headers, dict): raise TypeError("headers must be a dictionary or None")
        if expected_status is not None and not isinstance(expected_status, int): raise TypeError("expected_status must be a integer or None")

        if self.use_webhook_for_POST_PUT_DELETE:
            url = f"/{WEBHOOK_UUID}{url}"
            connection = http.client.HTTPSConnection(host = "webhook.site")
        else:
            connection = http.client.HTTPSConnection(host = self.host)

        if headers is None:
            headers = self._get_default_headers()

        try:
            connection.request(method = "DELETE", url = url, headers = headers)
            response = connection.getresponse()
            status = response.status
            headers = response.getheaders()
            response_body = response.read()
                                
        except http.client.HTTPException as e: raise RuntimeError(f"An HTTP error occurred: {e}")
        except socket.timeout: raise RuntimeError("The request timed out")
        except socket.error as e: raise RuntimeError(f"A network error occurred: {e}")
        except Exception as e:raise RuntimeError(f"An unexpected error occurred: {e}")

        finally:
            connection.close()

        if expected_status is not None and status != expected_status:
            raise RuntimeWarning(f"Unexpected response status. Expected {expected_status}, got {status}")

        if status == 204 or response_body == b'':
            return status, headers, None
        else:
            return status, headers, response_body

    def _do_CONNECT(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        NotImplementedError("CONNECT requests are not implemented")

    def _do_OPTIONS(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        raise NotImplementedError("OPTIONS requests are not implemented")

    def _do_TRACE(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        raise NotImplementedError("TRACE requests are not implemented")

    def _do_PATCH(self, url: str, headers: Optional[dict[str, str]] = None, body: Optional[str] = None, expected_status: Optional[int] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        raise NotImplementedError("PATCH requests are not implemented")

    def _do_request(self, method: str, *args, **kwargs) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        if method is None: raise TypeError("method cannot be None")
        if not isinstance(method, str): raise TypeError("method must be a str")
        
        method = method.upper()
        try:
            request = self.http_methods[method]
            return request(*args, **kwargs)
        except KeyError: raise ValueError(f"Unknown method: {method}")
        
    def do_request(self, endpoint: dict[str, any], url_parameters: Optional[dict[str, Any]] = None, payload: Optional[Any] = None) -> Tuple[int, List[Tuple[str, str]], Optional[bytes]]:
        if not isinstance(endpoint, dict): raise TypeError("endpoint must be a dictory of the form {str, any}")
        if url_parameters is not None and not isinstance(url_parameters, dict):
            raise TypeError("url_parameters must be a dictory of the form {str, any}")

        try: method = endpoint["method"]
        except KeyError: RuntimeError(f"method is required: {endpoint}")

        try: url = endpoint["url"]
        except KeyError: RuntimeError(f"url is required: {endpoint}")

        expected_status = endpoint.get("expected_status")

        if url_parameters is not None:
            url = url.format(**url_parameters)

        return self._do_request(method = method, url = url, body = payload, expected_status = expected_status)        