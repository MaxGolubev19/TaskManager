FROM python:3.11

WORKDIR /services/common
COPY /common .

WORKDIR /services/board_service
COPY /board_service/requirements.txt .

RUN pip install -r requirements.txt

COPY /board_service .

ENV PYTHONPATH=/

EXPOSE 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
