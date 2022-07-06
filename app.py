# coding:utf-8
import os, io
import codecs
import flask
from flask import render_template
import time
import json
import eftmqtt
from flask_script import Manager
from livereload import Server
from flask_apscheduler import APScheduler

import threading
import readdata


a = [0,0,0,0,0,0,0]
app = flask.Flask(__name__)
manager = Manager(app)

#ipc_token = '2419-IPC000-23B672B2'


class Config(object):
    JOBS = [
        {
            'id': 'read_IAQ',
            'func': '__main__:read_IAQ',
            'args': (4, 5),
            'trigger': 'interval',
            'seconds': 5
        },


    ]

def read_IAQ(a, b):
    payload = readdata.read_IAQ('/dev/ttyS1',1)
    print (payload)
    



        
    
        
if __name__ == '__main__':
    
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    
    
