import socket
import serial
import time


serial_port_name = '/dev/ttyACM0' 
serial_port = serial.Serial(serial_port_name, 9600)
time.sleep(2)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.1.25.118', 8080))
    server_socket.listen(5)
    print("Server waiting for connection...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print("Connection closed by the client.")
            break
        print(f"Client: {message}")
        
        serial_port.write(f"{message}\n".encode('utf-8'))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
