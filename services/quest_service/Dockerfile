FROM python:3.11

WORKDIR /services/common
COPY /common .

WORKDIR /services/quest_service
COPY /quest_service/requirements.txt .

RUN pip install -r requirements.txt

COPY /quest_service .

ENV PYTHONPATH=/

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
