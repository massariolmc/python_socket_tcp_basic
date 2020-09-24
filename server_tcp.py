#coding: utf-8

import socket
import threading

#Definir o IP e a PORTA 
bind = ("0.0.0.0",9999)

# Cria o socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Informa para o servidor ouvir neste IP e PORTA
server.bind(bind)

#O servidor fica ouvindo até 5 conexão simultaneas
server.listen(5)

print(" Iniciar escuta: {} - {} ".format(bind[0],bind[1]))

# THREAD para tratar os clientes
def handle_client(client):

    #exibe msg do cliente
    request = client.recv(4096)
    
    while request.decode('UTF-8').strip() not in 'sair':
        print(" MSG RECEBIDA: {}".format(request.decode('UTF-8')))
        
        # envia um pacote de volta
        client.send("OK!".encode("UTF-8"))
        
        request = client.recv(4096)
    
    print("Cliente cancelou a conexao.")
    client.close()

while True:
    #Deixa o servidor na escuta aguardando conex�es
    client, addr = server.accept()

    print("Recebido de {} {} ".format(addr[0],addr[1]))

    # coloca nossa thread de cliente em acao para tratar dados de entrada
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

