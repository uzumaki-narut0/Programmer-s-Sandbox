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
    		f.write(code)
    	#making file executable 
    	st = os.stat(f)
		os.chmod(f, st.st_mode | stat.S_IEXEC)
    	stdout = client.containers.run("sandbox",["python",f])
    	print(stdout)
        return {"stdout": stdout}

api.add_resource(TodoSimple, '/<string:code>')

port = int(os.environ.get("PORT", 82))
app.run(host='localhost', port=port)