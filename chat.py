#!/usr/bin/env python3
#
# Copyright (c) 2024-present toru173 and contributors Redistribution and use in source and binary forms, with or without 
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

import os
import sys
import json

from nomi import Nomi, Session

if __name__ == "__main__":

    cwd = os.path.dirname(os.path.realpath(sys.argv[0]))

    try:
        with open(f"{cwd}/.env_vars.json") as env_vars_file:
            env_vars = json.load(env_vars_file)
    except FileNotFoundError:
        raise RuntimeError("The .env file was not found.")
    except json.JSONDecodeError:
        raise RuntimeError("The .env file is not valid JSON.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

    api_key = env_vars["api_key"]

    # 1 Create a Session object
    session = Session(api_key = api_key, use_webhook_for_POST_PUT_DELETE=False)
    
    for nomi in session.nomis:
        print(f"Name: {nomi.name}")
        print(f"Gender: {nomi.gender}")
        print(f"Created: {nomi.created}")
        print(f"Relationship Type: {nomi.relationship_type}")
        print(f"UUID: {nomi.uuid}")
        print()

    nomi_uuid = input("Choose a Nomi UUID: ")
    print()
    nomi_name = None

    for nomi in session.nomis:
        if nomi.uuid == nomi_uuid:
            nomi_name = nomi.name
            break

    print(f"Now chatting with {nomi_name}. Press ctrl+c to stop")

    # 2 Create a Nomi object
    nomi = Nomi.from_uuid(session = session, uuid = nomi_uuid)

    while True:
        message = input("User: ")
        if len(message) > 600:
            print("Error: Message cannot exceed 600 characters")
            continue

        # 3 Start chatting!
        _, reply = nomi.send_message(message)
        print(f"{nomi_name}: {reply.text}")