from configparser import ConfigParser
import requests
from tkinter import*
from tkinter import messagebox

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['divya']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
def getweather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin,temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")

def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_Ibl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+" Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Eror', "Cannot find {}".format(city))

app = Tk()
app.title("Weather App")
app.geometry("300x300")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
Search_btn = Button(app, text="Search Weather",bg='royalblue', fg='white',font=('helvetica',12, 'bold'), command=search)
Search_btn.pack()
location_i=lbl = Label(app, text="Loaction", font={'bold', 20})
location_lbl.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_1 = Label(app, text="")
weather_1.pack()
app.mainloop()
