# Instructions to get the Docker Service Running


1. Please ensure docker is installed and under setting expose daemon on tcp... is checked
   * Download File Link: https://www.docker.com/products/docker-desktop
       * You will need to create a docker hub account to be able to download
   * Windows Installation Instructions: https://docs.docker.com/docker-for-windows/install/
   * Mac Installation Instructions: https://docs.docker.com/docker-for-mac/install/

2. Navigate to docker preferences
   * Windows: Under shared drives please make sure your local drives are checked
   * <img src="https://docs.docker.com/docker-for-windows/images/settings-shared-drives.png" alt="alt text" width="500" height="400">
   * Mac: Under file sharing please make sure your locka drives are added. 
   * <img src="https://docs.docker.com/v17.12/docker-for-mac/images/menu/d4m-menu-prefs-fileshare.png" alt="alt text" width="500" height="400">

3. Navigate to the bookmanager-service folder and open [terminal/powershell] here
   - Windows users do not use command prompt
   - You can type powershell in the address bar of the folder directory to bring it up

4. Within Terminal/Powershell type the following commands: 
```bash 
docker build -t bigdata:v1 .
python bmservice.py
```

6. Navigate to http://localhost:5000/ or the displayed link
