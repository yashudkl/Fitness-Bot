import json
def getPath():
    """
    Gets path of the from ./metadata.json/  
    """
    with open('bot_config.json', 'r') as openfile:
        global path
        json_object = json.load(openfile)
        pairs = json_object.items()
        path = json_object["token"]
    return path

print(getPath())