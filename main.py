from flask import Flask, render_template, send_file, request
from random import randrange
import hashlib
import time
from module.loads import getApis

modules = getApis()
app = Flask(__name__)
char = '%c' % randrange(1,120)
app.secret_key = hashlib.sha3_256(str(str(randrange(0,999999999))+char+'SEON06-Blog'+str(time.time())).encode('utf-8')).hexdigest()
@app.route('/')
def mainmenu():
    return render_template('mainmenu.html')

@app.route('/blog')
def blog_mainmenu():
    return render_template('blog_main.html')

@app.route('/api/<string:name>')
def api(name):
    if modules.get(name):
        return modules[name].run(request.args)
    return '?'
@app.route('/api/<string:name>/version')
def api_version(name):
    if modules.get(name):
        return f'{modules[name].getInfo()}'
    return '?'

@app.route('/file/<path:path>')
def returnFile(path):
    return send_file(f'./file/{path}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=88)