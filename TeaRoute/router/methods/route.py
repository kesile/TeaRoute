import openai, json
from .cos import cos

def route(question, file_path, embed):
    auxillary = {}

    with open(file_path, "r") as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                print("[NO DATA]")
    
    query = embed(question)
    
    for question in data:
        similarity = cos(query, question["prompt"])
        auxillary.update({similarity : question["output"]})

    auxillary = dict(sorted(auxillary.items(), reverse=True))
    # print(auxillary)
    auxillary = list(auxillary.values())
    return auxillary[0], 200