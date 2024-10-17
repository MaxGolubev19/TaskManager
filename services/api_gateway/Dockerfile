FROM python:3.9-slim

WORKDIR /services/common
COPY /common/ .

WORKDIR /services/api_gateway
COPY /api_gateway/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /api_gateway/ .

ENV PYTHONPATH=/

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
