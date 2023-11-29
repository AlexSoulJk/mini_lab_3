import requests
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('steam_api')

response_url = f"https://api.steampowered.com/"
img_url = f"http://media.steampowered.com/steamcommunity/public/images/apps/"


def get_response(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Ошибочка при запросе:{response.status_code}")


def steam_user_info(steamid):
    url_user_profile = response_url + "ISteamUser/GetPlayerSummaries/v0002/?" \
                                      f"key={api}&steamids={steamid}"
    return get_response(url_user_profile)


def steam_user_friends_list(steamid):
    url_friend_list = response_url + "ISteamUser/GetFriendList/v0001/?" \
                                     f"key={api}&steamid={steamid}&relationship=friend&format=json"
    return get_response(url_friend_list)


def steam_list_of_games(steamid):
    url_game_list = response_url + "IPlayerService/GetOwnedGames/v0001/?" \
                                   f"key={api}&steamid={steamid}&include_appinfo=true&include_extended_appinfo=true" \
                                   f"&format=json"

    return get_response(url_game_list)


def get_steam_profiles(steamid=[76561197960435530]):
    res = []
    url_profiles = response_url + f"ISteamUser/GetPlayerSummaries/v0002/?key={api}&steamids="

    list_ids = [steamid[i:i + 100] for i in range(0, len(steamid), 100)]

    for ids in list_ids:
        profiles = get_response(url_profiles + ",".join(map(str, ids)))['response']['players']
        for profile in profiles:
            res.append({'profileurl': str(profile.get('profileurl', "-")),
                        'real_name': str(profile.get('realname', "-")),
                        'personaname': str(profile.get('personaname', "-")),
                        'avatarfull': str(profile.get('avatarfull', "-"))})
    return res


def get_friend_list(steamid):
    data_dict = steam_user_friends_list(int(steamid))["friendslist"]["friends"]
    newList = []
    for info in data_dict:
        newList.append(info['steamid'])
    return get_steam_profiles(newList)


def get_game_list(steamid):
    res = []
    games = steam_list_of_games(steamid)['response']['games']
    print(games)
    for game in games:
        icon_hash = str(game.get('img_icon_url', "-"))
        game_id = str(game.get('appid', "-"))
        res.append({'name': str(game.get('name', "-")),
                    'img_icon_url': (img_url + game_id + "/" + icon_hash + ".jpg", "")[
                        icon_hash == "-" or game_id == "-"],
                    'game_id': game_id})
    return res


def get_profile(steamid):
    profile = steam_user_info(steamid)['response']['players'][0]

    res = {'profileurl': str(profile.get('profileurl', "-")),
           'real_name': str(profile.get('realname', "-")),
           'personaname': str(profile.get('personaname', "-")),
           'avatarfull': str(profile.get('avatarfull', "-"))}

    return res
