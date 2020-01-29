

# ************
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Use this for builtin class based views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from pip._internal.models import candidate

# from .models import Candidate
from .models import Candidate


# Function based views below
def candidate_home(request):
    context = {
        'candidates': Candidate.objects.all()
    }
    return render(request, 'candidates/home.html', context)


# class based views and inherit from ListView  looks for a templatename <app?/<modle?.html  so we need to set template name for class views
class CandidateListView(ListView):
    model = Candidate

    # need to set template = to be home.html in order to work
    template_name = 'candidates/candidate-home.html'  # could name template this but we can convert here  <app>/<model>_<viewtype>.html

    # need to set the object = to posts here which the template is looping over
    # or change the template looping variable posts to object
    context_object_name = 'candidates'

    # need to reorder the posts which can be done by setting the variable ordering to -dateposted
    ordering = ['-created_at']


class UserCandidateListView(ListView):
    model = Candidate
    template_name = 'candidates/user_candidates.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'candidates'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Candidates.objects.filter(author=user).order_by('-created_at')



# This is a typical class view using
class CandidateDetailView(DetailView):
    model = Candidate


class CandidateCreateView(LoginRequiredMixin, CreateView):
    model = Candidate
    fields = ['first_name', 'last_name']

# Need to override the form
    def form_valid(self, form):
        # run the form method to the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class CandidateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Candidate
    fields = ['first_name', 'last_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        candidate = self.get_object()
        if self.request.user == candidate.author:
            return True
        return False


class CandidateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Candidate
    success_url = '/'

    # Function to make sure author is the registered user to do the deleting
    def test_func(self):
        post = self.get_object()
        if self.request.user == candidate:
            return True
        return False

def about(request):
    return render(request, 'candidates/about.html', {'candidate': 'About'})

