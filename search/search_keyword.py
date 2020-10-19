from collections import defaultdict
import json
import pandas as pd
from search.request import open_url
from search.config import YOUTUBE_SEARCH_URL

class SearchVideo(object):
    """
    Class that will call the youtube search api and create results 
    to pandas dataframe and bulk upload to database
    """
    def __init__(self, search_term, max_results, published_after, key):
        self.videos = defaultdict(list)
        self.channels = defaultdict(list)
        self.playlists = defaultdict(list)
        self.params = {
                    'q': search_term,
                    'part': 'id,snippet',
                    'maxResults': max_results,
                    'publishedAfter': published_after,
                    'type' : 'video',
                    'key': key
                }

    def load_search_res(self, search_response):
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                self.videos["title"].append(search_result["snippet"]["title"])
                self.videos["description"].append(search_result["snippet"]["description"])
                self.videos["published"].append(search_result["snippet"]["publishedAt"])
                self.videos["video_id"].append(search_result["id"]["videoId"])
                self.videos["channel_title"].append(search_result["snippet"]["channelTitle"])
                self.videos["thumbnail"].append(search_result["snippet"]["thumbnails"]["default"]["url"])


    def get_videos(self):
        url_response = json.loads(open_url(YOUTUBE_SEARCH_URL, self.params))

        self.load_search_res(url_response)

        videos_df = self.create_df()
        self.save_to_model(videos_df)
    
    def create_df(self):
        return pd.DataFrame().from_dict(self.videos)
        
    def save_to_model(self, videos_df):
        from .models import Videos
        entries = []
        for e in videos_df.T.to_dict().values():
            entries.append(Videos(**e))
        
        Videos.objects.bulk_create(entries)
