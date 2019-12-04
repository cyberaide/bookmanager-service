# Instructions to get the Docker Service Running


1. Please ensure docker is installed and under setting expose daemon on tcp... is checked

2. Please ensure under shared drive c is checked

3. Navigate to the bookmanager-service folder and open [terminal/powershell] here
   - Windows users do not use command prompt
   - You can type powershell in the address bar of the folder directory to bring it up

4. Type docker build -t bigdata:v1 .

5. Type python bmservice.py

6. Navigate to http://localhost:5000/ or the displayed link
