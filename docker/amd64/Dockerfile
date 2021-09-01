FROM python:3.8

RUN apt install dumb-init && pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT [ "/sbin/my_init", "--" ]

CMD [ "tools/run.sh" ]