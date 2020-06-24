IMAGE_TAG=latest

define build_book
	docker run \
		--mount type=bind,src=$(shell pwd),target=/document \
		-e PYTHONPATH=/document/extensions \
		dive_into_data_science:${IMAGE_TAG} \
		/home/runner/env/bin/jupyter-book \
		build \
		$(1) \
		/document/book
endef


.PHONY: html
html: docker
	# build the HTML version of the textbook
	$(call build_book,--builder html)


.PHONY: pdf
pdf: docker
	# build the PDF version using LaTeX
	$(call build_book,--builder pdflatex)
	cd book/_build/latex && make


.PHONY: notebooks
notebooks: docker
	# take the notebooks used as source documents and remove tagged cells,
	# placing them in the notebooks/ directory.
	docker run \
		--mount type=bind,src=$(shell pwd),target=/document \
		dive_into_data_science:${IMAGE_TAG} \
		bash -c " \
		cd /document/notebooks && \
		/home/runner/env/bin/python \
		/document/scripts/make_student_notebooks.py \
		/document/book"


.PHONY: docker
init: docker
	# intialize the repository for development
	git config --local core.hooksPath .githooks/


.PHONY: docker
docker:
	# build the docker image used in the build process
	# usually unnecessary to run, as the image on DockerHub will
	# work for most people.
	#
	# one instance where you'd want to build this: your UID
	# is not 1000. In that case, `make docker` will create an
	# image using the appropriate user ID.
	docker build --build-arg USER_ID=$(shell id -u) . \
		-t dive_into_data_science:${IMAGE_TAG}


.PHONY: jupyter
jupyter:
	# start a jupyter notebook server within the docker container
	# used to build the textbook
	docker run -it -p 8888:8888 \
		--mount type=bind,src=$(shell pwd),target=/home/runner/host \
		dive_into_data_science:${IMAGE_TAG} ./env/bin/jupyter notebook --ip=0.0.0.0


.PHONY: shell
shell:
	# start a shell within the docker container used to build the textbook
	docker run -it \
		--mount type=bind,src=$(shell pwd),target=/home/runner/host \
		dive_into_data_science:${IMAGE_TAG}


.PHONY: clean
clean:
	rm -rf book/_build
