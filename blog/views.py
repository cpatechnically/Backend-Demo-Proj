from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


def home(request):
    template_name="apps/blog/home.html"
    #if post 
    context = {
        'posts': Post.objects.all()
    }
    return render(request,template_name, context)


class PostListView(ListView):
    model = Post
    template_name = 'apps/blog/home.html'
    context_object_name = 'posts'
    #set order of list
    ordering = ['-date_posted']
    #paginate_by is the only thing required to perform pagination
    paginate_by = 5


#View returning all of the posts only by a specified user, still should be paginated
class UserPostListView(ListView):
    model = Post
    template_name = 'apps/blog/user_posts.html'
    context_object_name = 'posts'
    #paginate_by is the only thing required to perform pagination
    paginate_by = 5

    #function to filter by a user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    template_name = 'apps/blog/detail.html'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'apps/blog/forms/post.html'
    model = Post
    #set the fields available in the form view
    #THIS does NOT include automatically created fields like the date posted
    fields = ['title','content']

    #Method to override the FORM VALID METHOD which will allow us to add the author/user before submission
    def form_valid(self, form):
        #telling the form that the current "instance" being posted, the AUTHOR is the user creating the post
        form.instance.author = self.request.user
        #Use the SUPER method to call the parent method
        #All we are doing is setting the AUTHOR of the post BEFORE the form validation method is run
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'apps/blog/forms/post.html'
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #test for user passes test to confirm the correct user is accessing only their posts
    def test_func(self):
        #defining the post object
        post = self.get_object()
        #if the current logged in user is equal to the current post authro
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'apps/blog/post_confirm_delete.html'
    model = Post
    #Redirect after deletion
    success_url = '/blog'

    #only test is to make sure the current logged in user is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request,'apps/blog/about.html', {'title': 'About'})
