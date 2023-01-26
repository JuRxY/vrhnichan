from flask import Flask, render_template, url_for
from threading import Thread
from urllib.request import urlopen
import json
import os


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


app = Flask('')

@app.route('/')
def home():
  return render_template("home.html")
  
@app.route('/vrhnika')
def vrhnika():
	returned_minutes, returned_arrival_time, returned_name, returned_key = get_arrival(str('776011'))
	returned_minutes2, returned_arrival_time2, returned_name2, returned_key2 = get_arrival(str('776012'))
	return render_template("vrhnika.html", hminutes=returned_minutes, htime=returned_arrival_time, hname=returned_name, hkey=returned_key, kminutes=returned_minutes2, ktime=returned_arrival_time2, kname=returned_name2, kkey=returned_key2)

@app.route('/logatec')
def logatec():
	returned_minutes, returned_arrival_time, returned_name, returned_key = get_arrival(str('707021'))
	returned_minutes2, returned_arrival_time2, returned_name2, returned_key2 = get_arrival(str('707022'))
	return render_template("logatec.html", hminutes=returned_minutes, htime=returned_arrival_time, hname="Ljubljana - Vrhnika - Logatec", hkey=returned_key, kminutes=returned_minutes2, ktime=returned_arrival_time2, kname="Logatec - Vrhnika - Ljubljana", kkey=returned_key2)


def run():
    app.run(
		host='0.0.0.0',
		port=8000
	)


def keep_alive():
	t = Thread(target=run)
	t.start()

keep_alive()

import webbrowser

webbrowser.open('http://127.0.0.1:8000/')