
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from .models import Advert
from django.shortcuts import render, get_object_or_404
from .forms import AdvertForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render






def advert_list(request):
    ads_list = Advert.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    paginator = Paginator(ads_list, 10)

    page = request.GET.get('page')
    try:
        adverts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        adverts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        adverts = paginator.page(paginator.num_pages)

    return render(request, 'advert/advert_list.html', {'adverts': adverts})


def advert_detail(request, pk):
    advert = get_object_or_404(Advert, pk=pk)

    # comments_list = post.comments.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    #
    # paginator = Paginator(comments_list, 10)
    #
    # page = request.GET.get('page')
    # try:
    #     comments = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     comments = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     comments = paginator.page(paginator.num_pages)

    return render(request, 'advert/advert_detail.html', {'advert': advert})






