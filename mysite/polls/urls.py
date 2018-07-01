from django.urls import path
from . import views

app_name = 'polls' #app has its own namespace.
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResusltsView.as_view(), name='results'),
        path('<int:pk>/vote/', views.vote, name='vote'),
        ] 
