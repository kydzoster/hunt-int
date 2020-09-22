from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Testament


# everyone can view a testimony
class TestamentListView(ListView):
    model = Testament
    template_name = 'testament_list.html'


# everyone can view a testimony, but only registered users can add content
class TestamentDetailView(LoginRequiredMixin, DetailView):
    model = Testament
    template_name = 'testament_detail.html'
    login_url = 'login'


# only user who created a testimony can edit it
class TestamentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Testament
    fields = ('title', 'body',)
    template_name = 'testament_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# only user who created a testimony can delete it
class TestamentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Testament
    template_name = 'testament_delete.html'
    success_url = reverse_lazy('testament_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# this will create a new testament by a current user
class TestamentCreateView(LoginRequiredMixin, CreateView):
    model = Testament
    template_name = 'testament_add.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
