#Requirement :

Create a web application which uses railway's api (https://railwayapi.com/api/#seat-availability) to get seat availability status.
Input Fields : Train number , From station , To station , date , class , quota
Output Fields : Seat availability status for next 5 days from given date

Use your HTML/CSS skill to create frontend for the application and log all the request in a database table. You can use (mlabs - online MongoDB) database for storing logs.



Solution & Design : 

Structure :
- server.js : app server based on express.js that helps avail port .
- index.html : HTML page used here is a form that takes arguments as :
		Train number 
		From station 
		To station 
		date 
		class	
		quota 
	And submits the arguments into a url that creates a request to the railway api for getting the data .

As the arguments are filled in the html form and submit button is pressed the server gets the parameter so as to access from railway api using the apikey.

As soon as the response from the api is returned the data is processed on the display of the browser.

Further,

Css needs to be worked out(responsive).
Mongodb needs to be integrated so as to log.
Displaying data must be returned in a format something like table.




Sample Input:
Train no. : 12001
Source : BPL
Destination : NDLS
Date : 16-01-2019
Preference : CC
Quota : GN 

Sample Output :

{"Data":{"debit":3,"quota":{"name":"GENERAL QUOTA","code":"GN"},"train":{"number":"12001","days":[{"runs":"Y","code":"MON"},{"runs":"Y","code":"TUE"},{"runs":"Y","code":"WED"},{"runs":"Y","code":"THU"},{"runs":"Y","code":"FRI"},{"runs":"Y","code":"SAT"},{"runs":"Y","code":"SUN"}],"name":"BPL - NDLS SHATABDI EXP","classes":[{"available":"N","name":"3rd AC ECONOMY","code":"3E"},{"available":"N","name":"FIRST CLASS","code":"FC"},{"available":"Y","name":"AC CHAIR CAR","code":"CC"},{"available":"N","name":"THIRD AC","code":"3A"},{"available":"N","name":"SECOND AC","code":"2A"},{"available":"N","name":"SECOND SEATING","code":"2S"},{"available":"N","name":"SLEEPER CLASS","code":"SL"},{"available":"N","name":"FIRST AC","code":"1A"}]},"from_station":{"lng":77.3962718,"name":"BHOPAL  JN","code":"BPL","lat":23.2530923},"to_station":{"lng":77.2022662,"name":"NEW DELHI","code":"NDLS","lat":28.6141793},"response_code":200,"journey_class":{"name":"AC CHAIR CAR","code":"CC"},"availability":[{"status":"AVAILABLE-0571","date":"16-1-2019"},{"status":"AVAILABLE-0575","date":"17-1-2019"},{"status":"AVAILABLE-0511","date":"18-1-2019"},{"status":"AVAILABLE-0557","date":"19-1-2019"},{"status":"AVAILABLE-0570","date":"20-1-2019"},{"status":"AVAILABLE-0575","date":"21-1-2019"}]}}
 
