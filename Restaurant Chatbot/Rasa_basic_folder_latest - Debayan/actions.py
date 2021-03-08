# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from typing import Dict, Text, Any, List
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import re
import smtplib

cuisines_dict = {'american': 1, 'chinese': 25, 'mexican': 73,'italian': 55, 'north indian': 50, 'south indian': 85}
sort_by_rating = []
gmail_user = 'kirtirajchaudhary@gmail.com'
gmail_password = ''

sent_from = gmail_user
subject = 'Restaurant details!!'


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "82620001ca282d1716dab0d934fb3051"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location').lower()
        cuisine = tracker.get_slot('cuisine').lower()
        budget = tracker.get_slot('budget')
        location_detail = zomato.get_location(loc, 1)
        print(type(loc))
        print(loc)
        print(cuisine)
        print(location_detail)
        global sort_by_rating
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        if (budget == str("Lesser than Rs 300")):
            results = zomato.restaurant_search(
                "", lat, lon, str(cuisines_dict.get(cuisine)), 20, 0)
        elif (budget == str("Rs 300 to Rs 700")):
            results = zomato.restaurant_search(
                "", lat, lon, str(cuisines_dict.get(cuisine)), 20, 11)
        elif (budget == str("More than Rs 700")):
            results = zomato.restaurant_search("", lat, lon, str(
                cuisines_dict.get(cuisine)), 20, 0, 16, str("cost"), str("desc"))
        d = json.loads(results)
        restDict = {}
        response = ""
        if d['results_found'] == 0:
            response = "no results"
        else:
            for p in d['restaurants']:
                restDict[p['restaurant']['id']] = [p['restaurant']['average_cost_for_two'], p['restaurant']['name'], float(
                    p['restaurant']['user_rating']['aggregate_rating']), p['restaurant']['location']['address']]

            sort_by_rating = sorted(
                restDict.items(), key=lambda e: e[1][2], reverse=True)
            for data in sort_by_rating[:5]:
                response = response + data[1][1] + " in " + data[1][3] + " has been rated " + str(
                    data[1][2]) + " with cost of " + str(data[1][0]) + "\n"

        dispatcher.utter_message("-----"+response + "\n\n")
        dispatcher.utter_template("utter_ask_ifemailrequired", tracker)
        return [SlotSet('location', loc)]


class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        global sort_by_rating
        dispatcher.utter_template("utter_mail", tracker)
        sent_to = []
        sent_to.append(str(tracker.get_slot('mail')))
        print("address to sent=",sent_to)
        response = ""
        for data in sort_by_rating[:10]:
            response = response + data[1][1] + " in " + data[1][3] + "has been rated" + str(data[1][2]) + " with cost of " + str(data[1][0]) + "\n"
        email_text = """\
        From: %s
        To: %s
        Subject: %s
        
        %s
        """ % (sent_from, ", ".join(sent_to), subject, response)
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.set_debuglevel(1)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()
        dispatcher.utter_message("Details has been sent to your mail ID.Thank You!!")
        return []
        
        
        
class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["location", "cuisine", "budget"]

    def check_for_city(self):
        file = open('all_cities.txt', mode='r', encoding="utf8")
        city_list = file.read()
        city_list = re.sub(r"[\n\t\s]*", "", city_list)
        return (city_list.lower().split(','))

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do after all required slots are filled"""
        dispatcher.utter_template("utter_slots_values", tracker)
        return []

    def validate_location(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate cuisine value."""
        if value.lower() in self.check_for_city():
            print("called")
            return {"location": value}
        else:
            print("not called")
            dispatcher.utter_template("utter_noservice", tracker)
            return {"location": None}

