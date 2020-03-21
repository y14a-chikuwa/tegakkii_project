from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class ViewForTegakkii(TemplateView):
	template_name = "welcome.html"


