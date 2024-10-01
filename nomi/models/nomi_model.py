# =============================================================================
# ============================= nomi_model.py =================================
# =============================================================================
# ===================== The base model of a Nomi Object =======================
# =============================================================================
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>

from __future__ import annotations

from nomi.models.base_model import BaseModel
from nomi.models.session_model import Session

from typing import Dict, Union
from datetime import datetime

import json

class NomiModel(BaseModel):

    _response_json_keys = {
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
    def from_json(cls, nomi_json: Dict) -> NomiModel:
        nomi_model = NomiModel.__new__(cls)
        nomi_model._parse_json(nomi_json)

        return nomi_model
    
    def _parse_json(nomi: NomiModel, nomi_json: Union[dict, str]) -> None:
        if not isinstance(nomi, NomiModel):
            raise TypeError(f"Expected nomi to be a NomiModel, got a {type(nomi)}")
        
        if type(nomi_json) is str:
            try: nomi_json = json.loads(nomi_json)
            except json.JSONDecodeError: raise RuntimeError("Unable to decode response from JSON")

        if not type(nomi_json) is dict:
            raise TypeError(f"Expected json to be a dict, got a {type(nomi_json)}")

        for variable_name, key in nomi._response_json_keys.items():
            if key in nomi_json:
                setattr(nomi, f"_{variable_name}", nomi_json[key])
            else: raise RuntimeError(f"Unable to get {key} from JSON")