{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["\"\"\"import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True) ","\"\"\"",""],"id":2}]]},"ace":{"folds":[],"scrolltop":310.5,"scrollleft":0,"selection":{"start":{"row":11,"column":30},"end":{"row":11,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":18,"state":"start","mode":"ace/mode/python"}},"timestamp":1584981798209,"hash":"8e53b306cc7b60ba793ba0ddb0392a258b99e3c6"}