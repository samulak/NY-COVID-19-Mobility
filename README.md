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
pip install jsonlib==1.6.1
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


