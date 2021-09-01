FROM python:3.8

RUN apt update && apt install dumb-init -y && pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT [ "/sbin/my_init", "--" ]

CMD [ "tools/run.sh" ]