FROM python:3.11

WORKDIR /services/common
COPY /common .

WORKDIR /services/user_service
COPY /user_service/requirements.txt .

RUN pip install -r requirements.txt

COPY /user_service .

ENV PYTHONPATH=/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
