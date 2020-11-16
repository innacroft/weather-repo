
  
# Openweather API INTEGRATION

This application consume a weather API and get last 5 days and 24 hours on main citys in Colombia from https://openweathermap.org/history.
![](https://github.com/innacroft/weather-repo/blob/master/dashboard.PNG)
On a custom Dashboard data average, max and min Temperature are plotted by selected city.
![](https://github.com/innacroft/weather-repo/blob/master/select1.PNG)
![](https://github.com/innacroft/weather-repo/blob/master/selected1.PNG)


  

- [Django Dashboard Atlantis Dark - Demo](https://django-dashboard-atlantis-dark.appseed.us/) - LIVE Deployment
 
  

## Technologies:

1. Postgresql
2. Venv
3. Django
4. Javascript
5. ChartJs
6. Celery

    

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

  Cities=[   

    {'id_api' : 3688689,
    'city' : 'BOGOTA',
    'country': 'CO',
    'coord_lon' : -74.08, #2 decimal
    'coord_lat' :4.60 #2 decimal
    },

    ]

You can change, add  or delete each city on the dict, if you want to obtain different city weather info.

 (This information was extracted from weather API on a list of cities https://openweathermap.org/history )

*Dates: Weater api returns temperature of each hour on a specific day, for getting 5 specific days before your current day. You must include this specific timestamp on the dictionary:

    /weather/views/timestamps
    
    timestamps=[
            {'1':'1605052800'}, #Time stamp for 11 Nov 0 h, h min, h secs , timezone GMT and year 2020
            {'2':'1605139200'}, #Time stamp for 12 Nov 0 h, h min, h secs , timezone GMT and year 2020
            {'3':'1605225600'}, #Time stamp for 13 Nov 0 h, h min, h secs , timezone GMT and year 2020
            {'4':'1605312000'}, #Time stamp for 14 Nov 0 h, h min, h secs , timezone GMT and year 2020
            {'5':'1605398400'}, #Time stamp for 15 Nov 0 h, h min, h secs , timezone GMT and year 2020
            ]

 (This information was generated using a generic timestamp generator https://timestampgenerator.com/ with specific 5 days ago datetimes on hour. min and secs in zero values )

You must update date names for show on dashboard on template base.html

arr1[24]='11 Noviembre'

arr1[48]='12 Noviembre'

arr1[72]='13 Noviembre'

arr1[96]='14 Noviembre'

arr1[120]='15 Noviembre'

You must change Tittle on graph on base.html on h3 
   >Temperaturas (11 - 15 Nov 2020) ciudades principales de Colombia 

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
