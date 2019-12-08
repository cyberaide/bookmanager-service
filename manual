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

3. Windows users if you do not have git please install it from the following link: https://git-scm.com/download/win
4. Navigate to your preferred location for download and open Terminal/PowerShell in that directory
5. Clone the bookmanager-service to you prefered location using **git** and go into the folder
  ```bash
   git clone git@github.com:cyberaide/bookmanager-service.git 
   cd bookmanager-service
  ```
5. Within Terminal/Powershell type the following commands: 
```bash 
docker build -t bigdata:v1 .
python bmservice.py
```

6. Navigate to http://localhost:5000/ or the displayed link

