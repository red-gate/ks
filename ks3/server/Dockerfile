FROM python:3.5

WORKDIR .

ADD ./server ./server

WORKDIR /server

RUN pip install -r requirements.txt

ENV FLASK_APP=/server/server.py

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["server.py"]