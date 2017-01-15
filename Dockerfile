FROM python:2.7

EXPOSE 5000
ADD . /code
WORKDIR /code
RUN pip install flask redis

CMD python app.py
