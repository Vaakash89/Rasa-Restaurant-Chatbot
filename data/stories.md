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
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story 4708982396586626192
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
    - action_restart

## Generated Story -4665169466705197949
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "aryancodify@gmail.com"}
    - slot{"emailid": "aryancodify@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -5043122488344133708
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
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
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 618260811243109624
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
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
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 1718058272252383512
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
    - verify_location
    - slot{"location": "allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "1000"}
    - slot{"budgetmax": "1000"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 1000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "allahabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "aryancodify@gmail.com"}
    - slot{"emailid": "aryancodify@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

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
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "srikanth.vs84@gmail.com"}
    - slot{"emailid": "srikanth.vs84@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

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
	- action_restart

## Generated Story 306586164453885916
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - verify_location
    - slot{"location": "coimbatore"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "coimbatore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "aryancodify@gmail.com"}
    - slot{"emailid": "aryancodify@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

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
	- action_restart

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
* deny
    - utter_goodbye
	- action_restart

## Generated Story -6868886679115127069
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "chennai", "budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chennai"}
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart
	
## Generated Story 475841212046557654
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "lanka"}
    - slot{"location": "lanka"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "oman"}
    - slot{"location": "oman"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "dubai"}
    - slot{"location": "dubai"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - verify_location
    - slot{"location": "lucknow"}
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
    - slot{"location": "lucknow"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart
	
## Generated Story 6145797985903623523
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - verify_location
    - slot{"location": "jaipur"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "jaipur"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
	- action_restart
	
## Generated Story -5687567762096400471
* greet
    - utter_greet
* restaurant_search{"location": "raipur", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"location": "raipur"}
    - verify_location
    - slot{"location": "raipur"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "raipur"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -6479006044568222703
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -2118681346680373904
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "mumbai"}
    - slot{"restaurant_exist": false}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
	- action_restart

## Generated Story 318010925000507245
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
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
    - slot{"location": "mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
	- action_restart

## Generated Story 9173743736444141906
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "500"}
    - slot{"budgetmax": "500"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
	- action_restart

## Generated Story -4894982680816150664
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "delhi", "budgetmin": "300", "budgetmax": "800"}
    - slot{"budgetmax": "800"}
    - slot{"budgetmin": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 800}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "euphoric.aakash@gmail.com"}
    - slot{"emailid": "euphoric.aakash@gmail.com"}
    - action_send_email
	- action_restart

## Generated Story -8039304074282048580
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - verify_location
    - slot{"location": "ajmer"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "ajmer"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
	- action_restart

## Generated Story -1506266381209530864
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "ajmer", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "ajmer"}
    - verify_location
    - slot{"location": "ajmer"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "ajmer"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
	- action_restart
    
## Generated Story 7250327259440289631
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "aryancodify@gmail.com"}
    - slot{"emailid": "aryancodify@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story 6590940324926527851
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
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
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "aryancodify@gmail.com"}
    - slot{"emailid": "aryancodify@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story 3200734634823395562
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "pathankot"}
    - slot{"location": "pathankot"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "itanagar"}
    - slot{"location": "itanagar"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - verify_location
    - slot{"location": "ranchi"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "ranchi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"emailid": "aryansinghjaswal@gmail.com"}
    - slot{"emailid": "aryansinghjaswal@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -3119872537346433768
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "dehradun"}
    - slot{"location": "dehradun"}
    - verify_location
    - slot{"location": "dehradun"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "dehradun"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"emailid": "aryansinghjaswal@gmail.com"}
    - slot{"emailid": "aryansinghjaswal@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -2747416429319312118
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "asansol"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "asansol"}
    - verify_location
    - slot{"location": "asansol"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "moroccan"}
    - slot{"cuisine": "moroccan"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "500"}
    - slot{"budgetmax": "500"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}    
    - action_restaurant
    - slot{"location": "asansol"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 5693031377652531498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bhubhaneshwar"}
    - slot{"location": "bhubhaneshwar"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "amravati"}
    - slot{"location": "amravati"}
    - verify_location
    - slot{"location": "amravati"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "amravati"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "aryansinghjaswal@gmail.com"}
    - slot{"emailid": "aryansinghjaswal@gmail.com"}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	
## Generated Story 8437935424406063230
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## Generated Story -5399400691021449854
* 
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* 
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
    - verify_location
    - slot{"location": "warangal"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "warangal"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 5176427587494693005
* greet
    - utter_greet
* restaurant_search{"location": "colombo"}
    - slot{"location": "colombo"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "vegas"}
    - slot{"location": "vegas"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story -4988396269851949806
* greet
    - utter_greet
* restaurant_search{"location": "Hubli-Dharwad"}
    - slot{"location": "Hubli-Dharwad"}
    - verify_location
    - slot{"location": "Hubli-Dharwad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Hubli-Dharwad"}
    - slot{"restaurant_exist": false}
* 
	- action_restart

## Generated Story -1237650150885828498
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Hubli-Dharwad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hubli-Dharwad"}
    - verify_location
    - slot{"location": "Hubli-Dharwad"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Hubli-Dharwad"}
    - slot{"restaurant_exist": false}
* goodbye
	- action_restart

## Generated Story -5550085684907924190
* greet
    - utter_greet
* restaurant_search{"location": "guwahati"}
    - slot{"location": "guwahati"}
    - verify_location
    - slot{"location": "guwahati"}
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
    - slot{"location": "guwahati"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "srikanth.vs84@gmail.com"}
    - slot{"emailid": "srikanth.vs84@gmail.com"}
    - action_send_email
    - utter_goodbye
* goodbye
	- action_restart

