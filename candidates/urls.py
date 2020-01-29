from django.urls import path

# class based urls below
from .views import (
    CandidateListView,
    CandidateDetailView,
    CandidateCreateView,
    CandidateUpdateView,
    CandidateDeleteView,

)

# function based views use this statement
from . import views

urlpatterns = [
    # routes for function based views
    # path('', views.home, name='kitchens-home'),
    # path('index/', views.home, name='kitchens-home'),
    # path('about/', views.about, name='kitchens-about'),
    #  end routes for function based views


# create, read, update, delete
# class based urls below
#     uses template home.html and this has to be converted using .as_view() function invoked
    path('', CandidateListView.as_view(), name='candidate-home'),

    # uses kitchen_detail.html template
    path('candidate<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),

    # Expects kitchen_form.html template. it does not expect post_create like you might think django uses post_form instead
    path('candidate/newpost/', CandidateCreateView.as_view(), name='candidate-create'),
    path('candidate/new_post/', CandidateCreateView.as_view(), name='blog-create'),
    path('candidate/new_conference/', CandidateCreateView.as_view(), name='conference-create'),

    path('candidate/new_message/', CandidateCreateView.as_view(), name='message-create'),
    path('candidate/new_market/', CandidateCreateView.as_view(), name='market-create'),
    path('candidate/new_assignment/', CandidateCreateView.as_view(), name='assignment-create'),


   # also uses kitchen_form.html template and shares it with the above post/new
    path('candidate/<int:pk>/update/', CandidateUpdateView.as_view(), name='candidate-update'),

    path('candidate/<int:pk>/delete/', CandidateDeleteView.as_view(), name='candidate-delete'),

    path('about/', views.about, name='candidates-about'),

]