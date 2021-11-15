import os
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def GetTopFive():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    API_KEY = os.getenv("API_KEY")

    # Create Youtube API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    request = youtube.videos().list(
        part="snippet",
        chart="mostPopular",
        regionCode="us"
    )
    response = request.execute()

    VideoInformation = []
    i = 0
    for item in response["items"]:
        VideoInformation.append([])
        VideoInformation[i].append(item["snippet"]["title"])
        VideoInformation[i].append("https://www.youtube.com/watch?v=" + item["id"])
        VideoInformation[i].append(item["snippet"]["thumbnails"]["medium"]["url"])
        i = i + 1



    return VideoInformation
