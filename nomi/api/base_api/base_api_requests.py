# =============================================================================
# ========================== base_api_requests.py =============================
# =============================================================================
# === Inherit and Extend this class to add additonal Base API Functionality ===
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

from nomi.api.base_api.base_api_session import BaseSession

class BaseRequests:
    def __init__(self, session: BaseSession) -> None:
        if not isinstance(session, BaseSession): raise TypeError("session must be a BaseSession object")
        
        self._session = session