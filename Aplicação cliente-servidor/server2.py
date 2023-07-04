import os
import socket
import threading
import time

lock = threading.Lock()

def handle_client(c, c_num, choices):
    print(f"Jogador {c_num} conectado.")

    c.send("Esperando outro jogador conectar...".encode())
    print(c.recv(1024).decode()) #Recebe a confirmação de pronto

    time.sleep(1)
    c.send("Escolha: pedra, papel ou tesoura: ".encode())
    choice = c.recv(1024).decode() #Recebe a escolha
    print("Escolha recebida.")

    with lock:
        choices.append(choice)

print('Servidor aguardando jogadores...')

def run_server():
    HOST = '127.0.0.1'
    PORT = 50000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    c1, adr1 = s.accept()
    c1.send('Você é o jogador 1, aguarde...'.encode())

    c2, adr2 = s.accept()
    c2.send('Você é o jogador 2, aguarde...'.encode())

    choices = []

    t1 = threading.Thread(target=handle_client, args=(c1, 1, choices))
    t2 = threading.Thread(target=handle_client, args=(c2, 2, choices))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    if(len(choices) == 2):
        a = choices[0]
        b = choices[1]
        esc = f"{a};{b}"

        #fifo write
        fifo_path = "fifo_pipe"

        if not os.path.exists(fifo_path):
            os.mkfifo(fifo_path)

        fifo_fd = os.open(fifo_path, os.O_WRONLY)

        os.write(fifo_fd, esc.encode())

        os.close(fifo_fd)

        #fifo read
        fifo_path = "fifo_pipe"

        fifo_fd = os.open(fifo_path, os.O_RDONLY)  # Abre para leitura

        result = os.read(fifo_fd, 100).decode()

        os.close(fifo_fd)

        print(result)
        c1.send(result.encode())
        c2.send(result.encode())



    print('Encerrando servidor...')
    s.close()

if __name__ == '__main__':
    run_server()