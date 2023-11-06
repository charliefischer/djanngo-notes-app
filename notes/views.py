from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes

# Create your views here.

class NotesDeleteView(DeleteView):
  model = Notes
  success_url = '/smart/notes'
  template_name = 'notes/note_delete.html'


class NotesCreateView(CreateView):
  model = Notes
  success_url = '/smart/notes'
  form_class = NotesForm

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
  model = Notes
  context_object_name = 'notes'
  template_name = 'notes/notes_list.html'
  login_url = '/login'

  def get_queryset(self):
    return self.request.user.notes.all()

class NotesDetailView(DetailView):
  model = Notes
  context_object_name = 'note'
  template_name = 'notes/note_detail.html'

class UpdateView(UpdateView):
  model = Notes
  success_url = '/smart/notes'
  form_class = NotesForm



# def list(request):
#   all_notes = Notes.objects.all()
#   return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def detail(request, pk):
#   try:
#     note = Notes.objects.get(pk=pk)
#   except Notes.DoesNotExist:
#     raise Http404("note doesn't existt")
#   return render(request, 'notes/note_detail.html', {'note': note})
