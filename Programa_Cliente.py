import socket
import random
import time

HOST = 'localhost' 
PORTA = 5000 

while True:
    
    Conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Conn.connect((HOST, PORTA))

    
    Num = random.randint(1, 10**30)

    
    Conn.send(str(Num).encode())

    
    resposta = Conn.recv(1024).decode()

    
    print(resposta)

    
    Conn.close()

    
    time.sleep(10)