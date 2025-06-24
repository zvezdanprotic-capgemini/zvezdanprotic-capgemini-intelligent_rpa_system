import os
import sys
sys.path.append("..")
from callback_logging import log_query_to_model, log_model_response

from dotenv import load_dotenv
from datetime import datetime, timedelta
import dateparser
import xml.etree.ElementTree as ET

from google.adk import Agent
import logging

from . import prompt

from typing import Optional, List, Dict

from google.adk.tools.tool_context import ToolContext

load_dotenv()
model_name = os.getenv("MODEL")

# Tools (add the tool here when instructed)

def save_data_objects_to_state(
    tool_context: ToolContext,
    data_objs: List[str]
) -> dict[str, str]:
    """Saves the list of data objects to state["data_objects"].

    Args:
        data_objs [str]: a list of str to add to the list of data objects

    Returns:
        None
    """
    # Load existing attractions from state. If none exist, start an empty list
    existing_objs = tool_context.state.get("data_objects", [])

    # Update the 'data_objects' key with a combo of old and new lists.
    # When the tool is run, ADK will create an event and make
    # corresponding updates in the session's state.
    tool_context.state["data_objects"] = existing_objs + data_objs

    # A best practice for tools is to return a status message in a return dict
    return {"status": "success"}


def get_data_object_references():
    """
    Retrieves the data object references in a given model in BPMN for loan process.

    Returns:
        A list of dicts with the details of each data object reference. For example:
        [{"process_id": "process_1",
         "process_name": "Loan Application Process",
         "data_object_id": "data_object_1",
         "name": "Name"}]
    """
    file_path = "loan_process.bpmn"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        logging.error(f"File not found: {file_path}")
        return {"status": "error - file not found"}

    try:
        # Parse the BPMN XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        data_object_references = []

        # Print data object references
        for process in root.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}process"):
            print(f"\nProcess ID: {process.get('id')}, Name: {process.get('name')}")
            for data_object in process.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}dataObjectReference"):
                print(f"  Data Object ID: {data_object.get('id')}, Name: {data_object.get('name')}")
                data_object_references.append({
                    "process_id": process.get('id'),
                    "process_name": process.get('name'),
                    "data_object_id": data_object.get('id'),
                    "name": data_object.get('name')
                })

        return {"status": "done", "data_object_references": data_object_references}

    except ET.ParseError as e:
        print(f"Error parsing BPMN file: {e}")
        return {"status": "error - parsing error"}


def get_date(x_days_from_today:int):
    """
    Retrieves a date for today or a day relative to today.

    Args:
        x_days_from_today (int): how many days from today? (use 0 for today)

    Returns:
        A dict with the date in a formal writing format. For example:
        {"date": "Wednesday, May 7, 2025"}
    """

    target_date = datetime.today() + timedelta(days=x_days_from_today)
    date_string = target_date.strftime("%A, %B %d, %Y")

    return {"date": date_string}


root_agent = Agent(
    name="function_tool_agent",
    model=model_name,
    description="Help users to identify data objects references used in BPMN files.",
    # instruction="""
    #     - Ask the user if they want to use the process model of loan applications and
    #     use their response to show the data objects required by the model.
    #     - Use your tool to save the data objects of the model to the state.
    # """,
    instruction=prompt.PROCESS_ANALYST_PROMPT,
    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,
    # Add the function tools below
    tools=[get_data_object_references, save_data_objects_to_state]#get_date, write_journal_entry]
)