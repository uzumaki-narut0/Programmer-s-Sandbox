import docker
client = docker.from_env()
print('in here! fellas!!')
client.containers.run("sandbox")
#print(container.logs())