
from django import forms
from .models import Reserve
from . import models

class ReserveForm(forms.Form):
    name = forms.CharField(max_length=100,label='氏名')
    data=[
        (1,'Aチケット (A〇～D〇〇席 〇〇〇〇円)'),
        (2,'Bチケット (E〇～H〇〇 〇〇〇〇円)'),
        (3,'Cチケット (A〇～D〇〇席 〇〇〇〇円)'),
    ]
    sheets =forms.ChoiceField(label='チケットグレード',\
        choices=data)
    phone_number = forms.CharField(label='電話番号')
    adress= forms.CharField(label='住所')