# youtube-search
Youtube search application where youtube videos of given keyword videos will be fetched and shown.

# How to start
-> The poject is dockerized. so need to build the project using below command
```sudo docker-compose up --detach --build ```

-> Start the project
```sudo docker-compose up ```

## Configuration

-> search keyword configuration needs to be done at  ```youtube_search/search/config.py ```

```
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

SEARCH_KEYWORD = 'football'
MAX_RESULTS = 40

#sample AUTH_KEY= 'AKDJhJEOIRluih$%kjhjkfdytJKKGFDS'
AUTH_KEY = '---------Add key here---------'

```
-> After configuration is changed, restart the project

-> Videos list will be shown at ``` http://localhost:8000/videos/fetch/ ```
