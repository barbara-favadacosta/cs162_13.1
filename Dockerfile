FROM python:3.6

WORKDIR /app

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

ADD app.py /app.py

EXPOSE 80

CMD ["python", "app.py"]