
from django.shortcuts import render


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


@login_required
def advert_new(request):
    if request.method == "POST":
        form = AdvertForm(request.POST)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.author = request.user
            # post.published_date = timezone.now()
            advert.save()
            return redirect('advert.views.advert_detail', pk=advert.pk)
    else:
        form = AdvertForm()
    return render(request, 'advert/advert_edit.html', {'form': form})


@login_required
def advert_edit(request, pk):
    advert = get_object_or_404(Advert, pk=pk)
    if request.method == "POST":
        form = AdvertForm(request.POST, instance=advert)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.author = request.user
            advert.published_date = timezone.now()
            advert.save()
            return redirect('advert.views.advert_detail', pk=advert.pk)
    else:
        form = AdvertForm(instance=advert)
    return render(request, 'advert/advert_edit.html', {'form': form})


@login_required
def advert_draft_list(request):
    adverts = Advert.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'advert/adverts_draft_list.html', {'adverts': adverts})


@login_required
def advert_publish(request, pk):
    advert = get_object_or_404(Advert, pk=pk)
    advert.publish()
    return redirect('advert.views.advert_detail', pk=pk)


@login_required
def advert_remove(request, pk):
    advert = get_object_or_404(Advert, pk=pk)
    advert.delete()
    return redirect('advert.views.advert_list')


@login_required
def advert_check_expired(request, pk):
    advert = get_object_or_404(Advert, pk=pk)
    advert.check_expired();
    return redirect('advert.views.advert_list')





