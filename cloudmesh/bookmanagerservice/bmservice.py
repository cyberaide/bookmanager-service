import subprocess
from pathlib import Path

host = "0.0.0.0"
#host = "127.0.0.1"
port = "5000"
image = "bookmanager-service"
#  DONT CHANGE ITS IN THE CONTAINER path = "."

def bmservice():
    directory = str(Path('.').absolute())
    strt = f'docker run --rm -it -p {host}:{port}:{port}/tcp -w /opt/project/bookmanager-service '
    envs = '-e "FLASK_APP=/opt/project/bookmanager-service/cloudmesh/bookmanagerservice/service/app.py" -e "FLASK_ENV=development" '
    vol = f'-v {directory}:/opt/project/bookmanager-service {image}:latest '
    pcmd = f'python -u -m flask run --host {host}'
    final = strt + envs + vol + pcmd
    print(final)
    subprocess.run(final, shell=True)


if __name__ == "__main__":
    bmservice()
