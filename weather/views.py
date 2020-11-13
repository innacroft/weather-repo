
import json 
import calendar
import time

from django.shortcuts import render
from .tasks import make_get_req
from  .models import City


Citys=[ #BOGOTA, MEDELLIN,CALI, BARRANQUILLA,CARTAGENA,SOACHA, CUCUTA, SOLEDAD,BUCARAMANGA, BELLO
    {'id_api' : 3688689,
    'city' : 'BOGOTA',
    'country': 'CO',
    'coord_lon' : -74.08, #2 decimal
    'coord_lat' :4.60 #2 decimal
    },

    {'id_api' : 3674962,
    'city' : 'MEDELLIN',
    'country': 'CO',
    'coord_lon' : -75.563591,
    'coord_lat' :6.25184
    },

    {'id_api' : 3687925,
    'city' : 'CALI',
    'country': 'CO',
    'coord_lon' : -76.522499,
    'coord_lat' :3.43722
    },

    {'id_api' : 3896433,
    'city' : 'CARTAGENA',
    'country': 'CO',
    'coord_lon' : -71.605278,
    'coord_lat' : -33.554169
    },

    {'id_api' : 3667905,
    'city' : 'SOACHA',
    'country': 'CO',
    'coord_lon' : -74.21682,
    'coord_lat' :  4.57937
    },

    {'id_api' : 3685533,
    'city' : 'CUCUTA',
    'country': 'CO',
    'coord_lon' : -72.50528,
    'coord_lat' : 7.88333
    },

    {'id_api' : 3667849,
    'city' : 'SOLEDAD',
    'country': 'CO',
    'coord_lon' : -74.764587,
    'coord_lat' : 10.91843
    },

     {'id_api' : 3688465,
    'city' : 'BUCARAMANGA',
    'country': 'CO',
    'coord_lon' : -73.119797,
    'coord_lat' :  7.12539
    },

     {'id_api' : 3688928,
    'city' : 'BELLO',
    'country': 'CO',
    'coord_lon' : -75.557953,
    'coord_lat' : 6.33732
    },

    ]

timestamps=[{'8':'1604793600'},
            {'9':'1604880000'},
            {'10':'1604793600'},
            {'11':'1604793600'},
            {'12':'1605139200'},
            ]


def weather(request):
    Dict={}
    for city in Citys:
        city_name=city.get('city')
        totaltemp=[]
        Dict2={}
        print(city_name)
        for dict_time in timestamps:
            for key,value in dict_time.items():
                data=make_get_req(lang='es',dt=value,lat=city['coord_lat'],long_=city['coord_lon'],units='metric')
                for temp in data['hourly']:
                    totaltemp.append(temp['temp'])
                Dict2['totaltemp']=totaltemp
                length=len(totaltemp)
                Dict2['temp_prom']=round(sum(totaltemp)/length , 2)
                Dict2['temp_max']=max(totaltemp)
                Dict2['temp_min']=min(totaltemp)
                Dict2['city']=city_name
                Dict[city_name]=Dict2
    return render(request, 'weather/base.html', {'Dict':Dict})


# def read_cities_from_doc(message):
#     print('read_cities_from_doc',message)
#     with open('weather/data.json') as json_file:
#         total_data = json.loads(json_file.read())
#         print(total_data)
        # for data in total_data:
        #     id_=data['id']
        #     city_=data['city']
            
            
        #     name_=city_['name']
        #     country_=city_['country']
        #     coord=city_['coord']
        #     coord_lon_=coord['lon']
        #     coord_lat_=coord['lat']
        #     print(f'id_ {id_},name_ {name_},country {country_},coord_lon {coord_lon_},coord_lat {coord_lat_}')
        #     city=City(id_api=id_,city=city_,country=country_,coord_lon=coord_lon_,coord_lat=coord_lat_)
        #     city.save()
                

