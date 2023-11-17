import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 57318

client_socket.connect((host, port))
print(f"Connected to {host}:{port}")

json_filename = 'academics_data.json'

# Open the file in text mode, read its content, encode it to UTF-8, and send in chunks
with open(json_filename, 'r', encoding='utf-8') as file:
    file_content = file.read()
    encoded_content = file_content.encode('utf-8')

    chunk_size = 1024
    for i in range(0, len(encoded_content), chunk_size):
        chunk = encoded_content[i:i+chunk_size]
        client_socket.send(chunk)
        print(f"Sending chunk {i//chunk_size + 1}/{len(encoded_content)//chunk_size}")
        time.sleep(1)  # Add a small delay to allow the server to process the chunk

# Shutdown the write side of the socket to signal the end of data
client_socket.shutdown(socket.SHUT_WR)

# Receive the response from the server
message = client_socket.recv(1024).decode('utf-8')
print(f"Server says: {message}")

# Close the socket
client_socket.close()
