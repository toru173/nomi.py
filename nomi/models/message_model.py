# =============================================================================
# =========================== message_model.py ================================
# =============================================================================
# ========================= Represents a Nomi Object ==========================
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
from datetime import datetime

from nomi.models.base_model import BaseModel
from nomi.models.session_model import Session

class MessageModel(BaseModel):

    _response_json_keys = {
        "uuid" : "uuid",
        "text" : "text",
        "sent" : "sent",
    }

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Use 'MessageModel.from_json()' instead of directly calling __init__")
    
    @property
    def uuid(self) -> str:
        return self._uuid
    
    @property
    def text(self) -> str:
        return self._text
    
    @property
    def sent(self) -> datetime:
        return self._sent
    
    @classmethod
    def from_json(cls, json: dict) -> MessageModel:       
        message = MessageModel.__new__(cls)
        message._parse_json(json)

        return message
    
    def _parse_json(message: MessageModel, message_json: dict) -> None:
        if not type(message) is MessageModel:
            raise TypeError(f"Expected message to be a Message, got a {type(message)}")
        
        if type(message_json) is str:
            try: message_json = message_json.loads(message_json)
            except message_json.JSONDecodeError: raise RuntimeError("Unable to decode response from JSON")

        if not type(message_json) is dict:
            raise TypeError(f"Expected json to be a dict, got a {type(message_json)}")

        for variable_name, key in message._response_json_keys.items():
            if key in message_json: setattr(message, f"_{variable_name}", message_json[key])
            else:
                raise RuntimeError(f"Unable to get {key} from JSON")