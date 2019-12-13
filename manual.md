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
   python bmservice.py
   ```

6. Finally, navigate to http://localhost:5000/ or the displayed link to make sure the service works

## Integration with Docusaurus 

To get bookmanager working through docusaurus. First run:

```bash
cd to the directory of your local repository.
cd docusaurus-tutorial
```

Then, enter the ```docusaurus-init``` command in the terminal.

```bash
docusaurus-init
```

This might take some time. Be patient.

Here's an example directory that will be created. Some example
documentation pages (under docs) and blog posts (under website/blog) are
included.

```
├── Dockerfile
├── docker-compose.yml
├── docs
│   ├── doc1.md
│   ├── exampledoc4.md
└── website
       ├── siteConfig.js
       └── yarn.lock
```

Next, run ```cd website``` to go in the ```website``` directory.
Then run ```npm start```. ```yarn start``` works as well.

A new browser window opens up at http://localhost:3000.

Hooray! We now have an HTML site. Now it's time to run some other commands.

### Adding Pages

We first need a documentation page. In the docs folder make a file and
name it whatever you like (we chose TRex1.md). This will be in the root
section of the Docusaurus site.

Here is what the first page/file should look like:

```
const React = require('react');

const CompLibrary = require('../../core/CompLibrary.js');

const Container = CompLibrary.Container;
const GridBlock = CompLibrary.GridBlock;

function NewDoc(props) {
  return (
    <div className="docMainWrapper wrapper">
      <Container className="mainContainer documentContainer postContainer">
        <Your text here>
      </Container>
    </div>
  );
}
module.exports = NewDoc;
```

Next, pull up the file the file
`docusaurus-tutorial/website/siteConfig.js` and place the values below in
there.

```
const siteConfig = {
  ...
  url: 'https://USERNAME.github.io', // Replace USERNAME with your GitHub username.
  baseUrl: '/bookmanager-service/', // The name of the bookmanager service
  projectName: 'bookmanager-service',  // The name of the bookmanager service. Same as above.
  ...
}
```

In the website directory, run ```npm run build``` or ```yarn build```.
The command generates a build directory inside the website directory,
containing HTML files (and other file types) for all of your docs and
other pages. Make sure the docusaurus-tutorial/website/build directory
is successfully created before running the next step.

Replace all necessary items like 'USERNAME' with your username.

Now run: 

```
GIT_USER=USERNAME CURRENT_BRANCH=master USE_SSH=true npm run publish-gh-pages # SSH
```

Now you can see bookmanager on github at https://github.com/USERNAME/bookmanager!


## References: 

* <https://docusaurus.io/docs/en/tutorial-create-new-site>

* <https://www.modelplusmodel.com/plugins/bookmanager.html>
