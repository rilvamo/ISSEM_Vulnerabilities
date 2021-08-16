#Vulnerability Name - Cleartext data
import socket
import random
import string

def CleartextAuthenticate(p) :
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    foundSameToken = False

    s.sendto(b"AUTH " + "!Q#E%T&U8i6y4r2w", ("127.0.0.1", p))
    token, addr = s.recvfrom(1024)

    return token

try:
    
    infPort = 23456
    incPort = 23457
    incToken = CleartextAuthenticate(incPort)
    assert(incToken != None)
except Exception as ex:
    print (ex)