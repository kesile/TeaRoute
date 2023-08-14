error = {
        "name": "error",
        "description": "Use this when you cannot classify the input with your options.",
        "parameters": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "In 2 sentences, explain why you cannot classify it.",
                }
            },
            "required": ["reason"],
        },
    }