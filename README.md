# data-rep-project
Main project as part of the Data Representation module at ATU
Author: Katie O'Brien G00398250

This project is in partial submission for the H.Dip in Data Analytics in Computing

This project asked the user to create a program that demonstrates understanding around creating and consuming RESTful APIs. 
The requirements stated that the project should have a web application, created in Flask that has a RESTful API, and the application should link to 1 or more database tables. It should also include the web pages that can consume the API. I.e. performs CRUD operations on the data.

Thid project contains a DAO file, a Flask file, and a HTML file. It also includes some images that are used on the HTML pages 


```dao_f1driver.py```- This contains the mySQL and configuration files for the ```my_sql_connector``` framework which allows the databases that are being used to interact with the webpage via the Flask server. There are multiple functions in this file for the CRUD operations required, however, with the exception of the ```createdatabases``` and ```createtables``` functions, none of these are ran from the file but instead are imported into the Flask Server. 

```application.py``` This contains the Flask server that interact with the webpage in order to transfer data and requests to the database and back. This primarily contains the basic CRUD operations that are required for the page to be run properly. 

```drivers.html``` The webpage that allows the user to interact with the  webpage correctly. This also contains the AJAX and JavaScript calls that go to the server to pull the data requests off there. It contains no functionality beyond the CRUD calls that are required for Adding Deleting Updating and Viewing the data. 


## Hosting

As part of the added functionality the project was hosted on pythonanywhere and is available on the following link: 

- http://kaob91.eu.pythonanywhere.com
It is important to ensure that the page is http instead of https as the database does not load with the extra layer of security.


## Conclusion

Unfortunately, further functionality such as adding in additional Databases, authorisation and 3rd party apis were beyond the time constraints I had for this project. Further developments to the project would have included getting a user authorisation before modifying the database, and using an API related to the topic to pull data, including race results from the following site, and putting the data from that into a secondary database. I plan on continuing this following completion of the course as I feel that this was an area that I particularly struggled with and would like to further my understanding around API's and how everything interacts with each other 



