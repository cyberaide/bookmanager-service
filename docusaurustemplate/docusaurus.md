---
id: docusaurus
title: This is HTML through Docusaurus
---

You can write additional content using [GitHub-flavored Markdown syntax](https://github.github.com/gfm/) if you so desire.

## Docusaurus Template

> This is the **sample template** page from which you can run the service _HTML_ from or on your system of choice.
> It can be accessed by running the 'bookmanager-service generate --docusaurus' command.

* Useful for running in HTML
* Can try it out on different platforms

{
  "docs": {
    "Docusaurus": [
      "doc1",
+     "doc9"
    ],
    "First Category": ["doc2"],
    "Second Category": ["doc3"]
  },
  "docs-other": {
    "First Category": ["doc4", "doc5"]
  }
}
---
metadata:
  image: "cover.png"
  title: "Sample"
  subtitle: "Test"
  author: "Gregor von Laszewski"
  subauthor: ""
  email: "laszewski@gmail.com"
  url: "https://github.com/cyberaide/bookmanager"
  description: "The lecture notes for e516"
  abstract: "Lecture notes for e516"
  keywords: "Cloud, Cloud Computing"
  stylesheet: "epub.css"
  dest: "./dest/book"
  filename: "vonLaszewski-e516-proceedings.epub"
  rights: (c) Gregor von Laszewski, 2018, 2019
git:
  "book": "https://raw.githubusercontent.com/cloudmesh-community/book/master/chapters"
github:
  "community": "https://raw.githubusercontent.com/cloudmesh-community"
  "chapter": "https://raw.githubusercontent.com/cloudmesh/book/chapters/"
  "template": "https://raw.githubusercontent.com/cyberaide/bookmanager/master/bookmanager/template"
  "chapters": "https://github.com/cloudmesh-community/book/blob/master/chapters"
BOOK:
  - PREFACE:
#    - "{github.chapter}/version.md"
    - "{github.template}/disclaimer.md"
  - REPORTS:
    - "https://raw.githubusercontent.com/cloudmesh-community/book/master/books/516/reports.md"
    - "{github.community}/fa19-516-140/master/project/report.md"
    - "{github.community}/fa19-516-141/master/project/report.md"
    - "{github.community}/fa19-516-144/master/project/report.md"
    - "{github.community}/fa19-516-147/master/project/report.md"
    - "{github.community}/fa19-516-148/master/project/report.md"
    - "{github.community}/fa19-516-151/master/project/report.md"
    - "{github.community}/fa19-516-152/master/project/report.md"
    - "{github.community}/fa19-516-153/master/project/report.md"
    - "{github.community}/fa19-516-155/master/project/report.md"
    - "{github.community}/fa19-516-158/master/project/report.md"
    - "{github.community}/fa19-516-159/master/project/report.md"
    - "{github.community}/fa19-516-160/master/project/report.md"
    - "{github.community}/fa19-516-161/master/project/report.md"
    - "{github.community}/fa19-516-162/master/project/report.md"
    - "{github.community}/fa19-516-163/master/project/report.md"
    - "{github.community}/fa19-516-164/master/Project/report.md"
    - "{github.community}/fa19-516-165/master/project/report.md"
    - "{github.community}/fa19-516-166/master/project/report.md"
    - "{github.community}/fa19-516-167/master/project/report.md"
    - "{github.community}/fa19-516-168/master/project/report.md"
    - "{github.community}/fa19-516-169/master/project/report.md"
    - "{github.community}/fa19-516-171/master/project/report.md"
  - DATACENTER:
    - "{github.community}/fa19-516-140/master/datacenter.md"
    - "{github.community}/fa19-516-141/master/datacenter.md"
##      - "{github.community}/fa19-516-142/master/datacenter.md"
    - "{github.community}/fa19-516-143/master/datacenter.md"
    - "{github.community}/fa19-516-144/master/datacenter.md"
##      - "{github.community}/fa19-516-145/master/datacenter.md"      -
    - "{github.community}/fa19-516-146/master/datacenter.md"
##    - "{github.community}/fa19-516-147/master/datacenter.md"
##      - "{github.community}/fa19-516-148/master/datacenter.md"
##      - "{github.community}/fa19-516-149/master/datacenter.md"
    - "{github.community}/fa19-516-150/master/datacenter.md"
    - "{github.community}/fa19-516-151/master/datacenter.md"
    - "{github.community}/fa19-516-152/master/datacenter.md"
    - "{github.community}/fa19-516-153/master/datacenter.md"
##      - "{github.community}/fa19-516-154/master/datacenter.md"
    - "{github.community}/fa19-516-155/master/datacenter.md"
    - "{github.community}/fa19-516-156/master/datacenter.md"
    - "{github.community}/fa19-516-157/master/datacenter.md"
##    - "{github.community}/fa19-516-158/master/datacenter.md"
##    - "{github.community}/fa19-516-159/master/datacenter.md"
##    - "{github.community}/fa19-516-160/master/datacenter.md"
##      - "{github.community}/fa19-516-161/master/datacenter.md"
##    - "{github.community}/fa19-516-161/master/datacenter.md"
##    - "{github.community}/fa19-516-162/master/datacenter.md"
##    - "{github.community}/fa19-516-163/master/datacenter.md"
##    - "{github.community}/fa19-516-164/master/datacenter.md"
##    - "{github.community}/fa19-516-165/master/datacenter.md"
##    - "{github.community}/fa19-516-166/master/datacenter.md"
##    - "{github.community}/fa19-516-167/master/datacenter.md"
##    - "{github.community}/fa19-516-168/master/datacenter.md"
##    - "{github.community}/fa19-516-169/master/datacenter.md"
##    - "{github.community}/fa19-516-170/master/datacenter.md"
##    - "{github.community}/fa19-516-171/master/datacenter.md"
  ##    - "{github.chapter}/preface/corrections.md"
  ##    - "{github.chapter}/authors.md"
  ##    - "{github.chapter}/preface/create.md"
  ##    - "{github.chapter}/preface/notation.md"
  ##    - "{github.chapter}/preface/updates.md"
  ##    - "{github.chapter}/preface/emoji.md"
  - REFERENCES:
      - "{github.template}/empty.md"
