# Importing libraries
import socket, sys, os

#colors
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDCOLOR = '\033[0m'

# 1st argument as server ip
if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print("\n\n Run like \n python3 client.py < serverip address > \n\n")
    exit(1)

# Client setup
dev = False
s = socket.socket()
PORT = 9898
s.connect((ServerIp, PORT))
print(f"{GREEN} Connected to {ServerIp}!\n")
print(f" waiting for server response...\n{ENDCOLOR}")

cmdprefix = "$"

while True:
    recvdata = s.recv(1024).decode()
    if recvdata == cmdprefix+"exit":
        print(f"{RED}\n Server has ended connection!\n{ENDCOLOR}")
        s.close()
        if dev == True:
            os.system("clear")
        sys.exit()
    else:
        SendData = input(f"{GREEN}{recvdata}{ENDCOLOR}{YELLOW} >> ").encode()
        print(ENDCOLOR)
        s.send(SendData)

# Close the connection from client side
s.close()
