FROM python:3.11

WORKDIR /services/common
COPY /common .

WORKDIR /services/adventure_service

COPY /adventure_service/requirements.txt .
RUN pip install -r requirements.txt

COPY /adventure_service .

ENV PYTHONPATH=/

EXPOSE 8003

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
