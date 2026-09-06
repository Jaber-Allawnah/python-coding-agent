import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from pycodeagent.prompts import system_prompt
from pycodeagent.tools.schemas import available_functions
from pycodeagent.agent.tool_dispatcher import call_function


def run_agent(user_prompt: str, verbose: bool = False):

    load_dotenv()
    api_key = os.environ.get("API_KEY")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [{"role": "system", "content": system_prompt},{"role": "user", "content": user_prompt}]

    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools= available_functions
        )

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose)
                if not result_message["content"]:
                    raise Exception("Function returned empty content")

                messages.append(result_message)
                if verbose:
                    print(f"-> {result_message['content']}")
        else:
            print("Response:", message.content)
            if verbose:
                print("User prompt:", user_prompt)
                print("Prompt tokens:", response.usage.prompt_tokens)
                print("Response tokens:", response.usage.completion_tokens)
            sys.exit(0)

    sys.exit("Agent exceeded the number of iterations, stopped to avoid infinite looping")
