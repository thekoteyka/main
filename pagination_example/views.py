from django.shortcuts import render
from rating.models import Rating

# Create your views here.

def pagination_view(request, *args, **kwargs):
    qs = Rating.objects.all()
    page = int(request.GET.get('page', 1))
    paginate_by = 5
    qs_to_show = qs[paginate_by*(page-1):paginate_by*page]
    return render(request, 'pagination_example/pagination_example.html', {'data_list': qs_to_show, "next_page": page+1, "previous_page": page-1 or 1})