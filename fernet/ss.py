# client.py

import socket
import os

def send_file(file_path, host='127.0.0.1', port=5001, buffer_size=4096):
    # Verify if the file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    # Open the file and send it in chunks
    with open(file_path, 'rb') as f:
        while True:
            # Read file data in chunks
            bytes_read = f.read(buffer_size)
            if not bytes_read:
                break    # End of file
            client_socket.sendall(bytes_read)
        print(f"File '{file_path}' sent successfully.")

    # Close the socket
    client_socket.close()
    print("Client connection closed.")

if __name__ == "__main__":
    file_to_send = "file1.txt"  # Specify the file to send
    send_file(file_to_send)
