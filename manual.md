# Book Manager Service Documentation

Naimesh
Gregor von Laszewski
Kang
Josiah

# TODO: UPDATET THE BUMPVERSION


## Rerequisits


### Native Install

GREGOR ADDS THE NATIVE WAY

## Docker Install

GREGOR FIXES THE DOCKER AND HAVE IT TESTED WITH NAIMESH

## Instructions to get the Docker Service Running

GREGOR MAKES SUGGESTION ON HOW TO DO THE 

1. First, make sure docker is installed and under settings confirm that
  the daemon on tcp box is checked
   
   * Download File Link: <https://www.docker.com/products/docker-desktop>
   
     * You will need to create a docker hub account to be able to download
   
   * Windows Installation Instructions: <https://docs.docker.com/docker-for-windows/install/>
   * Mac Installation Instructions: <https://docs.docker.com/docker-for-mac/install/>

2. Next, navigate to docker preferences

   * Windows 10 Pro or Edu: Under shared drives please make sure your 
     local drives are checked
   * <img src="https://docs.docker.com/docker-for-windows/images/settings-shared-drives.png" alt="alt text" width="500" height="400">
   * Mac: Under file sharing please make sure your local drives are added 
   * <img src="https://docs.docker.com/v17.12/docker-for-mac/images/menu/d4m-menu-prefs-fileshare.png" alt="alt text" width="500" height="400">
  
3. For Windows users, if you do not have Git you will need to install it 
   from the following link: https://git-scm.com/download/win
4. Navigate to your preferred location for downloading and open the 
   Terminal/PowerShell in that directory
5. Clone the bookmanager-service to your prefered location using **git** 
   and click on the folder that appears

   ```bash
   git clone git@github.com:cyberaide/bookmanager-service.git 
   cd bookmanager-service
   ```

5. Within Terminal/Powershell type the following commands: 

    TOO DO: RENAME IMAGE TO bookmanager-service
    
   ```bash 
   docker build -t bigdata:v1 .
   ```
   
   The next lines are still done on the host system as we assume the 
   file system is mounted as a volume into the container, so that the 
   host sysme and the container has the same volume.


   Gregor: please fix this to show how to do this from teh commandlin 
   and than remove the volume mount documention.
   
   the new docker file has a completly isolated instalation, and we just 
   need to fix the documentaion. this her is used for debugging
    
   ```
   pip install -e . 
   bookmanager-service
   ```
   
   

6. Finally, navigate to <http://localhost:5000/> or the displayed link to
   make sure the service works

## References: 

* <https://www.mkdocs.org/#getting-started>

* <https://www.mkdocs.org/user-guide/deploying-your-docs/>
