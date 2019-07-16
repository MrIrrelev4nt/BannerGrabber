import socket
import time
import sys

host = sys.argv[1]
port = sys.argv[2]

def info_check():
  try:
    host = sys.argv[1]
  except:
    print("Usage : python Banner_grabber.py host port")
    sys.exit()
  try:
    port = sys.argv[2]
  except:
    print("Usage : python Banner_grabber.py host port")
    sys.exit()
  client_socket()

def client_socket():
  s = socket.socket
  try:
    s.connect((host, port))
    print("[+] Connection To", host, "Was Successful Using Port", port)
  except:
    print("[-] Connection To", host, "Was Unsuccessful Using Port", port)
  else:
    try:
      banner = s.recv(1024).decode('utf8')
      print("[+] Banner Retrieval Was Successful On", host, "Using Port", port)
      print("[!] Banner >", banner)
    except:
      print("Banner Retrieval Was Unsuccessful On", host, "Using Port", port)
