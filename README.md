# Cloud-based Online Bookmanager 

This service provides a 
cloud-based online bookmanager for individualized learning material 
for big data and cloud computing

## Background

Some people at Stanford seem to think what I propose here is a
brilliant idea, so if you are interested to do this as part of the
class let me know.

## Idea

We have a tool called cyberaide bookmanager that can create books
based on markdown files that are distributed online in github (not
only for data science and cloud computing, but that is where we have
most material).

## Design Aspects

1. We like to host the creation of such a book in a container and
   place it online on a cloud or web service. (containerization is easy
   and mostly done for the command line, but not for the html/gui portion)

2. We like to allow people that visit a web page, select class modules
   that are automatically integrated in customized books for that student

3. The integration could be as simple as clicking on some chapters in a
   table of content that we distribute

4. The interface could be enabled with javascript where you drag and
   drop the chapters into a hierarchy with chapter titles that could be
   added or are derived from the included markdown

5. We would like to facilitate a markdown test that prior to the
   inclusion tests if the markdown is ok while using markdown lint
   (mdl).

6. (optional) as extension we like to include different formats, such
   as PDF, word, rst, txt, .org mode (this is in part easy as we use
   in the container pandoc that supports these formats.


## Requirement

Obviously, you need to have some Javascript/HTML/Webpage experience.
These days almost all students have them so I think that is doable. I
am open to suggestions for javascript framework, but i heard electron
may be a good choice so we can ost the service in the cloud, but also
run locally.

Other than a manual and programing the project has a 2 page report
requirement in markdown not LaTeX. The reason this is so low is that
you spend more time on programming than writing the report. You should
think of the report also like a mini manual, so you let the users know
why its good and how they can use it.

## Contact

Please contact Gregor and Geoffery via a private post. This project is
for maximal 3 participants and the selection of the participants is
competitive.

## Credit

The project can serve as class project for this course.

## Refernces

Bookmanager command line tool links:

* <https://pypi.org/project/cyberaide-bookmanager/>
* <https://github.com/cyberaide/bookmanager>
* https://github.com/cyberaide/bookmanager/blob/master/README.md>
