import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

exit_code, output = container.exec_run("cat /etc/passwd")
print(
    f"Attempt to read /etc/passwd: "
    f"Exit Code {exit_code}, Output: {output.decode()}"
)

exit_code, output = container.exec_run("/bin/bash")
print(
    f"Attempt to execute /bin/bash: "
    f"Exit Code {exit_code}, Output: {output.decode()}"
)

container.stop()
container.remove()