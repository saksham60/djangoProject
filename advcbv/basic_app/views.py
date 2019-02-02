from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,'index.html')


class CBView(View):
    def get(self,request):
        return HttpResponse("CLASS based are cool")

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic_Injection'
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
# it returns a list school_list by default or else call a class object attrbute


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    # it returns a list school by default
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields =('name','principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
