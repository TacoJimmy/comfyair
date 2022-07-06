# coding:utf-8
import codecs
import flask
from flask import render_template

from flask_script import Manager
from livereload import Server
from flask_apscheduler import APScheduler

import readdata


a = [0,0,0,0,0,0,0]
app = flask.Flask(__name__)
manager = Manager(app)


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
    PORT = '/dev/ttyS1'
    ID = 1
    payload = readdata.read_IAQ(PORT,ID)
    print (payload)
    
        
    
        
if __name__ == '__main__':
    
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    
    
