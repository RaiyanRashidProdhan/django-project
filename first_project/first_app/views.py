from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from first_app.models import AccessRecord,Topic,Webpage

@csrf_exempt #- using it here will disable CSRF protection for this whole view

# Create your views here.
def index(request):

    #my_dict = {'insert_me': "Hello I am from first_app/index.html my value is coming from insert_me"}

    #Crating tuples of every row from AccessRecords table
    webpages_list = AccessRecord.objects.order_by('date')
    #Creating a dictionary basen on those tuples
    date_dict = {'access_records' : webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
    #using csrf_exempt(filename.html) will only disable CSRF protection for only this specific html file
