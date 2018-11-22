from django.urls import include, path

from . import views

app_name = 'tree'

urlpatterns = [
	path('', views.index, name='index'),
	#path('wiki/', include('wiki.urls')),
	path('<int:person_id>/', views.detail, name='detail'),
]
