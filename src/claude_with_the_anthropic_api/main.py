"""This is a simple example of how to use the Anthropic API to have a multi-turn conversation with the Claude model. 
The conversation is about writing a haiku about the ocean and then commenting on it.
"""

from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages, system=None, model=None, temperature=0.7, stream=False):
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": 200,
        "temperature": temperature,
        "stream": stream,
    }
    if system:
        params["system"] = system
    response = client.messages.create(**params)
    if stream:
        full_text = ""
        for chunk in response:
            if chunk.type == "content_block_delta" and chunk.delta.type == "text_delta":
                print(chunk.delta.text, end="", flush=True)
                full_text += chunk.delta.text
        print()
        return full_text
    else:
        return response.content[0].text

def main():
    system = """
    You are a helpful haiku-writing assistant.
    You guide the user through writing a haiku about any topic they choose.
    Guide the user step by step.
"""
    messages = []
    while True:
        user_input = input("You: ")
        add_user_message(messages, user_input)
        print("Assistant: ", end="", flush=True)
        assistant_response = chat(messages, system=system, model=model, stream=True)
        add_assistant_message(messages, assistant_response)

if __name__ == "__main__":
    main()
