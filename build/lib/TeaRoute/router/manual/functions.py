from .error import error

def makeFunctions(buckets):
    functions = []
    functions.append(error)
    for bucket in buckets:
        temp = {
            "name": bucket.replace(" ", "_"),
            "description": buckets[bucket],
            "parameters": {
                "type": "object",
                "properties": {
                    "reason": {
                        "type": "string",
                        "description": f"The reason you classified the input as a {bucket}",
                    }
                },
                "required": ["reason"],
            },
        }
        functions.append(temp)
    
    return functions
