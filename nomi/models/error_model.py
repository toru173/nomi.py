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

from nomi.models.base_model import BaseModel

class ErrorModel(BaseModel):

    _issues_json_key = "issues"

    _response_json_keys = {
        "type" : "type",
        "issues" : _issues_json_key,
    }

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Use 'ErrorModel.from_json()' instead of directly calling __init__")
    
    @property
    def type(self) -> str:
        return self._type
    
    @property
    def issues(self) -> str:
        return self._issues
    
    @classmethod
    def from_json(cls, json: dict) -> ErrorModel:       
        message = ErrorModel.__new__(cls)
        message._parse_json(json)

        return message
    
    def _parse_json(error: ErrorModel, error_json: dict) -> None:
        if not type(error) is ErrorModel:
            raise TypeError(f"Expected error to be a ErrorModel, got a {type(error)}")
        
        if type(error_json) is str:
            try: error_json = error_json.loads(message_json)
            except error_json.JSONDecodeError: raise RuntimeError("Unable to decode response from JSON")

        if not type(error_json) is dict:
            raise TypeError(f"Expected json to be a dict, got a {type(error_json)}")

        for variable_name, key in error_json._response_json_keys.items():
            if key in error_json: setattr(error, f"_{variable_name}", error_json[key])
            else:
                if key is not error._issues_json_key:
                    raise RuntimeError(f"Unable to get {key} from JSON")
                setattr(error, f"_{error._issues_json_key}", None)