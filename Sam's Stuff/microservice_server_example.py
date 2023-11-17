import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 57318
server_socket.bind((host, port))

server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    try:
        # Receive data in chunks until the entire message is received
        received_data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                print("No chunk received. Breaking out of loop.")
                break
            received_data += chunk
            print(f"Received chunk: {len(chunk)} bytes")

        # Decode the received data
        message_in = received_data.decode('utf-8')
        print(f"Message received: {message_in}")

        # Parse the JSON data
        dict_from_json = json.loads(message_in)
        print(dict_from_json)



        # Send a response back to the client
        response_message = "Welcome to the test server!"
        client_socket.send(response_message.encode('utf-8'))
        client_socket.close()
    except Exception as e:
        print(f"Error processing message: {e}")
    finally:
        # Close the connection in the finally block to ensure it happens even if an exception occurs
        client_socket.close()
