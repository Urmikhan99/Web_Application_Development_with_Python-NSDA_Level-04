from django.shortcuts import render

def home(request):
    
    tableDict = {
        'cmpName': 'Microsoft',
        'cmpContact': '999999',
        'country': 'USA',
        
        'cmpName1': 'Google',
        'cmpContact1': '66511111',
        'country1': 'UK',
    }
    return render(request, 'home.html',tableDict)

def about(request):
    tableDict = {
        'cmpName': 'Google',
        'cmpContact': '012342',
        'country': 'USA',
        
        'cmpName1': 'Microsoft',
        'cmpContact1': '1211',
        'country1': 'Bangladesh',
    }
    return render(request, 'about.html',tableDict)

def contact(request):
    mydict={
        'name':'Urmi',
        'phone':'00000000',
        'email':'urmi@gmail.com',
    }
    return render(request,'contact.html',mydict)

def order(request):
    mydict={
        'order_id':'14523',
        'customer_id':'4335345',
        'order_date':'16-03-2024',
    }
    return render(request,'order.html',mydict)



