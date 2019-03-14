
## TEST COMMIT SS

## Generated Story 2493107679611460366
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - verify_location
    - slot{"location": "amritsar"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "amritsar"}
    - slot{"restaurant_exist": true}
    - utter_ask_emailid
* restaurant_search{"emailid": "aryansinghjaswal@gmail.com"}
    - slot{"emailid": "aryansinghjaswal@gmail.com"}
    - action_send_email
    - export

## Generated Story 964254582591831276
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
* affirm{"location": "thanks"}
    - slot{"location": "thanks"}
    - utter_goodbye
    - export

## Generated Story 5083914778265065896 (SS)
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - verify_location
    - slot{"location": "allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "allahabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"emailid": "srikanth.vs84@gmail.com"}
    - slot{"emailid": "srikanth.vs84@gmail.com"}
    - action_send_email
    - export

## Generated Story -734929165878046893 (SS)
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - export

## Generated Story -2497440363954761105 (SS)
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - verify_location
    - slot{"location": "Kochi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Kochi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "srikanth.vs84@gmail.com"}
    - slot{"emailid": "srikanth.vs84@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - export

## Generated Story -531731183292093066 (SS)
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "majuli"}
    - slot{"location": "majuli"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "madrid"}
    - slot{"location": "madrid"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - verify_location
    - slot{"location": "vijayawada"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "vijayawada"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
    - export

