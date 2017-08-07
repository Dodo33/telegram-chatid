#!/usr/bin/env python3

import sys

if sys.version_info < (3, 0):
    print("Python3 required.")
    exit()

import urllib.request
import json
from time import sleep

def main(argv):
    botId = argv[1]
    url = "https://api.telegram.org/bot" + botId + "/getUpdates"

    print("botId: " + botId)
    
    try:
        response = urllib.request.urlopen(url)
        print("HTTP response code: " + str(response.getcode()))
    except Exception as e:
        print("Exception " + str(e.__class__.__name__) + " " + str(e))
        exit()

    jsonData = json.loads(response.read().decode())
    if len(jsonData["result"]) == 0:
        print("I can't get the chatId if you don't send a message to the bot first. Try to send a random message and run me again.")
        exit()
    
    chatId = jsonData["result"][0]["message"]["chat"]["id"]
    print("ChatId: " + str(chatId))
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Usage: >python3 " + sys.argv[0] + " <BotId> ") 
