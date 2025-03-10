from openai import OpenAI
import re
import ast
from constants import *
from keys import *

class Agent():
    def __init__(self, model_url, model_name, api_key, system_prompt_path):
        self.client = OpenAI(
            base_url=model_url,
            api_key=api_key,
        )
        self.model_name = model_name
        with open(system_prompt_path, "r") as file:
            self.system_prompt = file.read()

    def get_value_from_prompt(self, text, regex):
        match = re.search(regex, text)
        if match:
            return match.group(1)
        return None

    def extract_info_of_action(self, text):
        action = self.get_value_from_prompt(text, REGEX_FOR_ACTION)  
        parameters_str = self.get_value_from_prompt(text, REGEX_FOR_PARAMETERS)  
        
        try:
            parameters = ast.literal_eval(parameters_str) if parameters_str else {}  
        except (SyntaxError, ValueError):
            parameters = {}

        return (action, parameters)
    
    def __call__(self, user_input, available_actions, default_action, chat_id, max_step_number=10, debug=False):
        print('Agent have started working')
        think_process = user_input 
        for _ in range(max_step_number):
            generated = self.generate_action(think_process, debug)
            action_name, param = self.extract_info_of_action(generated)
            
            if debug:
                print(f'The action {action_name} was chosen with parameters {param}')
            
            if action_name == 'final_answer':
                return param.get("answer", "No answer provided.")
            
            action = available_actions.get(action_name, default_action)
            result = action(**param, chat_id=chat_id)
            # if result.status_code == 401:
            #     return result
            think_process += generated + '\nObservation: ' + str(result)

    def generate_action(self, think_process, debug):
        completion = self.client.chat.completions.create(
            extra_body={},
            model=self.model_name,
            messages=[
                {
                    'role': 'system', 
                    'content': self.system_prompt
                },
                {
                    "role": "user",
                    "content": think_process
                }
            ]
        )
        generated = completion.choices[0].message.content
        if debug:
            print(f'Generated: {generated}')
        return generated