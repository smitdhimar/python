import socket;

S=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind((socket.gethostname(),1025));
S.listen(1);
client,addr=S.accept();

msg="hello client"
client.send(msg.encode('ascii'));
client.close();
S.close()

