import socket
import logging
import threading


def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            logging.info(data)
            if data == b'shutdown':
                flag = False
                break

            if not data:
                break
            client_socket.sendall(data)
    finally:
        client_socket.close()
        logging.info('Close client connection')
    if not flag:
        logging.info("Server stopped")
        assert KeyboardInterrupt
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9090))
    server_socket.listen()
    logging.basicConfig(
                        level=logging.INFO,
                        filename='server_th.log',
                        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                        datefmt='%Y-%m-%d %H:%M:%S'
    )
    flag = True
    while True:
        try:
            logging.info("Сервер запущен и ожидает подключений...")
            client_socket, client_address = server_socket.accept()
            logging.info(f'Accept connection, client adress: {client_address}')
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
        except KeyboardInterrupt:
            logging.info('Close server connection')
            break
    server_socket.close()

start_server()