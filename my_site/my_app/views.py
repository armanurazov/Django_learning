from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# articles = {
#     'sports' : 'Sports Page',
#     'finance' : 'Finance Page',
#     'politics' : 'Politics Page'
# }

# def news_view(request, topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         result = 'No page for that topic'
#         return HttpResponseNotFound(result)

# def add_view(request, num1, num2):
#     add_result = num1+num2
#     result = f'{num1} + {num2} = {add_result}'
#     return HttpResponse(result)


# def num_page_view(request, num_page):
#     topics_list = list(articles.keys())
#     topic = topics_list[num_page]

#     webpage = reverse('topic-page', args=[topic])

#     return HttpResponseRedirect(webpage)



# Create your views here.
