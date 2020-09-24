# coding: utf-8

import socket

target = ("XXX.XXX.XXX.XXX", 9999)

# cria um objeto socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# faz o cliente se conectar
client.connect(target)

print("Digite para enviar dados: ")
words = 'Inicio'

while words.strip() not in 'sair':
    #envia alguns dados
    print(type(words))
    words = input(">>>")
    print(type(words))
    # O padrao do metodo send e eviar dados do tipo byte, porem e enviado uma string
    # Para codificar isso, codificamos em utf-8 e enviamos
    client.send(words.encode('UTF-8'))
    print(type(words))
    # recebe alguns dados. O metodo recv é blocante, quer dizer que todo o código
    # ficará parado até receber dado
    #Como codificamos em utf-8, aqui temos que descodificar
    response = client.recv(4096).decode('UTF-8')

    print("Valor do response: {}".format(response))
