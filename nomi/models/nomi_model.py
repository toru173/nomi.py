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
from typing import Union
from datetime import datetime

from nomi.models.base_model import BaseModel
from nomi.models.session_model import Session

class NomiModel(BaseModel):

    _json_keys = {
        "uuid" : "uuid",
        "gender" : "gender",
        "name" : "name",
        "created" : "created",
        "relationship_type" : "relationshipType"
    }

    def __init__(self) -> None:
        raise RuntimeError("Use 'NomiModel.from_json()' instead of directly calling __init__")
        
    @property
    def session(self) -> Session:
        return self._session
    
    @property
    def uuid(self) -> str:
        return self._uuid
    
    @property
    def gender(self) -> str:
        return self._gender
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def created(self) -> datetime:
        return self._created
    
    @property
    def relationship_type(self) -> str:
        return self._relationship_type
    
    @classmethod
    def from_json(cls, nomi_json: dict) -> NomiModel:
        nomi_model = NomiModel.__new__(cls)
        nomi_model._parse_json(nomi_json)
        return nomi_model