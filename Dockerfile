From python:3.8-slim-buster

WORKDIR  /app

COPY . /app/

RUN pip install -r requirements.txt

# EXPOSE 8080

CMD ["python3","app.py"]