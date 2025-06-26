import sys
import requests

if len(sys.argv) not in [2, 3]:
    print("Insufficient arguments")
    sys.exit(1)

# Write your code here.
server_addr = sys.argv[1]
if len(sys.argv) == 2:
    port = 80
else:
    port = int(sys.argv[2])
if not 0 < port <= 65535:
    print("Invalid port number")
    sys.exit(2)
try:
    url =  f"{server_addr}:{port/}"
    request = requests.head(url)
    re
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect((server_addr, port))
    # sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
    #           bytes(server_addr, "utf8") +
    #           b"\r\nConnection: close\r\n\r\n")
    # reply = sock.recv(10000)
    # sock.shutdown(socket.SHUT_RDWR)
    # sock.close()
    replystr = reply.decode()
    print(replystr[:replystr.index('\r')])
except socket.timeout:
    print("Connection timed out")
    sys.exit(3)
except:
    print("Unknown mode of failure")
    sys.exit(4)
sys.exit(0)
