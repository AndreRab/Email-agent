FROM python:3.9

WORKDIR /app
COPY bot.py keys.py constans.py requirements.txt /app/

RUN pip install -r requirements.txt
CMD [ "python", "bot.py"]