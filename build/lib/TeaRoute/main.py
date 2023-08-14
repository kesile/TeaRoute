import openai, time, os
from .router.inner import Router

class Tear:
    def __init__(self, file_path, api_key, organization = False):
        openai.api_key = api_key
        self.file_path = file_path
        if organization: openai.organization = org
        self.internalRouter = Router(file_path)
        self.buckets = self.internalRouter.buckets
    
    def addBuckets(self, buckets): # Add training categories.
        code = self.internalRouter.addBuckets(buckets)
        return code

    def removeBuckets(self, buckets): # Remove training categories.
        code = self.internalRouter.removeBuckets(buckets)
        return code
    
    def train(self, questions, batchSize=5): # Train the model from a list of questions.
        code = self.internalRouter.trainWithFile(questions, batchSize)
        return {"code" : code[0], "cost" : code[1]}

    def manualRoute(self, inp): # Route the question with LLM instead of embeddings without adding to training data.
        code = self.internalRouter.manualAnswer(inp)
        return {"output" : code[0], "code" : code[1]}

    def route(self, inp): # Route the question using embeddings.
        code = self.internalRouter.route(inp)
        return {"output" : code[0], "code" : code[1]}

    def routeLearn(self, inp): # Train the model while also routing questions.
        code = self.internalRouter.learnAndRoute(inp)
        return {"output" : code[0], "code" : code[1]}

    def wipe(self): # Wipe the training data.
        code = self.internalRouter.wipe()
        return code