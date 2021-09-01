FROM python:3.8-alpine3.13

RUN apk update && apk add dumb-init

COPY . /just4fun

WORKDIR /just4fun

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "/usr/local/bin/dumb-init", "--" ]

CMD [ "tools/run.sh" ]
