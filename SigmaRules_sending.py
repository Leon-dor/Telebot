import requests


def sigma_rules():
    sigma_rules_id = "UCT0OARvv0-VeRZMUNW_e9hw"
    sigma_rules_api = "AIzaSyCIty0xJCF8bp7NK9GrGkaCdCsj99D_mCM"
    # api_token = "6156730475:AAF1Ss2x0V72KYYITKaDE1_mOA9cROuBUxg"

    #
    # def message_sending():
    #     requests.get(f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'.format(API_TOKEN), params=dict(
    #        chat_id='@my_channel_name',
    #        text='Hello world!'
    #                 )
    #             )

    endpoint = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": sigma_rules_id,
        "maxResults": 6,
        "order": "date",
        "type": "video",
        "key": sigma_rules_api
    }

    response = requests.get(endpoint, params=params)
    video_id = response.json()["items"][0]["id"]["videoId"]
    endpoint_video = f"https://www.youtube.com/shorts/"

    return f"{endpoint_video}{video_id}"
