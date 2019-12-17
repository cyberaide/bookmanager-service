import subprocess
from pathlib import Path

#
# sshoudl that not be integrated into
#
# bbookmanagerserice.command.bookmanagerservice.
# than we can use cms bookmanagerservice ....?
#

host = "127.0.0.1"
host = "0.0.0.0"
port = "5000"

def bmservice():
    p = str(Path('.').absolute())
    strt = f'docker run --rm -it -p {host}:{port}:{port}/tcp -w /opt/project/bookmanager-service '
    envs = '-e "FLASK_APP=/opt/project/bookmanager-service/cloudmesh/bookmanagerservice/service/app.py" -e "FLASK_ENV=development" '
    vol = '-v ' + str(
        Path('.').absolute()) + ':/opt/project/bookmanager-service bigdata:v1 '
    pcmd = f'python -u -m flask run --host {host}'
    final = strt + envs + vol + pcmd
    print(final)
    subprocess.run(final, shell=True)


if __name__ is "__main__":
    bmservice()
