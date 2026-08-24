from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

from app.rag import retrieve_context


class AgentState(TypedDict):
    question: str
    context: str
    answer: str


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def retrieval_node(state: AgentState):

    context = retrieve_context(
        state["question"]
    )

    return {
        **state,
        "context": context
    }


def generation_node(state: AgentState):

    prompt = f"""
You are an enterprise AI assistant.

Use only the context provided below when possible.

Context:
{state['context']}

Question:
{state['question']}

Provide a concise and grounded answer.
"""

    response = llm.invoke(prompt)

    return {
        **state,
        "answer": response.content
    }


workflow = StateGraph(AgentState)

workflow.add_node(
    "retrieve",
    retrieval_node
)

workflow.add_node(
    "generate",
    generation_node
)

workflow.set_entry_point("retrieve")

workflow.add_edge(
    "retrieve",
    "generate"
)

workflow.add_edge(
    "generate",
    END
)

agent = workflow.compile()
