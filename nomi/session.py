# =============================================================================
# =============================== session.py ==================================
# =============================================================================
# ======================= Represents a Session Object =========================
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

from nomi.api.nomi_api.nomi_api_session import NomiSession
from nomi.requests.nomi_information_requests import NomiInformationRequests
from nomi.models.nomi_model import NomiModel

from typing import Optional, List

class Session(NomiSession):
    def __init__(self, api_token: Optional[str] = None, use_webhook_for_all: bool = False, use_webhook_for_POST_PUT_DELETE: bool = False) -> None:
        super().__init__(api_token = api_token,
                         use_webhook_for_all = use_webhook_for_all,
                         use_webhook_for_POST_PUT_DELETE = use_webhook_for_POST_PUT_DELETE)
        
        self._nomi_information_requests = NomiInformationRequests(session = self)

        self._nomis = []
        
        for nomi_json in self._nomi_information_requests.get_all_nomis():
            self._nomis.append(NomiModel.from_json(nomi_json))

    @property
    def nomis(self) -> List:
        return self._nomis