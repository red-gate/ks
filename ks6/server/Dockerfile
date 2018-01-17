FROM python:3.5

WORKDIR ..

ADD ./server ./server
ADD ./app/build ./server/app/build 

WORKDIR /server

RUN pip install -r requirements.txt

ENV FLASK_APP=/server/server.py

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["server.py"]