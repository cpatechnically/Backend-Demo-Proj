from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView



# Create your views here.
class SearchView(ListView):
    template_name = "apps/search/view.html"

    def get_context_data(self,*args,**kwargs):
        print(f"called get context")
        context = super(SearchView,self).get_context_data(*args,**kwargs)
        print(f"context {context}")
        query = self.request.GET.get("q")
        context['query'] = query
        return context


    def get_queryset(self,*args,**kwargs):
        print(f"called get queryset")
        request = self.request
        method_dict = request.GET
        print(f"list request {request}, args {args}, kwargs {kwargs}, method_dict {method_dict}")

        query = method_dict.get('q', None)
        
        # if query is not None:
        #     return Resource.objects.search(query)
        # return Resource.objects.apps()

