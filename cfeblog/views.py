from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from django.views.generic import (
    RedirectView
)
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import CfePost
from .forms import CfePostForm


# def post_create(request,*args,**kwargs):
#     template_name="apps/cfeblog/post_form.html"
    
    # if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
		
	#form = CfePostForm(request.POST or None, request.FILES or None)
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	instance.user = request.user
	# 	instance.save()
	# 	# message success
	# 	messages.success(request, "Successfully Created")
	# 	return HttpResponseRedirect(instance.get_absolute_url())
	#context = {}
	#return render(request,template_name)

def post_detail(request, slug=None):
	template_name="apps/cfeblog/post_detail.html"
	instance = get_object_or_404(CfePost, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404

	initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
	}
	
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request,template_name, context)


def post_list(request):
	template_name="apps/cfeblog/post_list.html"
	today = timezone.now().date()
	queryset_list = CfePost.objects.all() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = CfePost.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request,template_name,context)





def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(CfePost, slug=slug)
	form = CfePostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)



def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(CfePost, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")