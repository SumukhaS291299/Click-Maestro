import json
import multiprocessing
import os
import re
import threading
import time
import pickle

import streamlit
import pyautogui

import Scripter

from streamlit.runtime.scriptrunner import add_script_run_ctx

streamlit.title("Welcome to Low Code configurator")
streamlit.header('Tasks', divider='rainbow')


# TODO Parser code inside script and add web elements to run script


def MoveMouse():
    # Check if move mouse was called before for future processing TODO
    streamlit.session_state["MoveMouse_Active"] = True


def Scroll():
    streamlit.session_state["Scroll_Active"] = True


def MiddleClick():
    streamlit.session_state["MiddleClick_Active"] = True


def MouseLeftClick():
    streamlit.session_state["MouseLeftClick_Active"] = True


def MouseRightClick():
    streamlit.session_state["MouseRightClick_Active"] = True


def RunWorkflow():
    streamlit.session_state["RunWorkflow_Active"] = True


def initRunWorkflow():
    streamlit.session_state["initRunWorkflow_Active"] = True


def UpdateWorkflow(task, args):
    with streamlit.status("Working on data...", expanded=True) as status:
        streamlit.write("Saving current task...")
        time.sleep(2)
        task = {"Task": task, "args": args}
        try:
            with open("RootCurrentTask.pickle", "rb") as pickleLoader:
                LOADED = pickle.load(pickleLoader)
                print(LOADED)
                currentTaskList: list = LOADED.get("Tasks")
                currentTaskList.append(task)
                print("Dumping --->", currentTaskList)
                with open("RootCurrentTask.pickle", "wb") as picklewriter:
                    tempdictdump = {"Tasks": currentTaskList}
                    pickle.dump(tempdictdump, picklewriter)

        except:
            with open("RootCurrentTask.pickle", "wb") as pickleLoader:
                inittask = {}
                inittask.setdefault("Tasks", []).append(task)
                print(inittask)
                pickle.dump(inittask, pickleLoader)
        UpdateWorkflowDisplay()
        streamlit.write("Done..")


with streamlit.container():
    def UpdateWorkflowDisplay():
        with open("RootCurrentTask.pickle", "rb") as pickleLoader:
            LOADED = pickle.load(pickleLoader)
            print("Loaded and updated workflow", LOADED)
            if LOADED.get("Tasks"):
                for stepNo, task in enumerate(LOADED.get("Tasks")):
                    with streamlit.container(border=True):
                        streamlit.write("✒ " + str(stepNo) + "::  Task: ", task["Task"])
                        streamlit.write(task)

            else:
                with streamlit.status("No workflow yet...", expanded=True) as status:
                    status.write("Workflow will be created automatically when you start a new task...")

TC1, TC2, TC3 = streamlit.columns(3)

streamlit.header('', divider='rainbow')

WC1, WC2, WC3 = streamlit.columns(3)

# Check if workflow already exists
dirFiles = os.listdir()

with WC1:
    if streamlit.button("Run Workflow", on_click=initRunWorkflow) or streamlit.session_state.get(
            "initRunWorkflow_Active"):
        compiler = re.compile(r"WORKFLOW_(.*).json")
        workflows_available = []
        for dirs in dirFiles:
            try:
                find = compiler.match(dirs)
                workflows_available.append(find.group(1))
            except:
                pass
        WorkflowToRun = streamlit.selectbox("Select Workflow to run", workflows_available)
        if streamlit.button("RUN", on_click=RunWorkflow) or streamlit.session_state.get("RunWorkflow_Active"):
            print("Running.....")
            streamlit.toast("Waiting 20s to do all pre-requisites")
            time.sleep(16)
            streamlit.toast("Starting in: 4s")
            time.sleep(1)
            streamlit.toast("Starting in: 3s")
            time.sleep(1)
            streamlit.toast("Starting in: 2s")
            time.sleep(1)
            streamlit.toast("Starting in: 1s")
            time.sleep(1)
            with open("WORKFLOW_" + WorkflowToRun + ".json") as SelectedWF:
                dictForScript = json.load(SelectedWF)
                print("Starting Workflow....")
                print(dictForScript)
                Scripter.RunScript.RunOnce(dictForScript)
            streamlit.session_state["RunWorkflow_Active"] = False
            streamlit.session_state["initRunWorkflow_Active"] = False

streamlit.header('Options', divider='rainbow')

WorkflowName = streamlit.text_input(label="Please give a unique name for your workflow", max_chars=20)

if streamlit.button("Check Workflow") and "WORKFLOW_" + WorkflowName + ".json" in dirFiles:
    with streamlit.status("Looks like a workflow with same name already exits.....") as loadingFile:
        loadingFile.write("Working on data....")
        with open("WORKFLOW_" + WorkflowName + ".json", "r") as f:
            workflowfromfile = json.load(f)
            # getTaskListFromFile = workflowfromfile.get("Tasks")
            with open("RootCurrentTask.pickle", "wb") as pickleLoader:
                pickle.dump(workflowfromfile, pickleLoader)
                print(workflowfromfile)
            streamlit.toast(f"Loaded Your {WorkflowName} data")

with TC1:
    # Move Mouse....
    if streamlit.button("Move Mouse", on_click=MoveMouse) or streamlit.session_state.get("MoveMouse_Active"):
        X = streamlit.number_input(label="Insert the X position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().width))
        Y = streamlit.number_input(label="Insert the Y position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().height))
        Duration = streamlit.number_input(label="Duration for movement", value=0.0, min_value=0.0)
        LogSS = streamlit.selectbox(label="Enable Screenshot log", options=[True, False])
        if streamlit.button("Save update", on_click=UpdateWorkflow,
                            kwargs={"args": {"X": X, "Y": Y, "Duration": Duration, "LogSS": LogSS},
                                    "task": "move_mouse"}):
            streamlit.session_state["MoveMouse_Active"] = False

    if streamlit.button("Scroll", on_click=Scroll) or streamlit.session_state.get("Scroll_Active"):
        X = streamlit.number_input(label="Insert the X position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().width))
        Y = streamlit.number_input(label="Insert the Y position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().height))
        Clicks = streamlit.number_input(label="The number of scroll, and defaults to 1", value=1, min_value=1)
        LogSS = streamlit.selectbox(label="Enable Screenshot log", options=[True, False])
        if streamlit.button("Save update", on_click=UpdateWorkflow,
                            kwargs={
                                "args": {"X": X, "Y": Y, "Clicks": Clicks, "LogSS": LogSS},
                                "task": "Scroll"}):
            streamlit.session_state["Scroll_Active"] = False

with TC2:
    # Left Click
    if streamlit.button("Mouse Left Click", on_click=MouseLeftClick) or streamlit.session_state.get(
            "MouseLeftClick_Active"):
        X = streamlit.number_input(label="Insert the X position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().width))
        Y = streamlit.number_input(label="Insert the Y position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().height))
        Clicks = streamlit.number_input(label="how many clicks to make, and defaults to 1", value=1, min_value=1)
        Interval = streamlit.number_input(label="how many seconds to wait in between each click", value=0.0,
                                          min_value=0.0)
        Duration = streamlit.number_input(label="Duration for movement", value=0.0, min_value=0.0)
        LogSS = streamlit.selectbox(label="Enable Screenshot log", options=[True, False])
        if streamlit.button("Save update", on_click=UpdateWorkflow,
                            kwargs={
                                "args": {"X": X, "Y": Y, "Clicks": Clicks, "Interval": Interval, "Duration": Duration,
                                         "LogSS": LogSS},
                                "task": "left_click"}):
            streamlit.session_state["MouseLeftClick_Active"] = False

    if streamlit.button("Middle Mouse Click", on_click=MiddleClick) or streamlit.session_state.get(
            "MiddleClick_Active"):
        X = streamlit.number_input(label="Insert the X position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().width))
        Y = streamlit.number_input(label="Insert the Y position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().height))
        Interval = streamlit.number_input(label="how many seconds to wait in between each click", value=0.0,
                                          min_value=0.0)
        Duration = streamlit.number_input(label="Duration for movement", value=0.0, min_value=0.0)
        Clicks = streamlit.number_input(label="how many middle clicks to make, and defaults to 1", value=1, min_value=1)
        LogSS = streamlit.selectbox(label="Enable Screenshot log", options=[True, False])
        if streamlit.button("Save update", on_click=UpdateWorkflow,
                            kwargs={
                                "args": {"X": X, "Y": Y, "Clicks": Clicks, "Interval": Interval, "Duration": Duration,
                                         "LogSS": LogSS},
                                "task": "middle_click"}):
            streamlit.session_state["MiddleClick_Active"] = False

with TC3:
    # Right Click
    if streamlit.button("Mouse Right Click", on_click=MouseRightClick) or streamlit.session_state.get(
            "MouseRightClick_Active"):
        X = streamlit.number_input(label="Insert the X position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().width))
        Y = streamlit.number_input(label="Insert the Y position", value=0, min_value=0,
                                   max_value=int(pyautogui.size().height))
        Clicks = streamlit.number_input(label="how many clicks to make, and defaults to 1", value=1, min_value=1)
        Interval = streamlit.number_input(label="how many seconds to wait in between each click", value=0.0,
                                          min_value=0.0)
        Duration = streamlit.number_input(label="Duration for movement", value=0.0, min_value=0.0)
        LogSS = streamlit.selectbox(label="Enable Screenshot log", options=[True, False])
        if streamlit.button("Save update", on_click=UpdateWorkflow,
                            kwargs={
                                "args": {"X": X, "Y": Y, "Clicks": Clicks, "Interval": Interval, "Duration": Duration,
                                         "LogSS": LogSS},
                                "task": "right_click"}):
            streamlit.session_state["MouseRightClick_Active"] = False

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
            with open("RootCurrentTask.pickle", "rb") as pickleLoader:
                LOADER = pickle.load(pickleLoader)
                print(LOADER)
            json.dump({"Tasks": LOADER.get("Tasks")}, f)


with Optcol2:
    if streamlit.button("Save Workflow", on_click=ValidateWorkFlowName):
        streamlit.toast("WorkFlow saving...")

streamlit.header('Workflow Status', divider='rainbow')

try:
    with open("RootCurrentTask.pickle", "rb") as pickleLoader:
        streamlit.write(pickle.load(pickleLoader))
except Exception as e:
    print(e)
