from django.shortcuts import render
from .models import Granpa

# django documents prefetch: https://docs.djangoproject.com/en/1.7/ref/models/querysets/
# 参考：http://stackoverflow.com/questions/9176430/django-does-prefetch-related-follow-reverse-relationship-lookup

# prefetch
def index1(request):

    granpa_list = Granpa.objects.all().prefetch_related('papas__children')

    return render(request, 'granpa.html', {'granpa_list': granpa_list})

# not prefetch
def index2(request):

    granpa_list = Granpa.objects.all()

    return render(request, 'granpa.html', {'granpa_list': granpa_list})
