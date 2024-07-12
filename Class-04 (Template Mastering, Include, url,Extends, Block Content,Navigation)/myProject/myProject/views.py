from django.shortcuts import render

def home(request):
    
    tableDict = {
        'cmpName': 'Youtube',
        'cmpContact': '999444',
        'country': 'USA',
        
        'cmpName1': 'Microsoft',
        'cmpContact1': '55123121',
        'country1': 'UK',
    }
    return render(request, 'index.html',tableDict)

def about(request):
    return render(request, 'about.html')
def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')



