import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 9090))

    print("UDP сервер запущен и ожидает сообщений...")
    while True:
        message, client_address = server_socket.recvfrom(1024)
        decoded_message = message.decode()
        print(f"Получено сообщение от {client_address}: {decoded_message}")

        if decoded_message == "exit":
            print("Получена команда завершения работы сервера.")
            break

        server_socket.sendto(message, client_address)

    server_socket.close()
    print("UDP сервер завершил работу.")

udp_server()
