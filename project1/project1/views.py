from django.shortcuts import render

def my_custom_not_found_page(request, exception):
    return render(request, 'error.html', status=404)