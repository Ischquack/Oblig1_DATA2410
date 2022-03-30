import random
import time
import story

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
        import client
        response = client.write()
    return response

def Chuck(a, b = None):
    #time.sleep(1)
    return random.choice(story.chuck).format(a + "ing")

def Huck(a, b = None):
    #time.sleep(2)
    return random.choice(story.huck).format(a + "ing")

def Duck(a, b = None):
    #time.sleep(3)
    return random.choice(story.duck).format(a + "ing")

def Tuck(a, b = None):
    #time.sleep(4)
    return random.choice(story.tuck).format(a + "ing")