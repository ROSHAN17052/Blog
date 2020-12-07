from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.http import Http404


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"


class Postview(ListView):
    model=Post
    template_name='blog.html'
    ordering=['id']
    paginate_by='3'
    paginate_orphans=2
    def get_context_data(self,*args, **kwargs):
        try:
          return super(Postview, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page']=1
            context = super(Postview,self).get_context_data(*args,**kwargs)
            return context
  
