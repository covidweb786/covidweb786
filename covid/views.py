from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import os
import requests
from joblib import load
from numpy import array
from .models import TestDetail


def index(request):
    a = "COVID-19 Prediction"
    b = ""
    return render(request, "covid/home.html", {
    "a":a, "b":b
    })


def test(request):
    return render(request, "covid/index.html")


def about(request):
    return render(request, "covid/about.html")


def prediction(request):
    symtoms_values = []
    print(request.POST)
    name = request.POST.get("name")
    cough = request.POST.get("cough")
    symtoms_values.append(cough)

    fever = request.POST.get("fever")
    symtoms_values.append(fever)


    sore = request.POST.get("sore")
    symtoms_values.append(sore)

    breath = request.POST.get("breath")
    symtoms_values.append(breath)

    head = request.POST.get("head")
    symtoms_values.append(head)

    older = request.POST.get("older")
    symtoms_values.append(older)
    male = request.POST.get("male")
    symtoms_values.append(male)

    patient = request.POST.get("patient")
    user = request.POST["name"]
    symtoms_values.append(patient)
    lr = load('logistic_regression.joblib')
    rf = load('random_forest.joblib')
    print('data',rf.predict_proba(array(symtoms_values).reshape(1, -1)))
    if rf.predict(array(symtoms_values).reshape(1, -1))[0] == 0:
        a = "You are most likely safe"
    else:
        a = "You most likely got the COVID virus"

    # b = "Your chance of having the COVID is {:.2f} %".format(lr.predict_proba(array(symtoms_values).reshape(1, -1))[0][1]*100)
    b="{:.0f}".format(lr.predict_proba(array(symtoms_values).reshape(1, -1))[0][1]*100)
    try:
        result = TestDetail(user_name=user, result=a, fever=fever, sore=sore,
        male=male, breath=breath, head=head, older=older,
        patient=patient, cough=cough)
        result.save()
    except:
        print("you have some error, data not saved in model")
    return render(request, "covid/s.html", {
    "a":a, "b":b, "name":user
    })
