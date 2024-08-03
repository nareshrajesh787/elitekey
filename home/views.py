from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class EntryListView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        entries = Entry.objects.filter(author=request.user).order_by('-date')
        form = EntryForm()
        return render(request, self.template_name, {'entries': entries, 'form': form})

    def post(self, request, *args, **kwargs):
        form = EntryForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
        else:
            entries = Entry.objects.filter(author=request.user).order_by('-date')
            return render(request, self.template_name, {'entries': entries, 'form': form})

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    template_name = 'home/update.html'
    fields = ['website', 'username', 'password']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    template_name = 'home/delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class EntryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Entry
    template_name = "home/detail.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    get_object_or_404
