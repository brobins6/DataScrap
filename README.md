# DataScrap
This project was for one of my friends. 
The purpose of this project was to scrap certain data from a google scholar search results and import the data results into a csv file 
## How the program works
--The program gets the html raw code by using pythons request library and then I use beautifulsoop to be able to access the html items. Then I grab the div tag that contains all the content I need for the scrap. Then in a for loop I go through all the elements in the div to find the data that I need and I extract it 
