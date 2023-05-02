import socket
import random

HOST = 'localhost' # Nome da maquina

PORTA = 5000 # Porta de conexao

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Familia de protocolo: IPV4 e Protocolo:TCP.

serv.bind((HOST, PORTA))#Vinculando valores que o servidor deve escutar.

serv.listen(1)#Modo de escuta.

while True:
    print('Aguardando conexão do Cliente')
    
    Conn, Ende = serv.accept() #Metodo para aceitar a conexao

    print(f'Conectado em:{Ende}')

    Num = int(Conn.recv(1024).decode()) #Tamanho dos dados que vou receber, 1024 bytes.

    num_casas = len(str(Num)) #Checa o numero recebido contem.

    if num_casas > 10: #Condicional para caso tenha mais de 10 casas ele retorna uma string do mesmo tamanho 
        
        string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=num_casas))

        Conn.send(string.encode())
    else:#Condicional para caso tenha menos de 10 casas, o programa retornara se o numero e impar ou par 
        
        if Num % 2 == 0:
            resposta = "PAR"
        else:
            resposta = "ÍMPAR"

        Conn.send(resposta.encode()) # Envia resposta para o Cliente

    Conn.close() #Fecha a conexao   
