FROM python:3.9-slim

WORKDIR /services/common
COPY /common .

WORKDIR /services/adventure_service

COPY /adventure_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /adventure_service/ .

ENV PYTHONPATH=/

EXPOSE 8003

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
