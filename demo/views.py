from django.shortcuts import render
import json
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.http import is_safe_url
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import DemoItem
# Create your views here.

class DemoItemListView(ListView):
    queryset = DemoItem.objects.all()
    template_name="apps/demo/home.html"
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super(DemoItemListView,self).get_context_data(*args,**kwargs)
        context_keys = list(context.keys())
        keys_ct = len(context_keys)
        obj_list = context.get("object_list",[])
        obj_list_ct = len(obj_list)
        request = self.request
        query = self.request.GET.get("q")
        demo_list = DemoItem.objects.all()
        #demo_filter = DemoItem(request.GET,queryset=demo_list)
        paginate_by=12
        paginator = Paginator(demo_list, paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        #demo_list = demo_filter.qs
        context['query'] = query
        item1 = "Announcements"
        context['item1'] = item1
        #context["pgfilter"]=demo_filter,
        context['total_obj'] = len(demo_list)
        context['obj_list_ct'] = obj_list_ct
        context['title'] = "Course Items"

        # print(f"CALLED get_context_data on ON SearchObjView \naction {type(action)} action -> {action}, \n context_keys ct {keys_ct} -> {context_keys} \n object_list -> {type(obj_list)} ct_obj_list -> {obj_list_ct} \n courseitem_list -> {type(courseitem_list)} courseitem_list_ct -> {courseitem_list_ct} \n total_obj {100}")
        return context


class DemoItemDetailSlugView(DetailView):
    print(f"calledDemoItemDetailSlugView")
    template_name = "apps/demo/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DemoItemDetailSlugView, self).get_context_data(*args, **kwargs)
        context_keys = list(context.keys())
        keys_ct = len(context_keys)

        print(f"get_context_data on CourseItemDetailSlugView querset ct = {type(context)}, \n context_keys ct {keys_ct} -> {context_keys}")
        return context
    
    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        objslug = self.kwargs.get("slug")
        print(f"called get_object on CourseItemDetailSlugView args {args} \n KWARGS {kwargs}\nslug {objslug}")
        instance = DemoItem.objects.get_by_slug(objslug)
        print(f"Detail object view request -> {request}")
        if instance is None:
            raise Http404("Item doesn't exist")
        return instance