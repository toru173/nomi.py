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
# * Neither the name of the copyright holder nor the names of the contributors
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