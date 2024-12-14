#server
import socket
import ssl

# Налаштування сервера
server_cert = "server.crt"  # Ваш сертифікат сервера
server_key = "server.key"   # Ваш приватний ключ

# Створення серверного сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Сервер запущено, чекаємо з'єднання...")

# Ожидаємо клієнта
client_socket, client_address = server_socket.accept()

# Захищене SSL з'єднання
ssl_socket = ssl.wrap_socket(client_socket, keyfile=server_key, certfile=server_cert, server_side=True)

print(f"З'єднано з клієнтом: {client_address}")
data = ssl_socket.recv(1024)
print(f"Отримано дані: {data.decode()}")

ssl_socket.close()
