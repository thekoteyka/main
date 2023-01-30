from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import SimpleForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Rating

# Create your views here.

class RatingListView(ListView):
    model = Rating

@method_decorator(login_required, name='dispatch')
class SimpleFormView(View):
    form_class = SimpleForm
    initial = {'foo': 'initial value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
        
        return render(request, self.template_name, {'form': form})


class SimpleView(View):
    name = 'nameeeeee'

    def get(self, request):
        return HttpResponse(f'Hi, {self.name}')

class Foo(SimpleView):
    name = 'Foo'