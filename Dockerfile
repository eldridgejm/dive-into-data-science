FROM eldridgejm/dive_into_data_science-base:latest

ARG USER_ID=1000

RUN useradd -u ${USER_ID} -ms /bin/bash runner
USER runner
WORKDIR /home/runner

ADD requirements.txt /home/runner/requirements.txt
RUN python3 -m venv env && ./env/bin/pip install wheel
RUN ./env/bin/pip install -r requirements.txt
RUN ./env/bin/jupyter contrib nbextension install --user && ./env/bin/jupyter nbextension enable spellchecker/main
