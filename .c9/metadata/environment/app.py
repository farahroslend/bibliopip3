{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":76,"position":76,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":1,"column":23},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":3},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["p"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["y"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["m"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["o"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["n"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["g"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["o"],"id":4}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":[" "],"id":5},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["i"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["m"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["p"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["r"],"id":6},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":[" "],"id":7},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["P"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["Y"]}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"remove","lines":["Y"],"id":8}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["y"],"id":9},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["M"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["o"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["n"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["g"]},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":27},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":11}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["f"],"id":12},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["l"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["a"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["s"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["k"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["b"],"id":13},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["s"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["o"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["n"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["_"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["b"],"id":14},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["j"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["e"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["c"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["t"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["i"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":[" "],"id":15},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["i"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["m"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["p"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["o"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["r"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":[" "],"id":16}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["O"],"id":17},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["b"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["j"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["e"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["c"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["t"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["I"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":18}],[{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":19}],[{"start":{"row":15,"column":23},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":16,"column":0},"end":{"row":16,"column":12},"action":"insert","lines":["            "]},{"start":{"row":16,"column":12},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":12},"action":"remove","lines":["    "],"id":21},{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":12},"end":{"row":17,"column":0},"action":"remove","lines":["",""]},{"start":{"row":16,"column":8},"end":{"row":16,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":8},"action":"remove","lines":["    "],"id":22},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":94},"action":"insert","lines":["mongodb+srv://firstUser:<password>@cluster0-6873q.mongodb.net/test?retryWrites=true&w=majority"],"id":23}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":24}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":71},"action":"insert","lines":["pp.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":25}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":94},"action":"remove","lines":["mongodb+srv://firstUser:<password>@cluster0-6873q.mongodb.net/test?retryWrites=true&w=majority"],"id":26}],[{"start":{"row":7,"column":37},"end":{"row":7,"column":70},"action":"remove","lines":["MONGO_URI', 'mongodb://localhost'"],"id":27},{"start":{"row":7,"column":37},"end":{"row":7,"column":131},"action":"insert","lines":["mongodb+srv://firstUser:<password>@cluster0-6873q.mongodb.net/test?retryWrites=true&w=majority"]}],[{"start":{"row":7,"column":131},"end":{"row":7,"column":132},"action":"insert","lines":["'"],"id":28}],[{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["r"],"id":29},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["e"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["g"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["a"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["n"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["a"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["m"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["_"],"id":30},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["k"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["s"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["a"]}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"remove","lines":["t"],"id":31}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["B"],"id":32},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["i"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["b"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["l"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["i"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["o"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["a"],"id":33}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":34}],[{"start":{"row":19,"column":0},"end":{"row":40,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":35}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":[","],"id":36}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":[" "],"id":37}],[{"start":{"row":1,"column":25},"end":{"row":1,"column":69},"action":"insert","lines":[" render_template, redirect, request, url_for"],"id":38}],[{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":[" "],"id":39}],[{"start":{"row":7,"column":70},"end":{"row":7,"column":71},"action":"remove","lines":[">"],"id":40},{"start":{"row":7,"column":69},"end":{"row":7,"column":70},"action":"remove","lines":["d"]},{"start":{"row":7,"column":68},"end":{"row":7,"column":69},"action":"remove","lines":["r"]},{"start":{"row":7,"column":67},"end":{"row":7,"column":68},"action":"remove","lines":["o"]},{"start":{"row":7,"column":66},"end":{"row":7,"column":67},"action":"remove","lines":["w"]},{"start":{"row":7,"column":65},"end":{"row":7,"column":66},"action":"remove","lines":["s"]},{"start":{"row":7,"column":64},"end":{"row":7,"column":65},"action":"remove","lines":["s"]},{"start":{"row":7,"column":63},"end":{"row":7,"column":64},"action":"remove","lines":["a"]},{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"remove","lines":["p"]}],[{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"remove","lines":["<"],"id":41}],[{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"insert","lines":["f"],"id":42},{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"insert","lines":["i"]},{"start":{"row":7,"column":63},"end":{"row":7,"column":64},"action":"insert","lines":["r"]},{"start":{"row":7,"column":64},"end":{"row":7,"column":65},"action":"insert","lines":["s"]},{"start":{"row":7,"column":65},"end":{"row":7,"column":66},"action":"insert","lines":["t"]},{"start":{"row":7,"column":66},"end":{"row":7,"column":67},"action":"insert","lines":["U"]},{"start":{"row":7,"column":67},"end":{"row":7,"column":68},"action":"insert","lines":["s"]},{"start":{"row":7,"column":68},"end":{"row":7,"column":69},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":69},"end":{"row":7,"column":70},"action":"insert","lines":["r"],"id":43},{"start":{"row":7,"column":70},"end":{"row":7,"column":71},"action":"insert","lines":["P"]},{"start":{"row":7,"column":71},"end":{"row":7,"column":72},"action":"insert","lines":["a"]},{"start":{"row":7,"column":72},"end":{"row":7,"column":73},"action":"insert","lines":["s"]},{"start":{"row":7,"column":73},"end":{"row":7,"column":74},"action":"insert","lines":["s"]},{"start":{"row":7,"column":74},"end":{"row":7,"column":75},"action":"insert","lines":["w"]},{"start":{"row":7,"column":75},"end":{"row":7,"column":76},"action":"insert","lines":["o"]},{"start":{"row":7,"column":76},"end":{"row":7,"column":77},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":77},"end":{"row":7,"column":78},"action":"insert","lines":["d"],"id":44}],[{"start":{"row":7,"column":109},"end":{"row":7,"column":110},"action":"remove","lines":["t"],"id":45},{"start":{"row":7,"column":108},"end":{"row":7,"column":109},"action":"remove","lines":["s"]},{"start":{"row":7,"column":107},"end":{"row":7,"column":108},"action":"remove","lines":["e"]},{"start":{"row":7,"column":106},"end":{"row":7,"column":107},"action":"remove","lines":["t"]}],[{"start":{"row":7,"column":106},"end":{"row":7,"column":107},"action":"insert","lines":["B"],"id":46},{"start":{"row":7,"column":107},"end":{"row":7,"column":108},"action":"insert","lines":["i"]},{"start":{"row":7,"column":108},"end":{"row":7,"column":109},"action":"insert","lines":["b"]},{"start":{"row":7,"column":109},"end":{"row":7,"column":110},"action":"insert","lines":["l"]},{"start":{"row":7,"column":110},"end":{"row":7,"column":111},"action":"insert","lines":["i"]},{"start":{"row":7,"column":111},"end":{"row":7,"column":112},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":20},"action":"insert","lines":["mongo = PyMongo(app)"],"id":48}],[{"start":{"row":11,"column":0},"end":{"row":13,"column":33},"action":"remove","lines":["@app.route('/')","def hello():","    return 'Hello World ...again'"],"id":49},{"start":{"row":11,"column":0},"end":{"row":14,"column":69},"action":"insert","lines":["@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())"]}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":22},"action":"remove","lines":["tasks"],"id":50}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["r"],"id":51},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["e"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["v"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["i"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["e"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["w"]}],[{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":["w"],"id":52},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["e"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["i"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"remove","lines":["v"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"remove","lines":["e"]},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"remove","lines":["r"]}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["U"],"id":53},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["s"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["e"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["r"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["R"]}],[{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["e"],"id":54},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["v"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["e"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["i"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["e"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"remove","lines":["s"],"id":55},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"remove","lines":["e"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"remove","lines":["i"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":["e"]}],[{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["i"],"id":56},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["e"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["w"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["s"],"id":57},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":["k"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["s"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":["a"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["U"],"id":58},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["s"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["e"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["r"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["R"]}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["e"],"id":59},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["v"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["i"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["e"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["w"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":33},"action":"remove","lines":["tasks"],"id":60},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["U"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["s"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["r"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["R"]}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["e"],"id":61},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["v"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["i"]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"insert","lines":["e"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"insert","lines":["w"]},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":47},"end":{"row":14,"column":52},"action":"remove","lines":["tasks"],"id":62},{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"insert","lines":["U"]},{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"insert","lines":["s"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"insert","lines":["e"]},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"insert","lines":["r"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"insert","lines":["R"]}],[{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"insert","lines":["e"],"id":63},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"insert","lines":["v"]},{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"insert","lines":["i"]},{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"insert","lines":["e"]},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"insert","lines":["w"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":68},"end":{"row":14,"column":73},"action":"remove","lines":["tasks"],"id":64},{"start":{"row":14,"column":68},"end":{"row":14,"column":69},"action":"insert","lines":["U"]},{"start":{"row":14,"column":69},"end":{"row":14,"column":70},"action":"insert","lines":["s"]},{"start":{"row":14,"column":70},"end":{"row":14,"column":71},"action":"insert","lines":["e"]},{"start":{"row":14,"column":71},"end":{"row":14,"column":72},"action":"insert","lines":["r"]},{"start":{"row":14,"column":72},"end":{"row":14,"column":73},"action":"insert","lines":["R"]}],[{"start":{"row":14,"column":73},"end":{"row":14,"column":74},"action":"insert","lines":["e"],"id":65},{"start":{"row":14,"column":74},"end":{"row":14,"column":75},"action":"insert","lines":["v"]},{"start":{"row":14,"column":75},"end":{"row":14,"column":76},"action":"insert","lines":["i"]},{"start":{"row":14,"column":76},"end":{"row":14,"column":77},"action":"insert","lines":["e"]},{"start":{"row":14,"column":77},"end":{"row":14,"column":78},"action":"insert","lines":["w"]},{"start":{"row":14,"column":78},"end":{"row":14,"column":79},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":0},"end":{"row":43,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":67}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["_"],"id":68}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["."],"id":69}],[{"start":{"row":7,"column":26},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":71}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":71},"action":"insert","lines":["os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":72}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":116},"action":"remove","lines":["os.getenv('mongodb+srv://firstUser:firstUserPassword@cluster0-6873q.mongodb.net/Biblio?retryWrites=true&w=majority')"],"id":73}],[{"start":{"row":7,"column":71},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":74}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":65},"action":"insert","lines":["return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())"],"id":75}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":65},"action":"remove","lines":["return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())"],"id":76},{"start":{"row":14,"column":87},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":23,"column":0},"end":{"row":34,"column":40},"action":"insert","lines":["@app.route('/update_task/<task_id>', methods=[\"POST\"])","def update_task(task_id):","   tasks = mongo.db.tasks","   tasks.update( {'_id': ObjectId(task_id)},","   {","       'task_name':request.form.get['task_name'],","       'category_name':request.form.get['category_name'],","       'task_description': request.form.get['task_description'],","       'due_date': request.form.get['due_date'],","       'is_urgent':request.form.get['is_urgent']","   })","   return redirect(url_for('get_tasks'))"],"id":78}],[{"start":{"row":23,"column":0},"end":{"row":34,"column":40},"action":"remove","lines":["@app.route('/update_task/<task_id>', methods=[\"POST\"])","def update_task(task_id):","   tasks = mongo.db.tasks","   tasks.update( {'_id': ObjectId(task_id)},","   {","       'task_name':request.form.get['task_name'],","       'category_name':request.form.get['category_name'],","       'task_description': request.form.get['task_description'],","       'due_date': request.form.get['due_date'],","       'is_urgent':request.form.get['is_urgent']","   })","   return redirect(url_for('get_tasks'))"],"id":79}]]},"ace":{"folds":[],"scrolltop":40,"scrollleft":0,"selection":{"start":{"row":21,"column":0},"end":{"row":21,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":1,"state":"start","mode":"ace/mode/python"}},"timestamp":1584286968471,"hash":"134b813bf14f3db811b7f9a5cd8b07fadadcb784"}