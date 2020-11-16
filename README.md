
  
# Openweather API INTEGRATION

  

![](https://github.com/innacroft/weather-repo/blob/master/dashboard_select.PNG)

  

This application consume a weather API and get last 5 days and 24 hours on main citys in Colombia from https://openweathermap.org/history.

On a custom Dashboard data average, max and min Temperature are plotted by selected city.
![](https://github.com/innacroft/weather-repo/blob/master/dashboard.PNG)
![](https://github.com/innacroft/weather-repo/blob/master/dashboardmain.PNG)
  

- [Django Dashboard Atlantis Dark - Demo](https://django-dashboard-atlantis-dark.appseed.us/) - LIVE Deployment
 
  

## Technologies:

1. Postgresql
2. Venv
3. Django
4. Javascript
5. ChartJs

    

## Usage

This project was made on Windows 10 as OS, using venv of python, requeriments are listed on requeriments.txt.

You can run the project using:

  

 1. install venv on python
 2.  clone the project
 3.  run venv env on python (on windows: env/Scripts/activate)
 4. Install redis 2.4.5 on your local machine and run server
 5. inside env:

>     python manage.py makemigrations
>     python manage.py migrate
>     python manage.py createsuperuser #create user for loggin on dashboard
>     loggin into dashboard
>     python manage.py runserver
>     Go to http://localhost:8000/weather/

  

## Features

This project isn't complete automated on dates and cities, you must include updated information:

Cities and dates are saved on a dictionaries inside the code:

*Cities:

    weather/views/Cities

 (This information was extracted from weather API on a list of cities https://openweathermap.org/history )

*Dates: Weater api returns temperature of each hour on a specific day, for getting 5 specific days before your current day. You must include this specific timestamp on the dictionary:

    /weather/views/timestamps

 (This information was generated using a generic timestamp generator https://timestampgenerator.com/ with specific 5 days ago datetimes on hour. min and secs in zero values )

You must update date names for show on dashboard on template base.html

arr1[24]='10 Noviembre'

arr1[48]='11 Noviembre'

arr1[72]='12 Noviembre'

arr1[96]='13 Noviembre'

arr1[120]='14 Noviembre'

Once you update all data you can reload url on /weather/ route and results are plotted on graph.

  

## External Tools

  

- A custom dashboard was used to plot the information and show the temperature information:

- [Django Dashboard Atlantis Dark](https://appseed.us/admin-dashboards/django-dashboard-atlantis-dark)

- Free API last 5 days:

https://openweathermap.org/history.

#### Author

Innacroft

[Link to My portfolio](https://innacroft.github.io/portfolio/)<br>

![](https://github.com/innacroft/portfolio/blob/gh-pages/images/back_inna.png)
