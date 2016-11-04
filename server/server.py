#!/usr/bin/env python3
from flask import Flask, request, jsonify, render_template
import zmq

app = Flask(__name__)

ctx = zmq.Context()
socket = ctx.socket(zmq.PUSH)
socket.bind('tcp://0.0.0.0:5500')

import os
import time
TIMESTAMP_WORKAROUND = 'persistent/last_instruction.workaround'
INSTRUCTION_DELAY = 2 * 15  # 30sek

def get_last_instruction():
    return int(os.stat(TIMESTAMP_WORKAROUND).st_mtime)

def set_last_instruction():
    os.utime(TIMESTAMP_WORKAROUND, None)


def now():
    return int(time.time())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/impressum')
def impressum():
    return render_template('impressum.html')


@app.route('/ichwilldenstreamsehen')
def stream():
    return render_template('stream.html')


@app.route('/send', methods=['POST'])
def send():
    if get_last_instruction() + INSTRUCTION_DELAY > now():
        return jsonify({
            'status': 'nope'
        })

    set_last_instruction()
    txt = str(request.form['txt'])
    socket.send_string(txt)
    return jsonify({
        'status': 'success'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
