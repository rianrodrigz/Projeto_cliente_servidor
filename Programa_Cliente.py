import socket
import random
import time

HOST = 'localhost' #Nome da maquina.

PORTA = 5000 #Porta de conexao. 

while True:
    
    Conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Familia de protocolo: IPV4 e Protocolo:TCP.
    
    Conn.connect((HOST, PORTA))#Pedindo conexao ao servidor.

    Num = random.randint(1, 10**30)#Criacao aleatoria de um numero de ate 30 casas.
    
    #Num = random.randint(1, 11)#Para testar a condicional caso o numero tenha menos de 10 casas.

    Conn.send(str(Num).encode())#Encode e utilizado para garantir que vai enviar a mensagem devidamente.

    resposta = Conn.recv(1024).decode()#Decode e utlizado para receber a mesagem devidamente. 

    print(resposta)#Mostra a resposta.

    Conn.close()#Fecha a conexao.

    time.sleep(10)#Utilizando a biblioteca time para esperar os 10 segundos ate a proxima conexao.
