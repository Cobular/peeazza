from json import dump
from json import load
import creds
import guidance

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
{{~/assistant}}""", silent=True, llm=guidance.llms.OpenAI("gpt-3.5-turbo", api_key=creds.apikey))

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
{{~/assistant}}""", silent=True, llm=guidance.llms.OpenAI("gpt-3.5-turbo", api_key="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")
)

questions = [
    "<p>After calculating eigenvectors, it is tempting to multiply by constants to eliminate any fractions, which will make subsequent calculations simpler. See the following eigenbasis:</p>\n<p>$$\\begin{bmatrix} \\frac{1}{3} & \\frac{1}{8} \\\\ 1 & 2 \\end{bmatrix} \\rightarrow \\begin{bmatrix} 1 & 1 \\\\ 3 & 16\\end{bmatrix}$$</p>\n<p>I don&#39;t see why this would not be okay as eigenvectors are spans, but some of the example in the book are very reluctant to do so. So, is this allowed?\u00a0</p>",
    "<p>Directed to Dr. Gannon:</p>\n<p></p>\n<p>For question 3 and 4, I was wondering if by &#34;For what values&#34; you mean all values or just some set of 3 values that work to satisfy what is being asked. I would assume it would mean for all values (because the other way would be very easy to answer), but then you go on to say &#34;This problem will be graded on a correct/incorrect basis only\u2013there is no need to show work&#34; which makes me think you want just some set of 3 values (I feel like you would want some algebra work being shown to answer the &#34;all values&#34; interpretation of this question).</p>",
    "I am a bit confused about nullity and geometric multiplicity and their relation to matrices. For example in Question 4A, is it correct that if the eigenbasis for a matrix has 3 vectors (to make a 3x3 matrix diagonalizable), then the geometric multiplicity has to be 3, meaning that the nullity of A-lambda(I) has to also equal 3? Thanks in advance!",
    "Im doing question 4a. A matrix that is 3x3 and all zeroes is considered to have a nullity of 3 right?",
    "<p>If we use the formula S^-1AS = D and we have calculated the eigenvectors to be</p>\n<p>$$\\begin{bmatrix} 1\\\\3 \\end{bmatrix}$$ and $$\\begin{bmatrix} 1\\\\2\\end{bmatrix}$$</p>\n<p>can we come to the correct diagonal matrix (D) using S as either\u00a0</p>\n<p>$$\\begin{bmatrix} 1&1\\\\3&2 \\end{bmatrix}$$ or $$\\begin{bmatrix} 1&1\\\\2&3\\end{bmatrix}$$?</p>",
]


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