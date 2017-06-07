import docker
client = docker.from_env()
print('in here! fellas!!')
container = client.containers.run("sandbox", "echo helloworld")
print(container.logs())