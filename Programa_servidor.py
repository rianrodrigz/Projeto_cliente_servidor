import socket
import random

HOST = 'localhost' 
PORTA = 5000 


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, PORTA))
serv.listen(1)

while True:
    print('Aguardando conexão do Cliente')
    
    Conn, Ende = serv.accept()

    print(f'Conectado em:{Ende}')

    
    Num = int(Conn.recv(1024).decode())

    
    num_casas = len(str(Num))

    if num_casas > 10:
        
        string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=num_casas))

        
        Conn.send(string.encode())
    else:
        
        if Num % 2 == 0:
            resposta = "PAR"
        else:
            resposta = "ÍMPAR"

        
        Conn.send(resposta.encode())

   
    Conn.close()