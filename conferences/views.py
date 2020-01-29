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

from .models import Conference

# Function based views below
def home(request):
    context = {
        'conferences': Conference.objects.all()
    }
    return render(request, 'conferences/home.html', context)


# class based views and inherit from ListView  looks for a templatename <app?/<modle?.html  so we need to set template name for class views
class ConferenceListView(ListView):
    model = Conference

    # need to set template = to be home.html in order to work
    template_name = 'conferences/home.html'  # could name template this but we can convert here  <app>/<model>_<viewtype>.html

    # need to set the object = to posts here which the template is looping over
    # or change the template looping variable posts to object
    context_object_name = 'conferences'

    # need to reorder the posts which can be done by setting the variable ordering to -dateposted
    ordering = ['-date_posted']


class UserConferenceListView(ListView):
    model = Conference
    template_name = 'conference/user_conferences.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'conferences'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Conference.objects.filter(author=user).order_by('-created_at')



# This is a typical class view using
class ConferenceDetailView(DetailView):
    model = Conference


class ConferenceCreateView(LoginRequiredMixin, CreateView):
    model = Conference
    fields = ['title', 'content']

# Need to override the form
    def form_valid(self, form):
        # run the form method to the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class ConferenceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Conference
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        conference = self.get_object()
        if self.request.user == conference.author:
            return True
        return False


class ConferenceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Conference
    success_url = '/'

    # Function to make sure author is the registered user to do the deleting
    def test_func(self):
        conference = self.get_object()
        if self.request.user == conference.author:
            return True
        return False

def about(request):
    return render(request, 'conferences/about.html', {'title': 'About'})

