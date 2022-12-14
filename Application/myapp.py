# This is an external application to acces the api
import requests
import json

URL='http://127.0.0.1:8000/info/'

# fatching the data 
def get_data(id=None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)    #its converting the python dictionary data into json data
    r = requests.get(url=URL, data= json_data)
    data = r.json()
    print(data)

# get_data(1) this is the id sendig throoug by the user
# get_data()      #thsi call without id it will return all the data


#inserting the data
def post_data():
    data={
        'name': 'Suresh',
        'email': 'suresh@gmail.com',
        'city': 'gorakpur'
    }
    json_data = json.dumps(data)    #its converting the python dictionary data into json data
    r = requests.post(url=URL, data= json_data) #Thsi time we send the data into post method
    data = r.json()
    print(data)

# post_data()

def update_data():
    data={
        'id': 4,
        'name': 'Mukesh',
        'email':'mukesh@gmail.com'
    }
    json_data = json.dumps(data)    #its converting the python dictionary data into json data
    r = requests.put(url=URL, data= json_data) #put method use to update the data
    data = r.json()
    print(data)

# update_data() #update function calling


def delete_data():
    data={'id': 1}      # deleting the 4 number of id
    json_data = json.dumps(data)    #its converting the python dictionary data into json data
    r = requests.delete(url=URL, data= json_data) #delete method use to delete the data
    data = r.json()
    print(data)

delete_data()

