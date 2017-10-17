from django.conf.urls import url
from django.contrib import admin

from . import views

def test(request):
	print """

	app level urls


	"""

urlpatterns = [
	url(r'^$', views.index),
	url(r'^addItem$', views.addItem),
	url(r'^clear$', views.clear),
]