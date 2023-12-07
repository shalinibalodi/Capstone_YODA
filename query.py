import binascii
import socket


def send_udp_message(message, address, port):
    """send_udp_message sends a message to UDP server

    message should be a hexadecimal encoded string
    """
    message = message.replace(" ", "").replace("\n", "")
    server_address = (address, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(binascii.unhexlify(message), server_address)
        data, _ = sock.recvfrom(4096)
    finally:
        sock.close()
    return binascii.hexlify(data).decode("utf-8")


def format_hex(hex):
    """format_hex returns a pretty version of a hex string"""
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return "\n".join(pairs)


message = "AA AA 01 00 00 01 00 00 00 00 00 00 " \
"06 67 6F 6F 67 6C 65 03 63 6f 6d 00 00 01 00 01"

response = send_udp_message(message, "8.8.8.8", 53)
print(format_hex(response))

#example.com "07 65 78 61 6d 70 6c 65 03 63 6f 6d 00 00 01 00 01"; Response = 5d b8 d8 22 (93.184.216.34)

#www.aditdhawan.com "03 77 77 77 10 2E 61 64 69 74 64 68 61 77 61 6E 03 63 6F 6D 00 00 01 00 01"
#google.com "06 67 6F 6F 67 6C 65 03 63 6f 6d 00 00 01 00 01"; Response = 8e fa c2 8e (142.250.194.142)
