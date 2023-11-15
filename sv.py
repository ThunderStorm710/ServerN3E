import socket

# Configurações do servidor
HOST = '0.0.0.0'  # Endereço IP do servidor
PORT = 12345       # Porta para ouvir

# Cria um socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço e à porta especificados
server_socket.bind((HOST, PORT))

# Define o limite máximo de conexões em espera
server_socket.listen(1)

print(f"Servidor ouvindo em {HOST}:{PORT}")

while True:
    # Espera por uma conexão do cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexão recebida de {client_address}")

    # Recebe a mensagem do cliente
    data = client_socket.recv(1024)
    if not data:
        break  # Se não houver dados, saia do loop

    # Processa a mensagem (neste exemplo, apenas ecoa de volta)
    response = data.decode('utf-8').upper()

    # Envia a resposta de volta para o cliente
    client_socket.sendall(response.encode('utf-8'))
    print(f"Resposta enviada: {response}")

    # Fecha a conexão com o cliente
    client_socket.close()

# Fecha o socket do servidor
server_socket.close()
