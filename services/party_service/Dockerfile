FROM python:3.11

WORKDIR /services/common
COPY /common .

WORKDIR /services/party_service
COPY /party_service/requirements.txt .

RUN pip install -r requirements.txt

COPY /party_service .

ENV PYTHONPATH=/

EXPOSE 8004

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004"]
