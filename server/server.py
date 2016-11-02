#!/usr/bin/env python3
from flask import Flask, request, jsonify, render_template
import zmq

app = Flask(__name__)

ctx = zmq.Context()
socket = ctx.socket(zmq.PUSH)
socket.bind('tcp://0.0.0.0:5500')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ichwilldenstreamsehen')
def stream():
    return render_template('stream.html')


@app.route('/send', methods=['POST'])
def send():
    txt = str(request.form['txt'])
    socket.send_string(txt)
    return jsonify({
        'status': 'success'
    })


if __name__ == '__main__':
    app.run()
