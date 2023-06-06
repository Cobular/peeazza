from json import dump
from json import load
import guidance
from .env import APIKEY

program = guidance("""{{#system~}}
You are helping to process but not answer student questions for an undergraduate {{classname}} class. 
You are provided with the start of the question, but there may be more that you cannot see.

Could the question be answered by an expert in {{classname}} who does not have specific knowlege about this class section? 
(i.e. without knowlege of specific homework problems, without access to student grades, without knowlege of the sylabus and without exact lecture notes)

Only respond with "Certainly", "Probably", "Unlikely", or "No". Do not answer the user question.
{{~/system}}
{{#user~}}
{{question}}
{{~/user}}
{{#assistant~}}
{{gen 'answer' max_tokens=1}}
{{~/assistant}}""", silent=True, llm=guidance.llms.OpenAI("gpt-3.5-turbo", api_key=APIKEY))

results = []


full_question = guidance(
    """{{#system~}}
You are a very smart undergraduate student taking {{classname}} and answering other student questions about the class material. 

You will be provided with the a student question.
If you can answer the question using general subject knowlege, provide a helpful and concise answer.
Do not answer if doing so would require specific information about the class, such as the answers to homework questions or knowlege about the sylabus.

If appropriate, you can include latex math in your response, delimited by two dollar signs on each side. 
{{~/system}}
{{#user~}}
{{question}}
{{~/user}}
{{#assistant~}}
{{gen 'answer' n=3}}
{{~/assistant}}""", silent=True, llm=guidance.llms.OpenAI("gpt-3.5-turbo", api_key=APIKEY)
)


def getFullText(question):
    answer = full_question(
        classname="linear algebra",
        question=question
    )
    # print(answer["answer"])
    return answer["answer"]


def getConfidence(question):
    answer = program(
        classname="linear algebra",
        question=question
    )
    # print(answer["answer"])
    resp: float
    match answer["answer"]:
        case "Certainly":
            resp = 1
        case "Probably":
            resp = 0.66
        case "Un":
            resp = 0.33
        case "No":
            resp = 0
        case other:
            resp = -1
    return resp

# print(getFullText("What is the sum of 2 and 2"))
