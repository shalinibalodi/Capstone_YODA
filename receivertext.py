import sys
from dns_RD0 import build_message, send_udp_message, decode_message
import time
from string import ascii_lowercase as alc


def receiver(domain, ws):
    msg = ""
    offset = 0
    while True:
        for offset in range(0,10):
            for j in alc:
                query=f"{offset}.{j}.{domain}"
                print(query)
                message = build_message("A", query)
                response = send_udp_message(message, "172.29.207.107", 9090)
                dcd_msg = decode_message(response)
                print(dcd_msg)
                empty =""
                #if "ANSWER SECTION" in response:
                #    print("success")
                #    msg += j
                if response is not empty:
                    print("success")
                    msg += j
                    print(msg)
                    break
                else:
                    continue
            if len(msg) ==3:
                return msg




domain = "reddit.com"
ws = 1
msg = receiver(domain, ws)
print("Received message:", msg)