from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PostCreateForm

@login_required
def home(request):
    
    context = {
        'posts': Post.objects.all()  
    }
    
    return render(request, 'blog/home.html',context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    


class PostDetailView(DetailView):
    model = Post




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.FILES is not None:
            form.instance.content = self.request.FILES['file']
        return super().form_valid(form)
        

class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):    
    
    model = Post
    fields = ['title', 'content']
    success_message = f'You have successfully updated the post'    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

def about(request):
    context = {
        'title':'About'        
    }
    return render(request, 'blog/about.html',context)