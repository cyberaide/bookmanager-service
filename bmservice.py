import subprocess
from pathlib import Path
p = str(Path('.').absolute())
strt = 'docker run --rm -it -p 0.0.0.0:5000:5000/tcp -w /opt/project/bookmanager-service '
envs = '-e "FLASK_APP=/opt/project/bookmanager-service/cloudmesh/bookmanagerservice/service/app.py" -e "FLASK_ENV=development" '
vol= '-v '+ str(Path('.').absolute()) + ':/opt/project/bookmanager-service bigdata:v1 '
pcmd = 'python -u -m flask run --host 0.0.0.0'
final = strt + envs + vol + pcmd
print(final)
subprocess.run(final, shell = True)



