from django.shortcuts import render
from ForoApp.models import Post, Profile
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ForoApp.forms import PostForm


# Create your views here.

def index(request):
    return render(request, "ForoApp/index.html")

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("index")
    fields = '__all__'


class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostMineList(LoginRequiredMixin, PostList):
    
    def get_queryset(self):
        return Post.objects.filter(publisher=self.request.user.id).all()

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id =  self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id, id=post_id).exists()


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id =  self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id, id=post_id).exists()
    
def buscar(request): 
    criterio = request.GET.get("criterio")
    context = {
        "posts": Post.objects.filter(titulo__icontains=criterio).all(),
    }
    return render(request, "ForoApp/busqueda.html", context)

class Login(LoginView):
    next_page = reverse_lazy("index")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')


class Logout(LogoutView):
    template_name = "registration/logout.html"


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ['avatar','nombre']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ['avatar','nombre']

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()

class ProfileDetail(DetailView):
    model = Profile
    context_object_name = "profile"
