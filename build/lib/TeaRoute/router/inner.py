import openai, os

from .manual.functions import makeFunctions
from .methods.chat import chat
from .methods.embed import embed
from .methods.training import trainFile
from .methods.route import route

class Router:
    def __init__(self):
        self.buckets = {}
        pass

    def trainWithFile(self, file, batchSize):
        instructions = makeFunctions(self.buckets)
        code = trainFile(file, instructions, chat, embed, batchSize)
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
        return route(question, embed)

    def manualAnswer(self, question):
        return chat(question, makeFunctions(self.buckets), False), 200

    def learnAndRoute(self, question):
        instructions = makeFunctions(self.buckets)
        code = chat(question, instructions, True), 200
        return code

    def wipe(self):
        with open(r"router\db\trainingData.json", 'w') as file:
            pass
        return 200
