from cv2 import split
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    details ={
        'name':'srikanth',
        'age':'20',
        'gender':'male'

    }
    return render(request,'index.html')

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request,'counter.html',{'amount':amount_of_words})