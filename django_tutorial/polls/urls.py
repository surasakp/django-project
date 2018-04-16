from django.urls import path
# from . import views
from .views import IndexView, DetailView, ResultsView, vote

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
