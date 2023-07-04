import socket

def run_client():
    HOST = '127.0.0.1'
    PORT = 50000

    c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2.connect((HOST, PORT))

    print(c2.recv(1024).decode()) #Você é o jogador n aguarde

    print(c2.recv(1024).decode()) #Esperando outro jogador conectar
    c2.send("Jogador 2 Pronto".encode())

    print(c2.recv(1024).decode()) #Escolha
    o_choice = input("> ")
    c2.send(o_choice.encode()) #Envia a escolha

    print(c2.recv(1024).decode()) #Recebe o ganhador
    print('Desconectando...')
    c2.close()


if __name__ == '__main__':
    run_client()


