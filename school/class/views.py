from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView
from .forms import ContactForm
from .models import Teacher
# Create your views here.

#def home_view(request):
#    return render(request, 'class/home.html')

class HomeView(TemplateView):
    template_name = 'class/home.html'

class ThanYou(TemplateView):
    template_name = 'class/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'class/contact.html'

    success_url = '/class/thank_you/'  # actually the URL not the template

    def form_valid(self, form):
        print(form.cleaned_data) 
        return  super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('class:thank_you')

class TeacherListView(ListView):
    
    model = Teacher
    queryset = Teacher.objects.order_by('first_name') # add any filters

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('class:list_teacher')