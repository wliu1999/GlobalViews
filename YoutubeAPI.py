import os
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def GetTopFive(code, category, numVideos):
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
        part="snippet", chart="mostPopular", regionCode=code, maxResults = numVideos, videoCategoryId = category
    )
    else:
        request = youtube.videos().list(
        part="snippet", chart="mostPopular", regionCode=code, maxResults = numVideos
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
            j = 0
            for tag in item["snippet"]["tags"]:
                if j >= 3:
                    tags = tags[0:len(tags) - 2]
                    break
                tags = tags + tag + ", "
                j = j + 1
            VideoInformation[i].append(tags)
        else:
            VideoInformation[i].append("No tags")
        VideoInformation[i][2] = VideoInformation[i][2][0:200] + "..."
        i = i + 1


    if category != "zero":
        request = youtube.videos().list(
        part="statistics", chart="mostPopular", regionCode=code, maxResults = numVideos, videoCategoryId = category
    )
    else:
        request = youtube.videos().list(
        part="statistics", chart="mostPopular", regionCode=code, maxResults = numVideos
    )
    response = request.execute()

    i = 0
    for item in response["items"]:
        VideoInformation[i].append(item["statistics"]["viewCount"])
        VideoInformation[i].append(item["statistics"]["likeCount"])
        VideoInformation[i].append(item["statistics"]["dislikeCount"])
        VideoInformation[i].append(item["statistics"]["commentCount"])
        i = i + 1

    return VideoInformation
