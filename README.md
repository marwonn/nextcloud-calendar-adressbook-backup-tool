## About The Project

![alt text](https://github.com/marwonn/nextcloud_calendar_adressbook_backup_tool/blob/master/img/1.JPG)

The idea of the project was to save the nextcloud calendar and adressbook files for backup reasons. Personally, this was the more approbiate way of backing up my files than saving the SQL-Database and extract the calendar items from there. 


### Built With

* [Selenium](https://www.selenium.dev/)
* [Python 3.8](https://www.python.org/)


## What does the script do

Once you have set up the ```config.py```the script checks if your computer is connected to a known wifi. Then the script starts the selenium web driver and logs into your account and beginns to download the calendar and adressbook files to your current working directory. After that the downloaded files were moved to a subfolder of your current working directory named "backup_cal".

### Prerequisites

1. ```pip install -r requirements.txt```
2. Download & install [Selenium Web Driver for Firefox](https://github.com/mozilla/geckodriver/releases)

### config.py

Firstly, all the credentials, your nextcloud directory, your domain and the names of your calendars needs to be defined in the ```config.py```.


## Usage

To start the script run the ```backup.py```from your CLI.





