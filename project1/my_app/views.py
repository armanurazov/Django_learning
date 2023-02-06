from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request, 'my_app/example.html')

def variable(request):
    my_var = {'first_name': 'Arman', 'last_name':'Arman',
    'some_list':[1,2,3], 'some_dict': {'admin': False,'key1': 'value1','key2': 'value2','key3': 'value3'}}
    return render(request, 'my_app/variable.html', context = my_var)

def inherit(request):
    return render(request, 'my_app/inherit.html')   