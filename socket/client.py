import socket
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S.connect((socket.gethostname(),1025))

msg=S.recv(1025);
print(msg.decode('ascii'));
S.close();