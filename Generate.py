import time

import streamlit
import pyautogui

streamlit.title("Welcome to Low Code configurator")

Steps = []

with streamlit.container():
    def UpdateWorkflowDisplay():
        if streamlit.session_state.get("Tasks"):
            for task in streamlit.session_state.get("Tasks"):
                streamlit.write(task)

if streamlit.button("Show Steps"):
    UpdateWorkflowDisplay()


def MoveMouse():
    streamlit.session_state["Active"] = True
    try:
        prevCalled = streamlit.session_state.get("Called")
        streamlit.session_state["Called"] = (prevCalled + 1)
    except:
        pass
    streamlit.session_state.setdefault("Called", 1)


def UpdateWorkflow(X, Y, Duration, LogSS):
    with streamlit.status("Working on data...", expanded=True) as status:
        streamlit.write("Saving current task...")
        time.sleep(2)
        task = {"Task": "move_mouse", "args": {"X": X, "Y": Y, "Duration": Duration, "LogScreenshot": LogSS}}
        try:
            currentTaskList: list = streamlit.session_state.get("Tasks")
            currentTaskList.append(task)
        except:
            streamlit.session_state.setdefault("Tasks", []).append(task)
        UpdateWorkflowDisplay()
        streamlit.write("Done..")


if streamlit.button("Move Mouse", on_click=MoveMouse) or streamlit.session_state.get("Active"):
    X = streamlit.number_input(label="Insert the X position", value=0, min_value=0,
                               max_value=int(pyautogui.size().width))
    Y = streamlit.number_input(label="Insert the Y position", value=0, min_value=0,
                               max_value=int(pyautogui.size().height))
    Duration = streamlit.number_input(label="Duration for movement", value=0.0, min_value=0.0)
    LogSS = streamlit.selectbox(label="Enable Screenshot log", options=[True, False])
    if streamlit.button("Save update", on_click=UpdateWorkflow,
                        kwargs={"X": X, "Y": Y, "Duration": Duration, "LogSS": LogSS}):
        streamlit.session_state["Active"] = False
