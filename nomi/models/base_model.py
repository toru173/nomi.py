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

from typing import TypeVar, Type, Union
import json

T = TypeVar('T', bound='BaseModel')

# This is similar to Python's dataclasses, but we want something a
# bit more flexible
class BaseModel:
    def __init__(self, json_dict: Union[dict, str]) -> None:
        self._parse_json(json_dict)

    @classmethod
    def from_json(cls: Type[T], json_dict: dict) -> BaseModel:       
        object = cls.__new__(cls)
        object._parse_json(json_dict)
        return object
    
    def _parse_json(self, json_dict: Union[dict, str]) -> None:
        if type(json_dict) is str:
            try:
                json_dict = json.loads(json_dict)
            except json.JSONDecodeError:
                raise RuntimeError("Unable to parse json to JSON")

        if not type(json_dict) is dict:
            raise TypeError(f"Expected json to be a dict, got a {type(json_dict)}")

        for variable_name, key in self._json_keys.items():
            if key in json_dict:
                setattr(self, f"_{variable_name}", json_dict[key])
            else:
                raise RuntimeError(f"Unable to get {key} from JSON")