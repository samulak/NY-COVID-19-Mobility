# NY-COVID-19-Transportation

## Application setup:
Application was created with python 3.8.

### Step 1:
In order to runt the application on your local machine install the following libraries:
```
pip install pandas==1.1.4
pip install numpy==1.19.4
pip install dash==1.17.0
pip install dash-bootstrap-components==0.10.7
pip install plotly==4.13.0
pip install plotly-express== 0.4.1
pip install urlopen==1.0.0
pip install urllib3==1.26.2
pip install DateTime==4.3
```
### Step 2:
Download: covid_application.py, New_York_State_Statewide_COVID-19_Testing_FIPS_3_Day.csv, and covid_image.jpg from this repository. 
Mobility data must be obtained from https://www.google.com/covid19/mobility/ and the file used in the project is: 2020_US_Region_Mobility_Report.csv.

### Step 3:
Place all the files in a directory and run:
```
python covid_application.py
```
Command prompt will display a message with a local ip address. Copy the address into the browser and explore the application.

## Note:
Libraries used for heroku deployment:
```
Brotli==1.0.9
click==7.1.2
dash==1.17.0
dash-bootstrap-components==0.10.7
dash-core-components==1.13.0
dash-html-components==1.1.1
dash-renderer==1.8.3
dash-table==4.11.0
DateTime==4.3
Flask==1.1.2
Flask-Compress==1.8.0
future==0.18.2
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
numpy==1.19.4
pandas==1.1.4
patsy==0.5.1
plotly==4.13.0
plotly-express==0.4.1
python-dateutil==2.8.1
pytz==2020.4
retrying==1.3.3
scipy==1.5.4
six==1.15.0
statsmodels==0.12.1
urllib3==1.26.2
urlopen==1.0.0
Werkzeug==1.0.1
zope.interface==5.2.0
```
