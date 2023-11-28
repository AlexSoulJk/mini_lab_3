import requests
import os
from dotenv import load_dotenv


load_dotenv()
api = os.getenv('steam_api')


def get_response(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Ошибочка при запросе:{response.status_code}")

def steam_user_info(steamid):
    url_user_profile = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?" \
                       f"key={api}&steamids={steamid}"
    return get_response(url_user_profile)

def steam_user_friends_list(steamid):
    url_friend_list = f"https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?" \
                      f"key={api}&steamid={steamid}&relationship=friend&format=json"
    return get_response(url_friend_list)

def steam_list_of_games(steamid):
    url_game_list = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?" \
                    f"key={api}&steamid={steamid}&include_appinfo=true&format=json"

    return get_response(url_game_list)
# {'response':
#      {'game_count': 26, 'games':
#          [
#              {'appid': 4000, 'playtime_forever': 111, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535433009, 'playtime_disconnected': 0},
#              {'appid': 550, 'playtime_forever': 76, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535391044, 'playtime_disconnected': 0},
#              {'appid': 105600, 'playtime_forever': 7665, 'playtime_windows_forever': 6919, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1673645076, 'playtime_disconnected': 0},
#              {'appid': 236390, 'playtime_forever': 18, 'playtime_windows_forever': 1, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1589627474, 'playtime_disconnected': 0},
#              {'appid': 203160, 'playtime_forever': 81, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535391349, 'playtime_disconnected': 0},
#              {'appid': 252490, 'playtime_forever': 274, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1514650289, 'playtime_disconnected': 0},
#              {'appid': 700580, 'playtime_forever': 0, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 0, 'playtime_disconnected': 0},
#              {'appid': 252950, 'playtime_forever': 177, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1540563177, 'playtime_disconnected': 0},
#              {'appid': 271590, 'playtime_forever': 4600, 'playtime_windows_forever': 690, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1626437633, 'playtime_disconnected': 0},
#              {'appid': 304930, 'playtime_forever': 1225, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1527420865, 'playtime_disconnected': 0},
#              {'appid': 323850, 'playtime_forever': 104, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1529761773, 'playtime_disconnected': 0},
#              {'appid': 730, 'playtime_forever': 55900, 'playtime_windows_forever': 14244, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1694289225, 'playtime_disconnected': 0},
#              {'appid': 400250, 'playtime_forever': 81, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535391349, 'playtime_disconnected': 0},
#              {'appid': 489220, 'playtime_forever': 76, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535391045, 'playtime_disconnected': 0},
#              {'appid': 307780, 'playtime_forever': 65, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535388169, 'playtime_disconnected': 0},
#              {'appid': 540900, 'playtime_forever': 58, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535389928, 'playtime_disconnected': 0},
#              {'appid': 547960, 'playtime_forever': 76, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535391044, 'playtime_disconnected': 0},
#              {'appid': 550650, 'playtime_forever': 3251, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1564139716, 'playtime_disconnected': 0},
#              {'appid': 444200, 'playtime_forever': 75, 'playtime_windows_forever': 1, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1589627473, 'playtime_disconnected': 0},
#              {'appid': 578080, 'playtime_forever': 6523, 'playtime_windows_forever': 85, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1581789332, 'playtime_disconnected': 0},
#              {'appid': 586380, 'playtime_forever': 57, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535389928, 'playtime_disconnected': 0},
#              {'appid': 601220, 'playtime_forever': 114, 'playtime_windows_forever': 114, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1589828804, 'playtime_disconnected': 0},
#              {'appid': 728540, 'playtime_forever': 132, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1560147450, 'playtime_disconnected': 0},
#              {'appid': 203770, 'playtime_forever': 151, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535449632, 'playtime_disconnected': 0},
#              {'appid': 222880, 'playtime_forever': 58, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 1535389928, 'playtime_disconnected': 0},
#              {'appid': 992310, 'playtime_forever': 0, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 0, 'playtime_disconnected': 0}
#          ]}}



##Example of response steam_user_info
# {'response':
#      {'players':
#           [
#               {'steamid': '76561198287722531',
#                'communityvisibilitystate': 3,
#                'profilestate': 1,
#                'personaname': 'Ricky',
#                'commentpermission': 1,
#                'profileurl': 'https://steamcommunity.com/profiles/76561198287722531/',
#                'avatar': 'https://avatars.steamstatic.com/ad38e959ffc921db1a5ddc9b69f9e88ef984731c.jpg',
#                'avatarmedium': 'https://avatars.steamstatic.com/ad38e959ffc921db1a5ddc9b69f9e88ef984731c_medium.jpg',
#                'avatarfull': 'https://avatars.steamstatic.com/ad38e959ffc921db1a5ddc9b69f9e88ef984731c_full.jpg',
#                'avatarhash': 'ad38e959ffc921db1a5ddc9b69f9e88ef984731c',
#                'lastlogoff': 1700697264,
#                'personastate': 0,
#                'realname': 'Just man)',
#                'primaryclanid': '103582791440448676',
#                'timecreated': 1456493725,
#                'personastateflags': 0}
#           ]
#      }
# }
