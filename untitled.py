#Vulnerability Name - Delete Tokens
import socket
import random
import string

def updateTemp(p, pw) :
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    foundToken = False

    while foundToken == False:
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        s.sendto(token + ";UPDATE_TEMP", ("127.0.0.1", p))
        msg, addr = s.recvfrom(1024)
        print(msg)
        if(msg != "Bad Token"):
            foundToken = True
    return token

try:
    
    infPort = 23456
    incPort = 23457
    incToken = updateTemp(incPort, b"!Q#E%T&U8i6y4r2w")

    # SampleNetworkServer has authentication so the testcase will exit at this assertion.
    assert(incToken != None)
except Exception as ex:
    print (ex)
    assert(1 == 2)