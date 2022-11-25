from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from speakers.models import Speaker, Comment, SpeakerUser
from speakers.forms import SpeakerForm, CommentForm
from django.contrib.auth.models import User
from home.owner import OwnerListView, OwnerDetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class MemberDetailView(DetailView):
    model = User
    template_name = "membership/membership.html"

    def get(self, request, pk):
        x = User.objects.get(id=pk)
        context = {'user': x}
        return render(request, self.template_name, context)
