from celery import shared_task
import requests

@shared_task
def make_get_req(lang,dt,lat,long_,units):
    #sp, es
    #http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=60.99&lon=30.9&dt=1605149949&units=metric&appid=4dec9cfaca5d992c37c77a7d00b83036
    api_key='4dec9cfaca5d992c37c77a7d00b83036'
    #api_key=''
    parameters = {'lat': lat,'lon': long_,'dt': dt,
    'lang': lang,'units': units,'appid':api_key}
    print(parameters)
    url='http://api.openweathermap.org/data/2.5/onecall/timemachine'
    response = requests.get(url,params=parameters)
    
    data = response.json()
    
    return data