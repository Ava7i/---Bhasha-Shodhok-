import requests
import json

from dis import dis
from datetime import date, datetime
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sqlalchemy import false, true
import random
from rasa.nlu.model import Interpreter

# # load the pre-trained model
interpreter = Interpreter.load("models/nlu-20230212-151559-felt-game.tar.gz")

class ActionCorrectSentence(Action):
    def name(self) -> Text:
        return "action_correct_sentence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get the latest user message
        message = tracker.latest_message["text"]

        # # pass the message to the pre-trained model
        prediction = interpreter.parse(message) 

        # # get the intent and its confidence score
        intent = prediction["intent"]["name"]
        confidence = prediction["intent"]["confidence"]

        # check if the intent is "correct_sentence" and the confidence score is high
        if intent == "correct_sentence" and confidence > 0.7:
            # the sentence is correct
            dispatcher.utter_message(text=message)
        else:
            # the sentence is incorrect
            shuffled_sentences = []

            # shuffle the input text 5 times
            for i in range(5):
                shuffled_sentence = ' '.join(random.sample(message.split(), len(message.split())))
                shuffled_sentences.append(shuffled_sentence)

            # get the shuffled sentence with the highest confidence score
            best_sentence = None
            best_confidence = 0
            for shuffled_sentence in shuffled_sentences:
                shuffled_prediction = interpreter.parse(shuffled_sentence)
                shuffled_intent = shuffled_prediction["intent"]["name"]
                shuffled_confidence = shuffled_prediction["intent"]["confidence"]
                if shuffled_confidence > best_confidence:
                    best_sentence = shuffled_sentence
                    best_confidence = shuffled_confidence

            # reply with the best sentence
            dispatcher.utter_message(text=best_sentence)
        
        return []
