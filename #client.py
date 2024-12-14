#client
import socket
import ssl

# Визначаємо параметри
server_address = ('localhost', 65432)  # Адреса та порт сервера
server_cert = 'server_cert.pem'  # Сертифікат сервера

# Створення сокету
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Обгортаємо сокет у SSL/TLS
secure_socket = ssl.wrap_socket(client_socket,
                                keyfile=None,  # Якщо у вас є приватний ключ клієнта, вкажіть його шлях
                                certfile=None,  # Якщо у вас є сертифікат клієнта, вкажіть його шлях
                                server_side=False,
                                cert_reqs=ssl.CERT_NONE,  # Можна вказати CERT_OPTIONAL або CERT_REQUIRED для валідації сертифіката сервера
                                ssl_version=ssl.PROTOCOL_TLSv1_2)

# Підключаємося до сервера
secure_socket.connect(server_address)

# Надсилаємо повідомлення серверу
message = "Привіт, сервер! Це клієнт."
secure_socket.send(message.encode('utf-8'))

# Отримуємо відповідь від сервера
response = secure_socket.recv(1024).decode('utf-8')
print(f"Отримано від сервера: {response}")

# Закриваємо з'єднання
secure_socket.close()
