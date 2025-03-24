# Email-agent 🤖🤖🤖

Email-agent is an agent that helps you navigate through your emails using the Telegram Bot API. You can ask for unread messages, mark them as read, and see a short message overview for each user. Additionally, you can request specific help from the agent when you need to handle your responses quickly.

## Application Setup
1.	Clone this repository and navigate to its directory:
```bash
git clone https://github.com/AndreRab/Email-agent.git
cd Email-agent
```
2. Replace all `.env.example` files with a simple `.env` file containing your environment variables:
   - In the `agent` folder, provide the API key required to invoke any model supported by the OpenAI library.
   - In the `gmail_api` folder, generate an application key and define the `CLIENT_SECRETS_FILE` name. (See the next step for instructions on how to obtain it.)
   - In the `telegram_bot` folder, paste your bot token, which you can obtain from [@BotFather](https://t.me/BotFather).
3.	Create the `CLIENT_SECRETS_FILE` using the Google Cloud Console:
	-	Open the Google Cloud Console
	-	Create a new project
	-	Navigate to APIs & Services > Credentials
	-	Click Create Credentials and select OAuth client ID
	-	Choose Web application as the application type
	-	Add the following to Authorized redirect URIs:
```http://localhost:1000/oauth/callback```
	-	Download the credentials file
	-	Move the file to the gmail_api folder
	-	Set the correct filename in your .env file under the `CLIENT_SECRETS_FILE` variable
4. If you haven't [docker engine](https://www.docker.com/products/docker-desktop/) download

## Application Running
1.	Start your Docker engine.
2.	Build the images:
```bash
  docker-compose build --no-cache
```

3. Start the containers:
```bash 
   docker-compose -up
```
