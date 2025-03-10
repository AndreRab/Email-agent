FROM python:3.9

WORKDIR /app
COPY agent.py agent_server.py requirements.txt keys.py constants.py system_prompt.txt /app/

RUN pip install -r requirements.txt

CMD [ "python", "agent_server.py"]