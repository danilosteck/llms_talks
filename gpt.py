import openai
import os
from config import config
import json

cfg = config()

# gets API Key from environment variable OPENAI_API_KEY
os.environ['OPENAI_API_KEY'] = cfg['api_keys']['openai']
# client = openai.OpenAI()

class ChamadoOpenAI():
    
    def __init__(self, model, assistant_instructions):
        self.model = model
        self.assistant_instructions = assistant_instructions
        self.client = openai.OpenAI()

    def create_assistant(self):
        assistant = self.client.beta.assistants.create(
            name="Assistant",
            instructions=self.assistant_instructions,
            tools=[{"type": "code_interpreter"}],
            model=self.model,
        )
        return assistant
    
    def call(self, call_content:str):
        thread = self.client.beta.threads.create()
        message = self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=call_content,
        )
        return thread, message
    
    def run(self, call_content:str):
        thread, _ = self.call(call_content)
        assistant = self.create_assistant()
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions="Stick to your role!",
        )
        if run.status == "completed":
            messages = self.client.beta.threads.messages.list(thread_id=thread.id)
            json_messages = json.loads(messages.to_json())

            # retorno_chamado = json_messages['data'][0]['content'][0]['text']['value']

        return json_messages
    
    def get_content_from_run(self, json_messages):
        return json_messages['data'][0]['content'][0]['text']['value']
        

if __name__ == '__main__':

    open_ai = ChamadoOpenAI(modelo = "gpt-4-1106-preview",
                            assistant_instructions='You are a helpful code assistant with lots of experience in Python.')

    msg = 'I want to create a code that uses the openAI API to pass instructions to an assistant, pass a message in string and receive a string in response based on the message.'
    orun = open_ai.run(msg)
