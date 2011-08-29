from django.shortcuts import render_to_response
from django.http import HttpResponse
import sqlite3

import os

def input(request):
    return render_to_response("input.html")

def generate(request):
    rannum=request.POST['itemno']
    
    ## SQLITE3 ##
    db=sqlite3.connect(os.path.join(ROOT_PATH,"toefl.db"))
    cursor=db.cursor()
    cursor.execute("SELECT A,B,C,D,example,Ans FROM dist ORDER BY RANDOM() LIMIT %s" % (rannum))
    r=cursor.fetchall()
    db.close
    r=[(i1.split(';')[0],i2.split(';')[0],i3.split(';')[0],i4.split(';')[0],example,Ans) for i1,i2,i3,i4, example,Ans in r]
    return render_to_response("item.html", {'item':r})