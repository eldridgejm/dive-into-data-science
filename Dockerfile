FROM debian:buster

ARG USER_ID=1000

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-venv \
    make

RUN apt-get update && apt-get install -y \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    latexmk

RUN useradd -u ${USER_ID} -ms /bin/bash runner
USER runner
WORKDIR /home/runner

ADD requirements.txt /home/runner/requirements.txt
RUN python3 -m venv env && ./env/bin/pip install wheel
RUN ./env/bin/pip install -r requirements.txt
