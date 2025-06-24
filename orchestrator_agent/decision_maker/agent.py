import os
import sys
sys.path.append("..")
from callback_logging import log_query_to_model, log_model_response
from dotenv import load_dotenv
from google.adk import Agent

from google.genai import types
from typing import Optional, List, Dict

from google.adk.tools.tool_context import ToolContext

load_dotenv()
model_name = os.getenv("MODEL")

# Tools (add the tool here when instructed)
def run_decision_maker(
    tool_context: ToolContext
) -> Dict[str, str]:
    """
    Make a decision regarding a loan application.
    This tool evaluates the loan application based on the provided parameters. 

    Args:
        context (ToolContext): The tool context.

    Returns:
        Dict[str, str]: A dictionary with the decision details.
    """
    # Load existing parameters from the tool context
    #params = tool_context.state.get("attractions", []) 
    age = tool_context.state.get("age", 0)
    amount = tool_context.state.get("amount", 0.0)
    salary = tool_context.state.get("salary", 0.0)
    installments = tool_context.state.get("installments", 1)
    lenght = tool_context.state.get("lenght", 0)
    

    # Here you can implement the logic to process the decision
    if salary/installments <= 2 or lenght+age > 70:
        decision = "rejected"
        reason = "Insufficient salary or too long loan period."
        amount = 0.0
    elif salary/installments > 2 and lenght+age <= 70:
        decision = "approved"
        reason = "Loan application approved."
        amount = amount if amount is not None else 0.0

    return {
        "decision": decision,
        "reason": reason or "",
        "amount": amount if amount is not None else 0.0
    }


# Agents

decision_maker = Agent(
    name="decision_maker",
    model=model_name,
    description="Make a decision regarding a loan application.",
    instruction="""
        - Use your tool to determine if the loan application is approved or rejected.
        - Provide a reason for the decision.
        - If the application is approved, provide the amount of the loan.
        - If the application is rejected, provide a reason for the rejection.
        - If the application is approved, provide a list of conditions that must be met.
        - If the application is rejected, provide a list of conditions that must be met for approval.
        """,
    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,
    # When instructed to do so, paste the tools parameter below this line
    tools=[run_decision_maker]

    )

root_agent = Agent(
    name="steering",
    model=model_name,
    description="Start a decision making process.",
    instruction="""
        Ask the user if they need help deciding if the loan application is approved or rejected.
        If they need help deciding, send them to 'decision_maker'.
        """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
    sub_agents=[decision_maker]

)

