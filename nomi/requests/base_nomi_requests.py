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
from typing import Union, Optional, Any

from nomi.api import NomiSession
from nomi.models.http_response_model import HTTPResponseModel

class BaseNomiRequests:

    _nomi_api_errors = {
        "InvalidAPIKey" : "There is an issue with your API key",
        "NomiNotFound" : "The specified Nomi was not found. It may not exist or may not be associated with this account.",
        "InvalidRouteParams" : "The id parameter is not a valid UUID.",
        "InvalidContentType" : "The Content-Type header is not application/json.",
        "NoReply" : "The Nomi did not reply to the message. This is rare but will occur if there is a server issue or if the nomi does not respond within 15 seconds.",
        "NomiStillResponding" : "The Nomi is already replying a user message (either made through the UI or a different API call) and so cannot reply to this message.",
        "NomiNotReady" : "Immediately after the creation of a Nomi, there is a short period of several seconds before it is possible to send messages.",
        "OngoingVoiceCallDetected" : "The Nomi is currently in a voice call and cannot respond to messages.",
        "MessageLengthLimitExceeded" : "The provided messageText is too long. Maximum message length is 400 for free accounts and 600 for users with a subscription.",
        "LimitExceeded" : "Cannot send the message because the user has exhausted their daily message quota.",
        "InvalidBody" : "Issue will be detailed in the errors.issues key, but there is an issue with the request body. This can happen if the messageText key is missing, the wrong type, or an empty string.",
        "TooManyRequests" : "Use of the Nomi.ai API is subject to rate limits, but they are generous and should not affect normal use. If you hit the rate limit, you will receive a 429 Too Many Requests response.",
    }
    
    def __init__(self, session: NomiSession) -> None:
        if not isinstance(session, NomiSession):
            raise TypeError("session must be a NomiSession object")
        
        self._session = session

    def do_request(self, endpoint: dict[str, any], url_parameters: Optional[dict[str, Any]] = None, payload: Optional[Any] = None) -> Union[dict, bytes, None]:
        status, headers, body = self._session.do_request(endpoint = endpoint,
                                                         url_parameters = url_parameters,
                                                         payload = payload
                                                    )

        response = HTTPResponseModel({
            "status" : status,
            "headers" : headers,
            "body" : body,
        })

        if "error" in response.body:
            error_type = response.body.get("error").get("type")
            error_message = self._nomi_api_errors.get(error_type)
            raise RuntimeError(error_message)        

        expected_status = endpoint.get("expected_status")

        if status != expected_status:
            raise BaseNomiError(f"Unexpected response from API. Expected {expected_status}, got {status}")

        return response
    
class BaseNomiError(RuntimeError):
    # Base class for Nomi API-specific errors
    pass