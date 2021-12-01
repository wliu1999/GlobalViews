import os
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def GetTopFive(code, category):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    API_KEY = os.getenv("API_KEY")

    # Create Youtube API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY
    )

    if category != "zero":
        request = youtube.videos().list(
        part="snippet", chart="mostPopular", regionCode=code, maxResults = 5, videoCategoryId = category
    )
    else:
        request = youtube.videos().list(
        part="snippet", chart="mostPopular", regionCode=code, maxResults = 5
    )
    response = request.execute()

    VideoInformation = []
    i = 0
    for item in response["items"]:
        VideoInformation.append([])
        VideoInformation[i].append(item["snippet"]["title"])
        VideoInformation[i].append("https://www.youtube.com/embed/" + item["id"])
        VideoInformation[i].append(item["snippet"]["description"])
        if "tags" in item["snippet"]:
            tags = ""
            for tag in item["snippet"]["tags"]:
                tags = tags + tag + " "
            VideoInformation[i].append(tags)
        else:
            VideoInformation[i].append("No tags")
        VideoInformation[i][2] = VideoInformation[i][2][0:200] + "..."
        i = i + 1
    

    request = youtube.videoCategories().list(
        part="snippet", regionCode=code
       
    )
    response = request.execute()

    print(response)
    return VideoInformation
