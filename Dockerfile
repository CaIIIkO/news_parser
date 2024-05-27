FROM python:3.10-slim

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

WORKDIR /app

COPY ./news_server .

COPY ./entrypoint.sh .
RUN chmod 777 entrypoint.sh
CMD ["./entrypoint.sh"]