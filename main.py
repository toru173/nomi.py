#!/usr/bin/env python3
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

    api_token = env_vars["api_token"]

    # 1 Create a Session object
    session = Session(api_token = api_token)
    
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