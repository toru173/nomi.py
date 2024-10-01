# =============================================================================
# ========================= base_nomi_requests.py =============================
# =============================================================================
# === Inherit and Extend this class to add additonal Nomi API Functionality ===
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

from nomi.api.base_api.base_api_requests import BaseSession
from nomi.api.nomi_api.nomi_api_session import NomiSession
from nomi.api.nomi_api.nomi_api_endpoints import *


class BaseNomiRequests(BaseSession):
    def __init__(self, session: NomiSession) -> None:
        if not isinstance(session, NomiSession): raise TypeError("session must be a NomiSession object")
        
        self.session = session  