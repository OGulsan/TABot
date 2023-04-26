import os

import openai
from dotenv import load_dotenv

import token_counter

MODEL = "gpt-3.5-turbo"

load_dotenv(".env")
token = os.getenv("OPEN_AI_TOKEN") 

class TABotAI():
    def __init__(self) -> None:
        self.totalTokenCount = 0
        openai.api_key = token
        self.previousRole = "assistant"
        self.previousContent = ""
        self.previousName = "none"
        self.previousQuestion = {"role": "{}".format(self.previousRole), "content": "{}".format(self.previousContent), "name": "{}".format(self.previousName)}

    def answerQuestion(self, message):
        # Messages must be an array of message objects

        # Current message object
        msgs = [
                {"role": "system", "content": "You are a Teaching Assistant discord bot for the course {}.".format(message.author.guild.name)}, # system message helps set the behavior of the assistant
                {"role": "user", "content": "{}".format(message.content.strip()[10:]), "name": "{}".format(message.author.name.strip())} # current message user asked
            ]
    
        # Make API call
        response = openai.ChatCompletion.create(
            model = MODEL,
            messages = msgs
        )
        
        # Update previous question's message object to get better responses when the user refers to prior messages 
        self.previousContent = "{}".format(message.content.strip()[10:])
        self.previousName = "{}".format(message.author.name.strip())
        self.previousQuestion = {"role": "{}".format(self.previousRole), "content": "Previous question asked was: {}.".format(self.previousContent), "name": "{}".format(self.previousName.strip())}

        # Keep track of API token usage
        currentTokenCount = token_counter.num_tokens_from_messages(messages=msgs, model=MODEL)
        self.totalTokenCount += currentTokenCount

        print("Total tokens count - {}\nToken count for this message {}".format(self.totalTokenCount + currentTokenCount, currentTokenCount))
       
        return response['choices'][0]['message']['content']
        
        
if __name__ == "__main__":
    pass