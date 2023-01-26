from urllib.request import urlopen
import json


def get_arrival(selected_bus):
	try:
		url = "https://www.lpp.si/lpp/ajax/1/"+selected_bus
		json_obj = urlopen(url)
		data = json.load(json_obj)
		bus_47_first = data[0][0]
	
		minutes = bus_47_first['minutes']
		arrival_time = bus_47_first['time']
		name = bus_47_first['name']
		key = bus_47_first['key']
		type = bus_47_first['type']
	except:
		minutes = "Ni na voljo"
		arrival_time = "Ni na voljo"
		name = "Ni na voljo"
		key = "Ni na voljo"
		type = "Ni na voljo"
 
	return minutes, arrival_time, name, key