import docker
from flask import Flask, request
from flask_restful import Resource, Api
import os

client = docker.from_env()
print('in here! fellas!!')

app = Flask(__name__)
api = Api(app)

stdout = {}


class TodoSimple(Resource):
    def get(self):
    	container = client.containers.run("sandbox","python progpy.py",detach=True)
        return {stdout: "hello world"}

    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/')

port = int(os.environ.get("PORT", 80))
app.run(host='0.0.0.0', port=port)