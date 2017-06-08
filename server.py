import docker
from flask import Flask, request
from flask_restful import Resource, Api
import os

client = docker.from_env()
print('in here! fellas!!')

app = Flask(__name__)
api = Api(app)

#stdout = {}


class TodoSimple(Resource):
    def get(self):
    	stdout = client.containers.run("sandbox","python progpy.py")
    	#docker.wait(contid)
    	#stdout = container
    	print(stdout)
        return {"stdout": stdout}

    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/')

port = int(os.environ.get("PORT", 82))
app.run(host='localhost', port=port)