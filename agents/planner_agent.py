from agents.code_agent import code_agent
from agents.data_agent import data_agent
from agents.file_agent import file_agent
from agents.general_agent import general_agent

def planner_agent(user_input, file_content=None):

    text = user_input.lower()

    if file_content:
        return file_agent(user_input, file_content)

    elif "code" in text or "error" in text or "bug" in text:
        return code_agent(user_input)

    elif "data" in text or "csv" in text:
        return data_agent(user_input)

    else:
        return general_agent(user_input)