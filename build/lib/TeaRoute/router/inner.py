import openai, os

from .manual.functions import makeFunctions
from .methods.chat import chat
from .methods.embed import embed
from .methods.training import trainFile
from .methods.route import route

class Router:
    def __init__(self, file_path):
        self.buckets = {}
        self.file_path = file_path
        pass

    def trainWithFile(self, file, batchSize):
        instructions = makeFunctions(self.buckets)
        code = trainFile(file, self.file_path, instructions, chat, embed, batchSize)
        return code[0], code[1]
    
    def addBuckets(self, buckets):
        self.buckets.update(buckets)
        return 200
    
    def removeBuckets(self, buckets):
        if buckets in self.buckets:
            return 404
        else:
            self.buckets.remove(buckets)
            return 200
    
    def route(self, question):
        return route(question, self.file_path, embed)

    def manualAnswer(self, question):
        return chat(question, self.file_path, makeFunctions(self.buckets), False), 200

    def learnAndRoute(self, question):
        instructions = makeFunctions(self.buckets)
        code = chat(question, self.file_path, instructions, True), 200
        return code

    def wipe(self):
        try:
            # Try to open the file in write mode, creating it if it doesn't exist
            with open(self.file_path, 'w') as file:
                pass
            return 200
        except FileNotFoundError:
            # File doesn't exist, so create it and return 200
            with open(self.file_path, 'w') as file:
                pass
            return 200

