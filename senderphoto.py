import sys
import socket

def sender(ws, address=""):
    offset = 0
    fragment_number = 1
    query = {}
    addr_parts = address.split(".")
    for part in addr_parts:
        total_fragments = (len(part)/ ws ) // ws
        while offset < len(part):
            # Extract a fragment of the data based on the window size
            fragment = part[offset:offset + ws]
            
            # Create a DNS query using the fragment, offset, and domain
            query_part = f"{offset}.{fragment}"
            query[fragment_number-1] = f"{query_part}.{addr_parts[1]}.{addr_parts[2]}"

            # Increment the offset
            offset += ws
            # Increment the fragment number
            fragment_number += 1
        break
        
    return query




ws = 1
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "cat.github.com"

query = sender(ws, url)
print(query)

for i in range(0, len(query)):
    resolve =socket.gethostbyname(query[i])
    print(f"{query[i]}:{resolve}")