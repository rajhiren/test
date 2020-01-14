FROM python:latest

COPY . /web

WORKDIR /web

RUN pip install -r ./requirements.txt

RUN flask db migrate -m 'initial migration'
RUN flask db upgrade


EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["mytest.py"]
