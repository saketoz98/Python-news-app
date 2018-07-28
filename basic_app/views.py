from django.shortcuts import render
import requests
from basic_app.forms import SelectCategory

#from urllib.requests import urlopen
#from newsapi import NewsApiClient
# Create your views here.


def index(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=546189393d044221bfc72c4d5a5fde33')
    response = requests.get(url)
    data = response.json()
    imagesURL = []
    news = []
    for i in range(3):
        d = data['articles'][i]
        imagesURL.append(d['urlToImage'])
    for i in range(3):
        d = data['articles'][i]
        news.append(d)
    # print(news)
    #print(imagesURL)
    # for i in data.articles:
    #     imagesURL.append(i.urlToImage)
    # print(imagesURL)
    details = {
        'all_news' : data,
        'i1'   : imagesURL[0],
        'i2'   : imagesURL[1],
        'i3'   : imagesURL[2],
        'carouselNews' : news,

    }
    return render(request,'basic_app/index.html',details)

def about(request):
    return render(request,'basic_app/about.html')

def formHandlerView(request):
    form = SelectCategory()
    if request.method == "POST":
        form = SelectCategory(request.POST)
        if form.is_valid():
            address = form.cleaned_data['category']
            country = form.cleaned_data['country']
            return categoryView(request,address,country)
    return render(request,'basic_app/forms.html',{'form':form})

def categoryView(request,address='technology',country='in'):
    url = 'https://newsapi.org/v2/top-headlines?'
    apiKey = 'apiKey=546189393d044221bfc72c4d5a5fde33'
    passCategory = address
    passCountry = country
    category = 'category='+ address
    ct = 'country='+ country
    url = url + category + '&' + ct + '&'+ apiKey
    response = requests.get(url)
    data = response.json()
    details = {
        'all_news' : data,
        'address' : passCategory,
        'country' : passCountry,
    }
    return render(request,'basic_app/category.html',details)
