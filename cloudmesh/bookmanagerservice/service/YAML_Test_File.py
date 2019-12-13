import sys
import os
os.chdir('bookmanager-service')

sys.path.append(os.getcwd() + '\\cloudmesh\\bookmanagerservice\\service')
import getdata

bks = getdata.getBooks(onlybooks=True)
tstbk = list(bks.keys())[1]
bkinfo = getdata.getBooks(onlybooks = False, filename = bks[tstbk])

#All Data
data = bkinfo[tstbk]['data']
links = bkinfo[tstbk]['links']
metadata = bkinfo[tstbk]['metadata']

#Data to generate book
#The book should be heading Preface, with the remaining 3 under it
id = ['PREFACE','MAPREDUCE/HADOOP_ECOSYSTEM/TWISTER_Twister2_Installation','REST'
	,'REST/REST_WITH_EVE','CONTAINER/DOCKER_PAAS_Docker_and_Docker_Swarm_on_FutureSystems']

"""
this should be the structure of this YAML FILE
---
metadata:
  image: "cover.png"
  title: "Cloud Computing"
  subtitle: ""
  author: "Gregor von Laszewski"
  subauthor: "Editor"
  email: "laszewski@gmail.com"
  url: "https://cloudmesh-community.github.io/book/vonlaszewski-cloud.epub"
  description: "Proposed Lecture content (subject to change)"
  abstract: "Proposed Lecture content (subject to change)"
  keywords: "Cloud, virtual machines, containers, cloud engenering"
  stylesheet: "epub.css"
  dest: "./dest/book"
  filename: "vonLaszewski-cloud.epub"
  rights: (c) Gregor von Laszewski, 2018, 2019

Preface:
  MAPREDUCE:
    Hadoop Ecosystem:
	  TWISTER_Twister2_Installation  #The last layes should alwasy be links
REST:	  
  REST:
	Rest With Eve #The last layes should alwasy be links
  CONTAINER:
     DOCKER_PAAS_Docker_and_Docker_Swarm_on_FutureSystems  #The last layes should alwasy be links
"""
	
print(len(data))
print(len(links))
