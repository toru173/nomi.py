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
#

# Maps Nomi API Errors to human-readable error messages
NOMI_API_ERRORS = {
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
}

# Maps Nomi API errors to PEP8 variable names
NOMI_API_JSON_KEYS = {
    "invalid_api_key" : "InvalidAPIKey",
    "nomi_not_found" : "NomiNotFound",
    "invalid_route_params" : "InvalidRouteParams",
    "invalid_content_type" : "InvalidContentType",
    "no_reply" : "NoReply",
    "nomi_still_responding" : "NomiStillResponding",
    "nomi_not_ready" : "NomiNotReady",
    "ongoing_voice_call_detected" : "OngoingVoiceCallDetected",
    "message_length_limit_exceeded" : "MessageLengthLimitExceeded",
    "limit_exceeded" : "LimitExceeded",
    "invalid_body" : "InvalidBody",
}