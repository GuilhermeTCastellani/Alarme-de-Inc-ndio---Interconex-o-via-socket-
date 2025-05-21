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
    print("Servidor aguardando conexão...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão estabelecida com {client_address}")

        while True:
            data = client_socket.recv(1024).decode('utf-8').strip()

            if not data:
                break  
            if data.lower() == 'exit':
                print("Conexão encerrada pelo cliente.")
                break

            print(f"Mensagem recebida: {data}")

            if data == "1":
                serial_port.write(b"led_on\n")
                serial_port.write(b"buzzer_on\n")
            elif data == "0":
                serial_port.write(b"led_off\n")
                serial_port.write(b"buzzer_off\n")
            else:
                print("Comando inválido recebido.")

        client_socket.close()
        print("Cliente desconectado.")

if __name__ == "__main__":
    start_server()