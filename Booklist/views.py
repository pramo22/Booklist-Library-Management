
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from .models import BookTask
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class ListBook(LoginRequiredMixin,ListView):
    model = BookTask
    template_name = 'base/index.html'
    context_object_name = 'booklist'
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booklist'] = context['booklist'].filter(user=self.request.user)
        return context

class ViewBook(LoginRequiredMixin,DetailView):
    model = BookTask
    template_name = 'base/view.html'
    context_object_name = 'tasks'
    login_url = '/login/'

def upload_file(request):
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request,'base/create.html',{'form':form})

class CreateBook(LoginRequiredMixin,CreateView):
    model = BookTask
    form_class = BookForm
    template_name = "base/create.html"
    #fields = ['cover','title','price','author','description','book','complete']
    success_message = 'Your submission is successful!'
    success_url = reverse_lazy('index')
    login_url = '/login/'

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super(CreateBook, self).form_valid(form)

    def get_success_message(self):
        return self.success_message

class UpdateBook(LoginRequiredMixin,UpdateView):
    model = BookTask
    template_name = 'base/create.html'
    #fields = ['cover','title','price','author','description','book','complete']
    success_message = 'Your submission is successful!'
    success_url = reverse_lazy('index')
    form_class = BookForm
    login_url = '/login/'

    def get_success_message(self):
        return self.success_message

class DeleteBook(LoginRequiredMixin,DeleteView):
    model = BookTask
    fields = ['title']
    template_name = 'base/delete.html'
    success_url = reverse_lazy('index')
    login_url = '/login/'

class LoginUser(LoginView):
    template_name = 'base/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class SignupUser(FormView):
    form_class = UserCreationForm
    template_name = "base/register.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(SignupUser,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(SignupUser,self).get(*args,**kwargs)