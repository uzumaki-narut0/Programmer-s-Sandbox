import docker
from flask import Flask, request
from flask_restful import Resource, Api
import os
import stat

client = docker.from_env()
print('in here! fellas!!')

app = Flask(__name__)
api = Api(app)

#stdout = {}


class TodoSimple(Resource):
    def get(self, code):
    	print(code)
    	with open('output.py', 'w') as f:
    		f.write('hello world')
    	#making file executable 
    	print(os.getcwd())
    	st = os.stat('output.py')
    	os.chmod('output.py', st.st_mode | stat.S_IEXEC)
    	stdout = client.containers.run("sandbox",["python","progpy.py"])
    	print(stdout)
        return {"stdout": stdout}

api.add_resource(TodoSimple, '/<string:code>')

port = int(os.environ.get("PORT", 82))
app.run(host='localhost', port=port)