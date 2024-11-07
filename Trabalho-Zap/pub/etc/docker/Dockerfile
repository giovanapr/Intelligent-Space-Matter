FROM python:3.12-slim

WORKDIR /app

COPY pub-zap.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python","pub-zap.py"]
