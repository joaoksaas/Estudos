import os

print("Servidor 2 operando...")

#fifo read
fifo_path = "fifo_pipe"
print("Ligando leitura de variáveis")

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

fifo_fd = os.open(fifo_path, os.O_RDONLY)

esc = os.read(fifo_fd, 100).decode()

var = esc.split(";")

print("Escolhas recebidas serv2.")

if len(var)== 2:
    p1c = var[0]
    p2c = var[1]
print("Desligando leitura de variáveis")
os.close(fifo_fd)

def play_game(p1c, p2c):
    if p1c == p2c:
        return "Empate!"
    elif(p1c.upper() == "PEDRA" and p2c.upper() == "TESOURA") or \
        (p1c.upper() == "PAPEL" and p2c.upper() == "PEDRA") or\
        (p1c.upper() == "TESOURA" and p2c.upper() == "PAPEL"):
        return "Jogador 1 venceu!"
    else:
        return "Jogador 2 venceu!"


result = play_game(p1c, p2c)

#fifo write
fifo_path = "fifo_pipe"
print("Ligando escrita de variável")
fifo_fd = os.open(fifo_path, os.O_WRONLY)

os.write(fifo_fd, result.encode())
print("Desligando escrita de variável")
os.close(fifo_fd)