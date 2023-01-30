from django.shortcuts import render

#def home_view(request):
#    return HttpResponse('Home Page')   
def simple_view(request):
    return render(request,'my_app/example.html') 