# =============================================================================
# ========================= nomi_api_endpoints.py =============================
# =============================================================================
# ================= Contains Information about the Nomi API ===================
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
#
# =============================================================================
# ============================ Messaging a Nomi ===============================
# =============================================================================
#
# GET Requests
# (None)
#
# POST Requests
SEND_MESSAGE = {"method" : "POST", "url" : "/v1/nomis/{nomi_id}/chat", "expected_status" : 200}
#
# PUT Requests
# (None)
#
# DELETE Requests
# (None)
#
# =============================================================================
# ============================ Nomi Information ===============================
# =============================================================================
#
# GET Requests
GET_ALL_NOMIS = {"method" : "GET", "url" : "/v1/nomis", "expected_status" : 200}
GET_NOMI_INFORMATION = {"method" : "GET", "url" : "/v1/nomis/{nomi_id}", "expected_status" : 200}
#
# POST Requests
# (None)
#
# PUT Requests
# (None)
#
# DELETE Requests
# (None)
#
# =============================================================================
# ======================= Exporting all API Endpoints =========================
# =============================================================================
#
__all__ = [name for name in dir() if not name.startswith('_')]