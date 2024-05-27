# ==============================================================================
# File: actions.py
# Project Name: ForestBot
# Version: 1
# Copyright: Copyright 2024 by Omar Mussa
# License: MIT License
# 
# Description: This file contains the custom actions for ForestBot, part of the ForestQB project.
# These actions are designed to process user inputs and push back JSON outputs that include the intent
# and its associated entities. ForestQB, in turn, processes these outputs to determine the appropriate
# actions and reflects these actions on the GUI. This integration enhances the dynamic interaction capabilities
# of ForestBot, facilitating effective user engagement and efficient data management.
# 
# Disclaimer: This software is provided "as is" without warranty of any kind, either express or implied,
# including but not limited to the implied warranties of merchantability, fitness for a particular purpose,
# or non-infringement. The developers of ForestBot do not guarantee the software's performance and is not
# liable for any issues that arise from its use.
# ==============================================================================


import json

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionMainHandler(Action):

    def name(self) -> Text:
        return "action_main_handler"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(json.dumps(tracker.latest_message, indent=4, sort_keys=True))

        json_msg = {
            "latest_message": tracker.latest_message,
        }

        dispatcher.utter_message(json_message = json_msg)

        return []

#  python3 actions/actions.py     