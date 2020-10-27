from rasa_sdk import Action
from typing import Any, Dict, List, Text, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
import secrets
import requests


class ActionTellBuy(Action):
    def __init__(self):
        # self.faq_data={}
        # self.js=json.load(open('data/answer.txt','r',encoding='utf-8'))
        # with open('data/nlu.md','r',encoding='utf-8',newline='') as f:
        # line=f.readline()
        # while line:
        # if line.find('## intent: ')>=0:
        # line1=f.readline()
        # if line1:
        # if line1.find('- ')>=0:
        # self.faq_data[line[11:-1]]=line1[2:-1]
        # line=f.readline()
        print("init buy")

    def name(self) -> Text:
        return "action_ask_buy_what"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buy_item = tracker.get_slot("buy_item")

        # dispatcher.utter_message(text=user_sex)
        if buy_item:
            dispatcher.utter_message(text='那推荐你这款' + str(buy_item))
        else:
            dispatcher.utter_message(text='获取物品失败，请重新尝试')
        return []
