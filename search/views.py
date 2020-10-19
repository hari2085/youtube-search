from django.shortcuts import render
from search.models import Videos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def fetch_youtube_videos(request):
    """
    Single get api to to get all the videos and also satisfying the search condition 
    """
    search_strings = request.GET.get('search', '').split(' ')
    videos_list = Videos.objects.none()
    for string in search_strings:
        videos_list = videos_list | Videos.objects.distinct().filter(title__icontains=string)
    
    videos_list = videos_list.order_by('-published').distinct()
    page = request.GET.get('page', 1)

    paginator = Paginator(videos_list, 50)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    return render(request, 'videos_list.html', {'videos': videos})