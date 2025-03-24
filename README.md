# ✉️ Email-agent ✉️

Email-agent is an agent that helps you navigate through your emails using the Telegram Bot API. You can ask for unread messages, mark them as read, and see a short message overview for each user. Additionally, you can request specific help from the agent when you need to find something in your emails quickly.

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

## Bot Features 
<img width="467" alt="image" src="https://github.com/user-attachments/assets/f446995e-377b-451e-93ee-ef4104c60345" />

The bot provides 6 features. To use any of them, you need to log in first. The bot will prompt you to follow a login link:

<img width="416" alt="image" src="https://github.com/user-attachments/assets/d77b962e-3476-4126-b3bd-4622e864b5b7" />

Follow the instructions at the provided link. Once you complete the login process, you can return to Telegram when you see the following message:

<img width="367" alt="image" src="https://github.com/user-attachments/assets/e77ab544-e003-497f-a950-f407a7e7b0c7" />

To ask the agent to process your prompt, use the /agent_invoke command followed by your input:

<img width="944" alt="image" src="https://github.com/user-attachments/assets/5e440e49-b7e2-43b1-8bfe-756619f6de40" />



