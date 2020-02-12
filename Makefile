package=bookmanagerservice
UNAME=$(shell uname)
export ROOT_DIR=${PWD}/cloudmesh/rest/server
MONGOD=mongod --dbpath ~/.cloudmesh/data/db --bind_ip 127.0.0.1
VERSION=`head -1 VERSION`

define banner
	@echo
	@echo "###################################"
	@echo $(1)
	@echo "###################################"
endef

ifeq ($(UNAME),Darwin)
define terminal
	osascript -e 'tell application "Terminal" to do script "$(1)"'
endef
endif
ifeq ($(UNAME),Linux)
define terminal
	echo "Linux is not yet supported, fix me"
endef
endif
ifeq ($(UNAME),Windows)
define terminal
	echo "Windows is not yet supported, fix me"
endef
endif

doc:
	cd paper; make

requirements:
	echo "cloudmesh-cloud" > tmp.txt
	pip-compile setup.py
	fgrep -v "# via" requirements.txt | fgrep -v "cloudmesh" >> tmp.txt
	mv tmp.txt requirements.txt
	git commit -m "update requirements" requirements.txt
	git push






view:
	# opening bookmanager
	open -a skim docs/vonLaszewski-bookmanager.pdf



source:
	pip install -e .
	cms help


clean:
	rm -rf *.zip
	rm -rf *.egg-info
	rm -rf *.eggs
	rm -rf docs/build
	rm -rf build
	rm -rf dist
	find . -type d -name __pycache__ -delete
	find . -name '*.pyc' -delete
	find . -name '*.pye' -delete
	rm -rf .tox
	rm -f *.whl

install:
	cd ../common; pip install .
	cd ../cmd5; pip install .
	pip install .

######################################################################
# DOCKER
######################################################################

image:
	docker build  -t bookmanager-service:1.0.0 -t bookmanager-service:latest .

#
# cm munts all parent directories into the container
#
cm:
	docker run -v `pwd`/..:/cm -w /cm --rm -it cloudmesh/bookmanager:1.0.0  /bin/bash

shell:
	docker run --rm -it cloudmesh/bookmanager:1.0.0  /bin/bash

cms:
	docker run --rm -it cloudmesh/bookmanager:1.0.0

dockerclean:
	-docker kill $$(docker ps -q)
	-docker rm $$(docker ps -a -q)
	-docker rmi $$(docker images -q)

push:
	docker push cloudmesh/bookmanager:1.0.0
	docker push cloudmesh/bookmanager:latest

run:
	docker run cloudmesh/bookmanager:1.0.0 /bin/sh -c "cd books/book/cloud; git pull; make"

######################################################################
# PYPI
######################################################################


twine:
	# installing twine
	pip install -U twine

dist:
	# setting up wheel
	python setup.py sdist bdist_wheel
	twine check dist/*

patch: clean
	$(call banner, "bbuild")
	bump2version --allow-dirty patch
	python setup.py sdist bdist_wheel
	# git push origin master --tags
	twine check dist/*
	twine upload --repository testpypi  dist/*
	$(call banner, "install")
	#sleep 10
	#pip install --index-url https://test.pypi.org/simple/ cloudmesh-$(package) -U

minor: clean
	$(call banner, "minor")
	bump2version minor --allow-dirty
	@cat VERSION
	@echo

release: clean
	$(call banner, "release")
	git tag "v$(VERSION)"
	git push origin master --tags
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository pypi dist/*
	$(call banner, "install")
	@cat VERSION
	@echo


dev:
	bump2version --new-version "$(VERSION)-dev0" part --allow-dirty
	bump2version patch --allow-dirty
	@cat VERSION
	@echo

reset:
	bump2version --new-version "4.0.0-dev0" part --allow-dirty

upload:
	twine check dist/*
	twine upload dist/*

pip:
	pip install --index-url https://test.pypi.org/simple/ cloudmesh-$(package) -U

#	    --extra-index-url https://test.pypi.org/simple

log:
	$(call banner, log)
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > ChangeLog
	git commit -m "chg: dev: Update ChangeLog" ChangeLog
	git push
