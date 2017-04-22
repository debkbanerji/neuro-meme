import json
import uuid
import os
import random
from os import listdir
from os.path import isfile, join

import pyrebase

image_extensions = ['jpg']

configFile = open('firebase-config.json', 'r+')
config = json.load(configFile)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

storage = firebase.storage()


# def upload_meme(path):
#     location, fileName = os.path.split(path)
#     print("Uploading " + path)
#     splitFileName = fileName.split(".")
#
#     to_push = fileName
#
#     f = open(path, 'r')
#     rawFileData = f.read()
#
#     json_data = json.loads(rawFileData)
#     json_data.pop('$id', None)
#     json_data.pop('$priority', None)
#
#     to_push = json_data
#
#     # This Version Below Does Not Overwrite Duplicates
#
#     # pushRef = db.child("memes")
#     # pushRef.push(to_push)
#
#     # The Version Below Overwrites Duplicates
#
#     pushRef = db.child("memes").child(splitFileName[0])
#     pushRef.set(to_push)

def upload_train_meme(item):
    pushRef = db.child("memes-train").child(item['key'])
    print(item)
    pushRef.set(item)
    # print(item)
    # db.child("memes-train").push(item)

def upload_classified_meme(item):
    pushRef = db.child("memes-classified").child(item['key'])
    print(item)
    pushRef.set(item)
    # print(item)
    # db.child("memes-train").push(item)

def get_train():
    return db.child("memes-train").get().val()

