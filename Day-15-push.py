# Project:
#- Write a simple TCP client-server application using Python’s socket module.


# server.py
import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to use

def handle_client(conn, addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received from {addr}: {data.decode()}") #decode the data
        conn.sendall(data) #echo back the data
    conn.close()
    print(f"Connection with {addr} closed.")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()



    # client.py
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        while True:
            message = input("Enter message to send (or 'exit'): ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode()) #encode the message
            data = s.recv(1024)
            print('Received:', data.decode())#decode received data
    except ConnectionRefusedError:
        print("Connection to server refused. Make sure the server is running.")
    except ConnectionResetError:
        print("Connection to server was reset.")
    except Exception as e:
        print(f"An error occurred: {e}")