## Instructions on how to get the Bookmanager Service to run on your device


## Instructions to get the Docker Service Running


1. First, make sure docker is installed and under settings confirm that the daemon on tcp box is checked
   * Download File Link: https://www.docker.com/products/docker-desktop
       * You will need to create a docker hub account to be able to download
   * Windows Installation Instructions: https://docs.docker.com/docker-for-windows/install/
   * Mac Installation Instructions: https://docs.docker.com/docker-for-mac/install/

2. Next, navigate to docker preferences
   * Windows: Under shared drives please make sure your local drives are checked
   * <img src="https://docs.docker.com/docker-for-windows/images/settings-shared-drives.png" alt="alt text" width="500" height="400">
   * Mac: Under file sharing please make sure your locka drives are added. 
   * <img src="https://docs.docker.com/v17.12/docker-for-mac/images/menu/d4m-menu-prefs-fileshare.png" alt="alt text" width="500" height="400">

3. For Windows users, if you do not have Git you will need to install it from the following link: https://git-scm.com/download/win
4. Navigate to your preferred location for downloading and open the Terminal/PowerShell in that directory
5. Clone the bookmanager-service to your prefered location using **git** and click on the folder that appears
  ```bash
   git clone git@github.com:cyberaide/bookmanager-service.git 
   cd bookmanager-service
  ```
5. Within Terminal/Powershell type the following commands: 
```bash 
docker build -t bigdata:v1 .
python bmservice.py
```

6. Finally, navigate to http://localhost:5000/ or the displayed link to make sure the service works

