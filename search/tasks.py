from celery import shared_task
from .search_keyword import SearchVideo
from .config import *
import datetime

@shared_task(name="search.tasks.fetch_youtube_videos", queue="youtube_search")
def fetch_youtube_videos():
    """
    Task to asynchrnously run the search api call and store the videos
    """
    published_after = datetime.datetime.now() - datetime.timedelta(minutes=300)
    published_after = datetime.datetime.strftime(published_after,"%Y-%m-%dT%H:%M:%SZ")
    search_class = SearchVideo(SEARCH_KEYWORD, MAX_RESULTS, published_after, AUTH_KEY)

    search_class.get_videos()
