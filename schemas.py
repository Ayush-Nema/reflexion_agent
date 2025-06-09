from typing import List

from pydantic import BaseModel, Field


class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing")
    superfluous: str = Field(description="Critique of what is superfluous")  # superfluous ≡ redundant/ not needed


class AnswerQuestion(BaseModel):
    """Answer the question."""

    answer: str = Field(description="~250 word detailed answer to the question.")
    reflection: Reflection = Field(description="Your reflection on the initial answer.")
    search_queries: List[str] = Field(
        description="1-3 search queries for researching improvements to address the critique of your current answer."
    )


class ReviseAnswer(AnswerQuestion):
    """Revise your answer as per original question"""
    references: List[str] = Field(description="Citation from your updated answer")
