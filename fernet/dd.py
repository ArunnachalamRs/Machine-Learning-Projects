# server.py

import socket

def start_server(host='0.0.0.0', port=5001, buffer_size=4096, save_file='received_file.txt'):
    # Create a socket and bind it to the specified host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    # Wait for a client connection
    conn, addr = server_socket.accept()
    print(f"Connection from {addr} established.")

    # Open file to write the incoming data
    with open(save_file, 'wb') as f:
        while True:
            # Read data from the client in chunks
            bytes_read = conn.recv(buffer_size)
            if not bytes_read:    
                break    # No more data, file received
            f.write(bytes_read)
        print(f"File received and saved as '{save_file}'")

    # Close the connection and the socket
    conn.close()
    server_socket.close()
    print("Server connection closed.")

if __name__ == "__main__":
    start_server()
