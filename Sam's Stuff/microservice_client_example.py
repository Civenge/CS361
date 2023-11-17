import socket
import time
from docx import Document

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 57318

client_socket.connect((host, port))
print(f"Connected to {host}:{port}")

json_filename = 'academics_data.json'

# open the file in text mode, read its content, encode it to UTF-8, and send in chunks
with open(json_filename, 'r', encoding='utf-8') as file:
    file_content = file.read()
    encoded_content = file_content.encode('utf-8')

    chunk_size = 1024
    for i in range(0, len(encoded_content), chunk_size):
        chunk = encoded_content[i:i+chunk_size]
        client_socket.send(chunk)
        print(f"Sending chunk {i//chunk_size + 1}/{len(encoded_content)//chunk_size + 1}")
        time.sleep(1)  # Add a small delay to allow the server to process the chunk

# stop the write side of the socket to signal the end of data
client_socket.shutdown(socket.SHUT_WR)

# receive response from the server
received_data = b""
while True:
    chunk = client_socket.recv(1024)
    if not chunk:
        break
    received_data += chunk

# create word document
doc = Document()

# save word document
doc.save('received_data.docx')

# save the received data to the file
response_filename = 'received_data.docx'
with open(response_filename, 'wb') as response_file:
    response_file.write(received_data)

print(f"Received data saved to {response_filename}")

# close the socket
client_socket.close()
