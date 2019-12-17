# Cloud-based Online Bookmanager 

This service provides a cloud-based online bookmanager for
individualized learning material for big data and cloud computing

## Background

Some people seem to think what I propose here is a brilliant idea, so if
you are interested to do this as part of the class let me know.

## Idea

We have a tool called cyberaide bookmanager that can create books
based on markdown files that are distributed online in github (it's not
only for data science and cloud computing, but that is where we have the
most material).

## Design Aspects

1. We would like to host the creation of such a book in a container and
   place it online on a cloud or web service. (containerization is easy and
   mostly done for the command line, but not for the html/gui portion)

2. We would like to allow people tovisit a web page, select class
   modules and have them automatically integrated into a customized book
   for that student

3. The integration could be as simple as clicking on some chapters in a
   table of content that we distribute

4. The interface could be enabled with javascript where you drag and
   drop the chapters into a hierarchy with chapter titles that could be
   added or are derived from the included markdown

5. We would like to facilitate a markdown test that signals prior to the
   inclusion tests if the markdown is ok while using markdown lint (mdl).

6. (Optional) As an extension we would like to include different
   formats, such as PDF, word, rst, txt, .org mode (this should be easy as
   we use the container 'pandoc' that supports these formats).


## Requirements

Obviously, you need to have some Javascript/HTML/Webpage experience.
These days almost all students have them so I think that is doable. I am
open to suggestions for Javascript framework, but I have heard electron
may be a good choice so we can host the service in the cloud, but also
run locally.

Other than a manual and programing the project has a 2 page report
requirement in Markdown not LaTeX. The reason this is so low is that
you'll likely spend more time on programming than writing the report.
You should think of the report also like a mini manual, so you'll be
letting the users know why it's good and how they can use it.

## Contact

Please contact Gregor and Geoffery via a private post. This project is
for maximal 3 participants and the selection of the participants is
competitive.

## Credit

The project can serve as class project for this course.

## References

Bookmanager command line tool links:

* <https://pypi.org/project/cyberaide-bookmanager/>
* <https://github.com/cyberaide/bookmanager>
* <https://github.com/cyberaide/bookmanager/blob/master/README.md>
