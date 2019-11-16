# Instructions to get the Docker Service Running


 1. Please ensure docker is installed and under setting expose daemon on tcp... is checked

2. Please ensure under shared drive c is checked

1. Navigate to the bookmanager-service folder and open [terminal/powershell] here
   - Windows users do not use command prompt
   - You can type powershell in the address bar of the folder directory to bring it up

2. Type docker build -t bigdata:v1 .

3.  Type docker run -it -p 0.0.0.0:5000:5000/tcp -v C:/Users/Nick/Documents/GitHub:/opt/project bigdata:v1
    - Replace C:/Users/Nick/Documents/GitHub with your directory

4. Type cd /opt/project/bookmanager-service/

5. Type export FLASK_APP=/opt/project/bookmanager-service/cloudmesh/bookmanagerservice/service/app.py

6. Type export FLASK_ENV=development

7. Type python -u -m flask run --host 0.0.0.0

8. Navigate to http://localhost:5000/ or the displayed link
