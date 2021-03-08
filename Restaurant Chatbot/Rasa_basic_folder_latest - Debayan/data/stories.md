## happy path_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
* goodbye
    - utter_goodbye
	- action_restart
	
## happy path_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
* form: affirm
    - utter_ask_email
* form: tells_emailid{"mail": "kirtirajchaudhary@gmail.com"}
    - slot{"mail": "kirtirajchaudhary@gmail.com"}
    - action_listen
    - slot{"mail": "kirtirajchaudhary@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
	- action_restart
	


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - action_listen
    - slot{"location": "delhi"}
    - slot{"budget": "Lesser Than Rs 300"}
    - slot{"cuisine": "chinese"}
	- form{"name": null}
* form: affirm
    - utter_ask_email
* form: tells_emailid{"mail": "kirtirajchaudhary@gmail.com"}
    - slot{"requested_slot": "mail"}
    - slot{"mail": "kirtirajchaudhary@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
	- action_restart


## Complete Path1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - action_listen
    - slot{"location": "delhi"}
    - slot{"budget": "Lesser Than Rs 300"}
    - slot{"cuisine": "chinese"}
* form: affirm
    - utter_ask_email
* form: tells_emailid{"mail": "kirtirajchaudhary@gmail.com"}
    - slot{"requested_slot": "mail"}
    - slot{"mail": "kirtirajchaudhary@gmail.com"}
    - action_send_mail
* affirm
    - utter_did_it_help
* affirm
    - utter_goodbye
    - action_restart
    

## Complete Path1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - action_listen
    - slot{"location": "delhi"}
    - slot{"budget": "Lesser Than Rs 300"}
    - slot{"cuisine": "chinese"}
* form: affirm
    - utter_ask_email
* form: tells_emailid{"mail": "kirtirajchaudhary@gmail.com"}
    - slot{"requested_slot": "mail"}
    - slot{"mail": "kirtirajchaudhary@gmail.com"}
    - action_send_mail
* affirm
    - utter_did_it_help
* deny
    - action_restart
    
    
## Complete Path3
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - action_listen
    - slot{"location": "delhi"}
    - slot{"budget": "Lesser Than Rs 300"}
    - slot{"cuisine": "chinese"}
* form: deny
    - utter_did_it_help
* affirm
    - utter_goodbye
    - action_restart
    
## Complete Path4
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - action_listen
    - slot{"location": "delhi"}
    - slot{"budget": "Lesser Than Rs 300"}
    - slot{"cuisine": "chinese"}
* form: deny
    - utter_did_it_help
* deny
    - action_restart

    
## greet path
* greet
  - utter_greet

## goodbye path
* goodbye
  - utter_goodbye
  

