FROM python:3.12-slim

WORKDIR /app
COPY pub-img.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python","pub-img.py"]
