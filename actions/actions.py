# Documentation : https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class action_operation(Action):

	def name(self) -> Text:
		return "action_calculate"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


		first_number = float(tracker.get_slot("first_number"))
		second_number = float(tracker.get_slot("second_number"))
		operation = tracker.get_slot("operation")

		result = 0
		reply = "I am not quite sure what that means?"
		if operation == 'add':
			result = first_number + second_number
			reply = f"{str(first_number)} +  {str(second_number)} = {str(result)}"
		elif operation == 'subtract':
			result = first_number - second_number
			reply = f"{str(first_number)} -  {str(second_number)} = {str(result)}"
		elif operation == 'multiply':
			result = first_number * second_number
			reply = f"{str(first_number)} *  {str(second_number)} = {str(result)}"
		elif operation == 'divide':
			if second_number:
				result = first_number / second_number
				reply = f"{str(first_number)} /  {str(second_number)} = {str(result)}"
			else:
				reply = "Cannot divide by 0"

		dispatcher.utter_message(text=reply)

		return [SlotSet("result", result)]