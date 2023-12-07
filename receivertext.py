import sys
from dns_RD0 import build_message
from dns_RD0 import send_udp_message

from string import ascii_lowercase as alc


def receiver(domain, ws):
    msg = ""
    offset = 0
    while True:
        for offset in range(0,10):
            for j in alc:
                query=f"{offset}.{j}.{domain}"
                message = build_message("A", query)
                response = send_udp_message(message, "1.1.1.1", 9090)
                if "ANSWER SECTION" in response:
                    print("success")
                    msg += j




domain = "reddit.com"
ws = 1
msg = receiver(domain, ws)
print(msg)