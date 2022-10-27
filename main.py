#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mimetypes
from operator import ge
from flask import Flask, render_template, request, Response, send_file
import datetime
from random import randint
import pandas as pd


#################### Logic ################


def randomize(ar, i):
    for i in range(i - 1, 0, -1):
        j = randint(0, i-1)
        ar[i], ar[j] = ar[j], ar[i]
    return ar

def generateMenu():
        x = datetime.datetime.now()
        print(x)
        arr = ['Roast,Sambar,Coconut Chutney(Varamilagai),Milk,Coffee', 'Plain Dosa,Kondakadalai Kolambu,Coconut Chutney(Green Chilli)', 'Pongal,Vadai,Sambar,Coconut Chutney(Grenn Chilli),Plain Bread,Butter,Milk,Coffee', 'Idli,Sambar,Kara Chutney(Tomato with varamilagai),White rava uppama,Podi,Oil,Milk,Coffee', 'Rava kichidi,Toasted Bread,Bread,Butter,Jam,Milk,Coffee,Omlet', 'Idly,Sambar,Ulundhu Vadai,Aval Uppma/Samaba rava+curd,Sakarai Pongal,Groundnut Chutnet,Milk,Coffee', 'Sandagai(Tomato and Plain) Chutney,Toasted Bread,Butter,Sugar,Milk,Coffee' ]
        n = len(arr)
        nr = randomize(arr, n)
        # print(nr)
        arr2 = ['Rice,Pasi Payaru/Kollu Parupu,Proriyal,Rasam,Curd,Pickle,Appalam,Boiled Egg', 'Rice,Dhal Sambar,Rasam,Curd,Cabbage/Carrot poriyal,Parupu Vadai,Payasam,Ghee', 'Rice ,Buttermilk Kolumbu,Poriyal Rasam,Curd,Vadagam,pickle,Omlet','Rice Sambar Rasam Soya Poriyal(Not chopped),Curd,Applam,Pickle','Rice, Plain, Dhall ,Ghee+Pulikulambu, Potato, Poriyal,curd,Rasam,Pickle,Appalam', 'Jeera Rice,Mushroom/Veg Gravy/Potato kuruma,Poriyal/Potato chips,Curd rice,Rasasadam', 'Rice,Kathmba Sambar,Rasam,Beetroot poriyal,Curd,Vadagam ,Pickle']
        n1 = len(arr2)
        nr1 = randomize(arr2, n1)
        # print(nr1)
        arr3 = ['Parotta,Veg Kuruma/Potato Kuruma,Curd Rice,Milk,Tea', 'Noodles/Macaroni Pasat,Plain Kuruma,Sambar satham,Omlet,Tea,Milk,Curd rice', 'Roast ,sambar,Chutney,(Mali/Pudina) Chutney,Curd Rice,Tea,Milk', 'Chapati,Idly Upma,Jam,White Kuruma,Egg/Egg Masala,Ragi Malt,Tea', 'Kothu Parotta and Vegkuruma,Chilly Parotta and Curd Raitha(Alternate Week)Romali Rotti (Monthly Once) and Paneer Butter Masala,Curd Rice', 'Plain Dosa,Sambar,(Malli/Pudina)Chutney,Curd rice,Tea,Milk', 'Chapatti,White Kuruma and jam,Sambar Rice,Boiled Egg,Ragimalt,Tea']
        n2 = len(arr3)
        nr2 = randomize(arr3, n2)
        # print(nr2)
        morning = pd.DataFrame(nr, columns=['morning'])
        lunch = pd.DataFrame(nr1, columns=['lunch'])
        dinner = pd.DataFrame(nr2, columns=['dinner'])
        e = (pd.concat([morning, lunch, dinner], axis=1))
        e1 = pd.DataFrame(e)
        # print(e1)
        e1.to_csv(r'op.csv')



#################### Logic ################





DEVELOPMENT_ENV  = True

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Generate')
def plot_csv():
    generateMenu()
    return send_file(
        'op.csv',
        mimetype='text/csv',
        download_name='New_Menu.csv',
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)