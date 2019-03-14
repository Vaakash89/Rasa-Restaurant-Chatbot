from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
# Import the email modules we'll need
from email.message import EmailMessage
import zomatopy
import json
import requests
# Import smtplib for the email sending function
import smtplib
from concurrent.futures import ThreadPoolExecutor
d_email_rest = []

class ActionSearchRestaurants(Action):

    config = {"user_key": "75502752c8a4b706194ec22543a11dc1"}

    def name(self):
        return 'action_restaurant'

    def run(self, dispatcher, tracker, domain):
        zomato = zomatopy.initialize_app(self.config)
        # Get location from slot
        loc = tracker.get_slot('location')

        # Get cuisine from slot
        cuisine = tracker.get_slot('cuisine')
        cost_min = tracker.get_slot('budgetmin')
        cost_max = tracker.get_slot('budgetmax')
        results, lat, lon = self.get_location_suggestions(loc,zomato)

        if (results == 0):
            # Zomato API could not find suggestions for this location.
            restaurant_exist = False
            dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
        else:
            d_rest = self.get_restaurants(lat, lon, cost_min, cost_max, cuisine)

            # Filter the results based on budget
            d_budget = [d_rest_single for d_rest_single in d_rest if ((d_rest_single['restaurant']['average_cost_for_two'] > cost_min) & (
                d_rest_single['restaurant']['average_cost_for_two'] < cost_max))]
            # Sort the results according to the restaurant's rating
            d_budget_rating_sorted = sorted(
                d_budget, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

            # Build the response
            response = ""
            restaurant_exist = False
            if len(d_budget_rating_sorted) == 0:
                dispatcher.utter_message("Sorry, no results found :("+ "\n")
            else:
                # Pick the top 5
                d_budget_rating_top5 = d_budget_rating_sorted[:5]
                global d_email_rest
                d_email_rest = d_budget_rating_sorted[:10]
                if(d_email_rest and len(d_email_rest) > 0):
                    restaurant_exist = True
                for restaurant in d_budget_rating_top5:
                    response = response + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + \
                        " has been rated " + \
                        restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
                dispatcher.utter_message("Here are our picks!"+ "\n" + response)
        return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]

    def get_location_suggestions(self, loc, zomato):
        # Get location details including latitude and longitude
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = 0
        lon = 0
        results = len(d1["location_suggestions"])
        if (results > 0):
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
        return results, lat, lon

    def get_restaurants(self, lat, lon, budgetmin, budgetmax , cuisine):
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        d_rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
        executor.shutdown()
        return d_rest
    
class VerifyLocation(Action):

    TIER_1 = []
    TIER_2 = []

    def __init__(self):
        self.TIER_1 = ['ahmedabad', 'bangalore', 'chennai',
                       'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.TIER_2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi',
                       'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']
    def name(self):
        return "verify_location"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if not (self.verify_location(loc)):
            dispatcher.utter_message(
                "We do not operate in " + loc + " yet. Please try some other city.")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        else:
            return [SlotSet('location', loc), SlotSet("location_ok", True)]

    def verify_location(self, loc):
        return loc.lower() in self.TIER_1 or loc.lower() in self.TIER_2
        
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global d_email_rest
        email_rest_count = len(d_email_rest)
        # Construct the email 'subject' and the contents.
        d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
        for restaurant in d_email_rest:
            d_email_msg = d_email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" +"\n"

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("asaupgrad.chatbot@gmail.com", "pgdmlaiupgrad")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "asaupgrad.chatbot@gmail.com"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
        return []


class VerifyBudget(Action):

    def name(self):
        return "verify_budget"

    def run(self, dispatcher, tracker, domain):
        budgetmin = None
        budgetmax = None
        error_msg = "Sorry!! price range not supported, please re-enter."
        try:
            budgetmin = int(tracker.get_slot('budgetmin'))
            budgetmax = int(tracker.get_slot('budgetmax'))
        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', None), SlotSet('budgetmax', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if budgetmin in min_dict and (budgetmax in max_dict or budgetmax > 700):
            return [SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 10000), SlotSet('budget_ok', False)]

class VerifyCuisine(Action):

    def name(self):
        return "verify_cuisine"

    def run(self, dispatcher, tracker, domain):
        cuisines = ['chinese','mexican','italian','american','south indian','north indian']
        error_msg = "Sorry!! The cuisine is not supported. Please re-enter."
        cuisine = tracker.get_slot('cuisine')
        try:
            cuisine = cuisine.lower()
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]
        if cuisine in cuisines:
            return [SlotSet('cuisine', cuisine), SlotSet('cuisine_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]

def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': '5787bb8301dd97fbe86ec40febf7e03b'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])
