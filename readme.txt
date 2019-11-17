This is a module written in Python. It uses the Beautiful Soup Library to scrape information from the website.
It uses the the Request library to get the website data. 
It uses the json library to convert the data into a json.
 
Instruction Copy the files into the same Directory.
run Python 
From the Python terminal run the following commands:
1) pip install -r requirements.txt( do this to install libraries)
2) from scrape import *  
3) scrape_web() 

The program will open the website "http://www.wegotickets.com/searchresults/all".
It will scrape all the events listed on the page and extract the URLs. It will use the URLs' scraped
to open up the full web pages and scrap the information. The information will be stored on a Json text file locally.
The file will be named eventsjson.json
The JSON file will be an array with the following information:-
  artists_playing
  venue
  city
  date
  time
  age
