# bookmanager-service

This service provides a cloud-based online bookmanager for
individualized learning material managed via cyberaide bookmanager yaml files

Cyeraide bookamanger code is available from 

* <https://pypi.org/project/cyberaide-bookmanager/>

Cyberaide bookmanager that can create books based on markdown files that
are distributed online in github. The table of content is managed
through a YAML file. Cyberaide bookmanager-service can read these yaml
files and present a graphical user interface that allows us to check on
specific sections and change the order through a convenient tree view.
  
![Screenshot](images/screenshot-bookmanager-service.png)

## Installation

We assume you have docker installed and use a Vvenv called BOOK:

```bash
python3.8 -m venv ~/BOOK
source ~/BOOK/bin/activate
```

In the activated vm do

```bash
cd ~
mkdir cm
cd cm
pip install cyberaide-bookmanager
https://github.com/cyberaide/bookmanager-service.git
cd bookmanager-service
make image
pip install -e .
bookmanager-service
```

In your web browser open 

```
localhost:5000
```

Make sure to close the container with CTRL-C once done.

More instaltion instruction can be found in the [Manual](manual.md) (alpha)

## Container

A container is available but we have not yet documented how to use it 

## Adding new book tamplates

The book tamplates are in 

`bookmanager-service/books`

you should be able to modify them in your local copy.

## Bugs

1. Selecting a chapter should automatically select the parents. This is not yet implemented.
2. REFERENCES must always bee checked on.
3. The container is not yet using mount or the host network.
4. This has only ben tested on macOS

## Credit

Nitesh and Gregor. Please contact Gregor von Laszewski for more
information.


## References

Bookmanager command line tool links:

1. <https://github.com/cyberaide/bookmanager-service>
2. <https://pypi.org/project/cyberaide-bookmanager/>
3. <https://github.com/cyberaide/bookmanager>
4. <https://github.com/cyberaide/bookmanager/blob/master/README.md>


