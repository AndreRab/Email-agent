from agent import *

def get_messages_from_sender(email):
  if email == 'sunchulin@gmail.com':
    return [
        {
            'email': 'sunchulin@gmail.com',
            'topic': 'Math tutor',
            'content': 'Do u find a math tutor?' 
        },
        {
            'email': 'sunchulin@gmail.com',
            'topic': 'tutor',
            'content': 'I see u have found it' 
        }, 
      ]
  return []

def get_unread():
  return [
      {
          'email': 'sunchulin@gmail.com',
          'topic': 'tutor',
          'content': 'I see u have found it' 
      }, 
    ] 

def final_answer(answer):
  print(answer)

available_actions = {
    'get_messages_from_sender': get_messages_from_sender,
    'get_unread': get_unread,
    'final_answer': final_answer
}

def default_action():
    return 'something went wrong, format your action properly'

agent = Agent(BASE_MODEL_URL, MODEL_NAME, MODEL_API_KEY, system_prompt_path='system_prompt.txt')
user_prompt = 'Check my mail and refresh my memory about old conversations'
print(agent(user_prompt, available_actions, default_action, debug=True))