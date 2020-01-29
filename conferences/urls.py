from django.urls import path

# class based urls below
from .views import (
    ConferenceListView,
    ConferenceDetailView,
    ConferenceCreateView,
    ConferenceUpdateView,
    ConferenceDeleteView,

)

# function based views use this statement
from . import views

urlpatterns = [
    # routes for function based views
    path('', views.home, name='conferences-home'),
    path('about/', views.about, name='conferences-about'),
    #  end routes for function based views


# create, read, update, delete
# class based urls below
#     uses template home.html and this has to be converted using .as_view() function invoked
    path('conferences/', ConferenceListView.as_view(), name='conference-home'),

    # uses kitchen_detail.html template
    path('conference<int:pk>/', ConferenceDetailView.as_view(), name='conference-detail'),

    # Expects kitchen_form.html template. it does not expect post_create like you might think django uses post_form instead
    path('new_conference/', ConferenceCreateView.as_view(), name='conference-create'),
    # path('conference/new_conference/', ConferenceCreateView.as_view(), name='blog-create'),

    # path('conference/new_message/', ConferenceCreateView.as_view(), name='message-create'),
    # path('conference/new_market/', ConferenceCreateView.as_view(), name='market-create'),
    # path('conference/new_assignment/', ConferenceCreateView.as_view(), name='assignment-create'),


   # also uses kitchen_form.html template and shares it with the above post/new
    path('conference/<int:pk>/update/', ConferenceUpdateView.as_view(), name='conference-update'),

    path('conference/<int:pk>/delete/', ConferenceDeleteView.as_view(), name='conference-delete'),

    # path('about/', views.about, name='conferences-about'),

]