import socket

def run_client():
    HOST = '127.0.0.1'
    PORT = 50000

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((HOST, PORT))

    print(c.recv(1024).decode())

    print(c.recv(1024).decode())
    c.send("Jogador 1 Pronto".encode())

    print(c.recv(1024).decode())
    choice = input("> ")
    c.send(choice.encode())

    print(c.recv(1024).decode())
    print('Desconectando...')
    c.close()


if __name__ == '__main__':
    run_client()


