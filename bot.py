
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
        response = ""
    return response

def Chuck(a, b = None):
    return "This is gonna be the summer of love because I'm gonna be {}".format(a + "ing")

def Huck(a, b = None):
    return "I'm gonna fuck Chuck's summer up, because he wants to {}".format(a)

def Duck(a, b = None):
    return "I hate it when Huck fucks Chuck, but if Chuck tries to {} I guess it can't be helped".format(a)

def Tuck(a, b = None):
    return "Chuck went too far this time, but I still love him"
