FROM python:3.8-alpine3.13

RUN apk update && apk add dumb-init

COPY . /just4fun

WORKDIR /just4fun

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN chmod a+x tools/run.sh

ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]

CMD [ "/bin/sh", "-c", "tools/run.sh && tail -f /dev/null" ]
