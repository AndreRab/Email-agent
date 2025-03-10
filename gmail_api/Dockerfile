FROM python:3.9

WORKDIR /app
COPY server.py credentials.json requirements.txt keys.py constants.py /app/

RUN pip install -r requirements.txt

CMD [ "python", "server.py"]