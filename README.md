# data-rep-project
Main project as part of the Data Representation module at ATU

Author: Katie O'Brien G00398250

This project is in partial submission for the H.Dip in Data Analytics in Computing

This project asked the user to create a program that demonstrates understanding around creating and consuming RESTful APIs. 
The requirements stated that the project should have a web application, created in Flask that has a RESTful API, and the application should link to 1 or more database tables. It should also include the web pages that can consume the API. I.e. performs CRUD operations on the data.

This project contains a DAO file, a Flask file, and a HTML file. It also includes some images that are used on the HTML pages 


```dao_f1driver.py```- This contains the mySQL and configuration files for the ```my_sql_connector``` framework which allows the databases that are being used to interact with the webpage via the Flask server. There are multiple functions in this file for the CRUD operations required, however, with the exception of the ```createdatabases``` and ```createtables``` functions, none of these are ran from the file but instead are imported into the Flask Server. 

```application.py``` This contains the Flask server that interact with the webpage in order to transfer data and requests to the database and back. This primarily contains the basic CRUD operations that are required for the page to be run properly. 

```drivers.html``` The webpage that allows the user to interact with the  webpage correctly. This also contains the AJAX and JavaScript calls that go to the server to pull the data requests off there. It contains no functionality beyond the CRUD calls that are required for Adding Deleting Updating and Viewing the data. 
```requirements.txt``` contains the files used when accessing this file from a Virtual Environment.This allows a user to easy install the additional libraries etc without interfering with the users system files. 

## Running the files 
- Download the entire repository to your local machine
- The user should install a virtual enviroment before use. This is done by using the command terminal and moving to the correct folder then typing ```python -m 
 venv env``` pressing enter, then using either ```.\env\Scripts\activate.bat``` in Windows or ```source env/bin/activate``` in Linux/MacOS.
 When this is complete use ```pip install requirements.txt```. 
 - The user should also install WAMP server on Windows to allow the user to interact with mySQL, or alternative options are available on Mac/Linux. (For Linux, MariaDB is a good alternative, however, the ```db-connector``` is unstable on some devices, including my own chromebook)
 - The ```application.py``` program should be run and the web browser should be opened on the localhost that the program advises (usually http://127.0.0.1:5000/) to access the webpage and associated files and folders. 


## Hosting

As part of the added functionality the project was hosted on pythonanywhere and is available on the following link: 

- http://kaob91.eu.pythonanywhere.com
It is important to ensure that the page is http instead of https as the database does not load with the extra layer of security.


## Conclusion

Unfortunately, further functionality such as adding in additional Databases, authorisation and 3rd party apis were beyond the time constraints I had for this project. Further developments to the project would have included getting a user authorisation before modifying the database, and using an API related to the topic to pull data, including race results from the following site: http://ergast.com/mrd/, and putting the data from that into a secondary database. I plan on continuing this following completion of the course as I feel that this was an area that I particularly struggled with and would like to further my understanding around API's and how everything interacts with each other 



