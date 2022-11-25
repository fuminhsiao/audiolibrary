from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from amplifiers.models import Amplifier
from amplifiers.forms import AmplifierForm
from home.owner import OwnerListView, OwnerDetailView


# Create your views here.

class AmplifierListView(OwnerListView):
    model = Amplifier
    template_name = "amplifier/index.html"


class AmplifierDetailView(OwnerDetailView):
    model = Amplifier
    template_name = "amplifier/detail.html"


class AmplifierCreateView(View):
    template_name = "amplifier/forms.html"
    success_url = reverse_lazy('amplifiers:all')

    def get(self, request, pk=None):
        form = AmplifierForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = AmplifierForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        amplifier = form.save(commit=False)
        amplifier.save()
        return redirect(self.success_url)

def stream_file(request, pk):
    pic = get_object_or_404(Amplifier, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response