import openai
import json
from .embed import embed

import threading
lock = threading.Lock()

def chat(prompt, file_path, funcs, write, instructions="Classify this item."):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": "Always answer in a function call."},
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt},
        ],
        functions=funcs,
        function_call="auto",
    )

    function_call_name = output["choices"][0]["message"]["function_call"]["name"]

    data_to_save = {"prompt": embed(prompt), "output": function_call_name}

    if write == True:
        with lock:  # Acquire the lock before reading the file
            try:
                with open(file_path, "r") as json_file:
                    try:
                        data = json.load(json_file)
                    except json.decoder.JSONDecodeError:
                        data = []
                    data.append(data_to_save)

            except FileNotFoundError:
                data = [data_to_save]

        with lock:  # Acquire the lock before writing to the file
            with open(file_path, "w") as json_file:
                json.dump(data, json_file)

        # print(prompt + " -> " + function_call_name)

    return function_call_name