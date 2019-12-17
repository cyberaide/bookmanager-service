# Manual on how to get the Bookmanager Service to run


## Instructions to get the Docker Service Running


1. First, make sure docker is installed and under settings confirm 
   that the daemon on tcp box is checked
   
   * Download File Link: https://www.docker.com/products/docker-desktop
   
     * You will need to create a docker hub account to be able to download
   
   * Windows Installation Instructions: https://docs.docker.com/docker-for-windows/install/
   * Mac Installation Instructions: https://docs.docker.com/docker-for-mac/install/

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

   ```bash 
   docker build -t bigdata:v1 .
   pip install -e . 
   bookmanager-service
   ```

6. Finally, navigate to http://localhost:5000/ or the displayed link to make sure the service works

## How to get Bookmanager to run with MkDocs

The site files for bookmanager are within the project repository (gh-pages by default, but in ours they're located in ```site```). 

First perform the command of ```git-checkout``` on the main working branch (master) of the git repository where the source documentation is for your project, and then run the following command:

```mkdocs gh-deploy```

You've done it! Now unseen, MkDocs will build the docs and use ```ghp-import``` to commit to the ```gh-pages``` branch, then pushing the ```gh-pages``` branch out to GitHub.

Use ```mkdocs gh-deploy --help``` to get more options for the ```gh-deploy``` command.

Note: You can't review the built site right as it's pushed out to GitHub. So you might want to verify made changes to the docs first through using the ```build``` or ```serve``` commands and then reviewing the built files perhaps locally.

## References: 

* <https://www.mkdocs.org/#getting-started>

* <https://www.mkdocs.org/user-guide/deploying-your-docs/>
