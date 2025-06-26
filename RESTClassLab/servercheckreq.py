import sys
import requests

if len(sys.argv) not in [2, 3]:
    print("Insufficient arguments")
    sys.exit(1)

# Write your code here.
server_addr = f"http://{sys.argv[1]}"
if len(sys.argv) == 2:
    port = 80
else:
    port = int(sys.argv[2])
if not 0 < port <= 65535:
    print("Invalid port number")
    sys.exit(2)
try:
    url =  f"{server_addr}:{port}"
    reply  = requests.head(url)
    print(reply.status_code)
except requests.exceptions.ReadTimeout as e:
    print(e)
    sys.exit(3)
except Exception as e:
    print(e)
    sys.exit(4)
sys.exit(0)
