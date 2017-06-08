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
    	with open('progpy.py', 'w') as f:
    		f.write('hello new world')
    	#making file executable 
    	client.images.build(path='.',tag='sandbox')
    	print(os.getcwd())
    	st = os.stat('output.py')
    	os.chmod('output.py', st.st_mode | stat.S_IEXEC)
    	stdout = client.containers.run("sandbox",["python","progpy.py"])
    	print(stdout)
        return {"stdout": stdout}

    def post(self):
    	parser = reqparse.RequestParser()
        parser.add_argument('langid');
        parser.add_argument('code')
        #parser.add_argument('lng')
        args = parser.parse_args()
        language = args['langid']
        code = args['code']
        #lng = args['lng']
        with open('progpy.py', 'w') as f:
    		f.write(code)
    	#making file executable 
    	client.images.build(path='.',tag='sandbox')
    	print(os.getcwd())
    	st = os.stat('output.py')
    	os.chmod('output.py', st.st_mode | stat.S_IEXEC)
    	stdout = client.containers.run("sandbox",["python","progpy.py"])
    	print(stdout)
        return {"stdout": stdout}  

api.add_resource(TodoSimple, '/')

port = int(os.environ.get("PORT", 82))
app.run(host='localhost', port=port)