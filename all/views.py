from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from all.forms import ContactModelForm
from all.models import PortfolioModel


class PortfolioView(View):
    def get(self, request):
        portfolio = PortfolioModel.objects.all()
        return render(request, 'index.html', {'context': portfolio})

    def post(self, request):
        form = ContactModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('all:main'))
        return render(request, 'index.html')
