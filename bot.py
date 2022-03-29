import time
import client

bots = ["Chuck", "Huck", "Duck", "Tuck"]

def selectBot(nick, message):
    if nick == "Chuck":
        response = Chuck(message)
    elif nick == "Huck":
        response = Huck(message)
    elif nick == "Duck":
        response = Duck(message)
    elif nick == "Tuck":
        response = Tuck(message)
    else:
        response = client.write()
    return response

def Chuck(a, b = None):
    #time.sleep(1)
    return "This is gonna be the summer of love because I'm gonna be {} \n".format(a + "ing")

def Huck(a, b = None):
    #time.sleep(2)
    return "I'm gonna fuck Chuck's summer up, because he wants to {} \n".format(a)

def Duck(a, b = None):
    #time.sleep(3)
    return "I hate it when Huck fucks Chuck, but if Chuck tries to {} I guess it can't be helped \n".format(a)

def Tuck(a, b = None):
    #time.sleep(4)
    return "Chuck went too far this time, but I still love him \n"
