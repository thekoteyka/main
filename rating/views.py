from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import RateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import Rating, Subject
from django.urls import reverse
from django.views.generic.edit import FormMixin
from .forms import SimpleForm


# Create your views here.

class RatingsDetailView(DetailView):
    model = Subject
    template_name = 'rating/rating_detail.html'

class RatingListView(ListView):
    model = Subject
    paginate_by = 2
    context_object_name = 'rating_objects'
    template_name = 'rating/rating_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_content'] = "Foo"
        return context

class RatingEntryListView(ListView):
    template_name = 'rating/rating_by_name.html'
    context_object_name = 'rating_name_objects'

    def get_queryset(self):
        return Subject.objects.filter(name=self.kwargs['name'])

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

class RatingDetailView(FormMixin, DetailView):
    model = Subject
    template_name = 'rating/rating_detail.html'
    form_class = RateForm

    def get_success_url(self) -> str:
        return reverse('main')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            user = request.user
            rating = Rating(user=user, rate=form.data['rate'])
            rating.save()
            self.object.rating.add(rating)
            self.object.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)