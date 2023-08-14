# Tear - Trainable, autonomous, efficient routing.
Tear is a simple tool that allows you to easily (<10 lines of code) and cheaply (500,000/1$) control the flow of information through LLM chains via automated classification. It provides routing via two methods, LLMs and Embeddings. Furthermore, you can train an LLM on a set of question and use embeddings thereafter. Let's demonstrate this by creating a simple, easy router for movie related questions.

## Example Set-up / Movies
```python
pip install TeaRoute
API_KEY = "sk-xxx... ...xxx" # Currently, only OpenAI is supported.
myRouter = Tear(API_KEY)
```
First, we will initialize a Tear instance.
```python
buckets = {
    "Genre" : "Questions about the genre or genres of a movie (e.g. Is it a comedy? Is it a romantic comedy?",
    "Plot" : "Questions about the storyline or events in a movie (e.g. What happens in the movie? Who is the main character?)",
    "Cast And Characters" : "Questions about the actors or characters in a movie (e.g. Who stars in it? Who plays the main character?)",
    "Reviews And Opinions" : "Questions asking for subjective thoughts or critiques of a movie (e.g. Is it any good? What do critics say about it?)",
    "Details" : "Factual questions about specific details of a movie (e.g. When was it released? Who directed it? Where was it filmed?)"
}
```
Next, we will define the categories that questions can be sorted/classified/diverted to. It should be formatted as a name, which should only use letters and spaces, alongside a description. This will help the LLM learn to better classify the inputs. You can have as many as you want, but remember; this is being fed into an LLM and is thus subject to tokenization limits. If you're hitting token issues, you can always split to GPT-3.5-Turbo-0613-16k or GPT-4-0613-32k. 
```python
trainingData = [
    "What genre is The Godfather?",
    # ... 99 more questions.
]
```
We will now create our training data. It can just be a list of questions.
```python
myRouter.addBuckets(buckets) # This will add the buckets (categories) to the router as available options.
myRouter.wipe() # This is an optional step, but it will wipe any training data already written inside of the file.
myRouter.train(trainingData, 20) # This will train it. The number at the end is the batch size, which is the amount of concurrent requests at a time.
```
This will allow us to now train the router based on our added data.

Now, there's 3 ways that we can actually route requests, now that we've trained everything, etc.
- **route** - This is the simplest (and cheapest (and fastest)) way to route questions. At about 18 tokens per question, you can get around half a million requests routed per dollar (Token price: 0.0001/1k). This embeds the questions and runs it against the other embeddings that we have.
- **manual** - This version has an LLM classify it. It's potentially useful for complex requests. At about 500 tokens when combining question and instructions, you can get around 1000 requests per dollar (Token price: 0.002/1k). This is not recommended for production use in most cases.
- **routeLearn** - This version has an LLM classify it, while embedding it and adding it to the training data. It allows you to train your model and recursively improve it as users use it. Same price as *manual*.

In our case, we will choose to just use basic routing.
```python
while True:
    query = input("~ ")
    print("\n" + myRouter.route(query)["output"] + "\n")
```
And with that, we have created a fully-functional router in about 10 lines of code.

## Use Case Examples
Here are some example cases in which this will be useful. Example data will be provided. For an annotated implementation, see the Example Set-up that's below. As always, this is not an exhaustive list, and is rather just to make you think.
### Navigational Chatbot

A while ago, one of the projects I was building was a navigational chatbot. It needed to be able to identify the question to direct it to various handling systems. 
```python
buckets = {
    "general" : "General questions that don't fit any of the others.",
    "navigation" : "Questions about the navigation of a place (e.g. How do I get to 7/11? How do I get from FamilyMart to Mia C'bon?)",
    "reviews" : "Questions about the reviews of a place (e.g. How is Din Tai Fung? Is Sushiro any good?)",
    }

trainingData = [
    "How do I get to 7/11?",
    # ... 99 more questions.
    ] 
```

### Customer Support

You can also use a system like this for department-routing for customer support queries. Here's an example.
```python
buckets = {
    "it" : "Questions for the IT department (e.g. My laptop is broken.)",
    "sales" : "Questions for the sales department (e.g. How can I buy this? What do your enterprise deals look like?)",
    "cs" : "Questions for the customer support department (e.g. I need a refund, now.)",
    "escalation" : "Situations that must be escalated immediately (e.g. I'm in an emergency.)",
    }

trainingData = [
    "Do you guys do bulk discounts?",
    # ... 99 more questions.
    ] 
```

### Multi-docu-query

It can also be used as a means to control the flow of different document retrieval. For example, let's say we were building a ChatBot that was an expert on Apple's recent stock documents.
```python
buckets = {
    "Q1" : "Q1 Earnings Report for Apple's stock",
    "Q2" : "Q2 Earnings Report for Apple's stock",
    "Q3" : "Q3 Earnings Report for Apple's stock",
    "Q4" : "Q4 Earnings Report for Apple's stock",
}

trainingData = [
    "What were the key highlights of Apple's Q1 earnings report?",
    # ... 99 more questions.
]
```

