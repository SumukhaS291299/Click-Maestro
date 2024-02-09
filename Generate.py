import json
import os
import time

import streamlit
import pyautogui

streamlit.title("Welcome to Low Code configurator")
streamlit.header('Tasks', divider='rainbow')

# TODO Remove Streamlit session state for task and create a pickle file for same :0


def MoveMouse():
    streamlit.session_state["Active"] = True
    try:
        prevCalled = streamlit.session_state.get("Called")
        streamlit.session_state["Called"] = (prevCalled + 1)
    except:
        pass
    streamlit.session_state.setdefault("Called", 1)


def UpdateWorkflow(args):
    with streamlit.status("Working on data...", expanded=True) as status:
        streamlit.write("Saving current task...")
        time.sleep(2)
        task = {"Task": "move_mouse", "args": args}
        try:
            currentTaskList: list = streamlit.session_state.get("Tasks")
            currentTaskList.append(task)
        except:
            streamlit.session_state.setdefault("Tasks", []).append(task)
        UpdateWorkflowDisplay()
        streamlit.write("Done..")


with streamlit.container():
    def UpdateWorkflowDisplay():
        if streamlit.session_state.get("Tasks"):
            for stepNo, task in enumerate(streamlit.session_state.get("Tasks")):
                with streamlit.container(border=True):
                    streamlit.write("✒ " + str(stepNo) + "::  Task: ", task["Task"])
                    streamlit.write(task)

        else:
            with streamlit.status("No workflow yet...", expanded=True) as status:
                status.write("Workflow will be created automatically when you start a new task...")

TC1, TC2, TC3 = streamlit.columns(3)

streamlit.header('', divider='rainbow')
streamlit.header('Options', divider='rainbow')

WorkflowName = streamlit.text_input(label="Please give a unique name for your workflow", max_chars=20)

# Check if workflow already exists
dirFiles = os.listdir()

if "WORKFLOW_" + WorkflowName + ".json" in dirFiles:
    with streamlit.status("Looks like a workflow with same name already exits.....") as loadingFile:
        loadingFile.write("Working on data....")
        with open("WORKFLOW_" + WorkflowName + ".json", "r") as f:
            workflowfromfile = json.load(f)
            getTaskListFromFile = workflowfromfile.get("Tasks")
            streamlit.session_state["Tasks"] = getTaskListFromFile
            streamlit.toast(f"Loaded Your {WorkflowName} data")

with TC1:
    if streamlit.button("Move Mouse", on_click=MoveMouse) or streamlit.session_state.get("Active"):
        X = streamlit.number_input(label="Insert the X position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().width))
        Y = streamlit.number_input(label="Insert the Y position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().height))
        Duration = streamlit.number_input(label="Duration for movement", value=0.0, min_value=0.0)
        LogSS = streamlit.selectbox(label="Enable Screenshot log", options=[True, False])
        if streamlit.button("Save update", on_click=UpdateWorkflow,
                            kwargs={"args": {"X": X, "Y": Y, "Duration": Duration, "LogSS": LogSS}}):
            streamlit.session_state["Active"] = False

Optcol1, Optcol2, Optcol3 = streamlit.columns(3)

with Optcol1:
    if streamlit.button("Show Steps"):
        UpdateWorkflowDisplay()


def ValidateWorkFlowName():
    print("WorkflowName:", WorkflowName)
    if WorkflowName.strip().replace("\n", "") == "":
        streamlit.toast("WorkFlow name cannot be empty...")
    else:
        with open("WORKFLOW_" + WorkflowName + ".json", "w") as f:
            json.dump({"Tasks": streamlit.session_state.get("Tasks")}, f)


with Optcol2:
    if streamlit.button("Save Workflow", on_click=ValidateWorkFlowName):
        streamlit.toast("WorkFlow saving...")
