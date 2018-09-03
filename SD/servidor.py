import socket

ip = ''
porta = 5001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0) # TCP-IP

servidor.bind((ip, porta))
servidor.listen(5)

print 'Servidor ouvindo no ip %s e na porta %s' %(ip, porta)
obj, cliente = servidor.accept()


while True:

	print 'O servidor esta conectado no cliente', cliente
	# while True:
	obj.send("Ola cliente 1!")
	msg = obj.recv(1024)
	print msg

	# 	if not msg:
	# 		break
	# 	obj.send("Ola cliente !")

servidor.close()
