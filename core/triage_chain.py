from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

class TriageOutput(BaseModel):
    category: str = Field(description="Billing, Technical, Account, or Other")
    priority: str = Field(description="High, Medium, or Low")
    summary: str = Field(description="One-line issue summary")

output_parser = JsonOutputParser(pydantic_object=TriageOutput)

prompt = PromptTemplate(
    template="""
You are a customer support triage assistant.

Classify the customer message into:
- Category: Billing, Technical, Account, Other
- Priority: High, Medium, Low
- Summary: short and clear

Customer message:
{message}

{format_instructions}
""",
    input_variables=["message"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

llm = ChatOpenAI(
    model="microsoft/Phi-3-mini-4k-instruct",
    openai_api_base="http://vllm-server:8000/v1",
    openai_api_key="EMPTY",
    temperature=0
)

def run_triage(message: str):
    chain = prompt | llm | output_parser
    result = chain.invoke({"message": message})

    return {
        "category": result["category"],
        "priority": result["priority"],
        "summary": result["summary"],
        "confidence": 0.85,          #replace by actual probs
    }
