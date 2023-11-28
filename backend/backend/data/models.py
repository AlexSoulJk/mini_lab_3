from backend.backend.response import response as r


class SteamGame:
    name: str = "-"
    playtime: str = "-"
    img_icon_url: str = "-"
    rtime_last_played: str = "-"

    def __init__(self, name, playtime, img_icon_url, rtime_last_played):
        self.name = name
        self.playtime = playtime
        self.img_icon_url = img_icon_url
        self.rtime_last_played = rtime_last_played

    def print(self):
        print(f"name: {self.name}\n"
              f"playtime: {self.playtime}\n"
              f"last played: {self.rtime_last_played}\n")


class SteamProfile:
    profileurl: str = "-"
    real_name: str = "-"
    personaname: str = "-"
    timecreated: str = "-"
    avatarfull: str = "-"
    list_of_games: [SteamGame] = None
    steamid: str = "-"
    list_of_friends: [int] = None

    def print(self):
        print(f"name: {self.personaname}\n"
              f"real_name: {self.real_name}\n"
              f"url: {self.profileurl}\n"
              f"time_created: {self.timecreated}")

    def print_list_games(self):
        for game in self.list_of_games:
            game.print()

    def __init__(self, steamid):
        self.steamid = steamid
        profile = r.steam_user_info(steamid)['response']['players'][0]
        self.profileurl = str(profile.get('profileurl', "-"))
        self.real_name = str(profile.get('realname', "-"))
        self.personaname = str(profile.get('personaname', "-"))
        self.timecreated = str(profile.get('timecreated', "-"))
        self.avatarfull = str(profile.get('avatarfull', "-"))
        self.list_of_games = self.get_game_list()
        self.list_of_friends = self.get_friend_list()

    def get_game_list(self) -> [SteamGame]:
        res = []
        games = r.steam_list_of_games(self.steamid)['response']['games']
        for game in games:
            res.append(SteamGame(name=str(game.get('name', "-")),
                                 playtime=str(game.get('playtime_forever', "-")),
                                 img_icon_url=str(game.get('img_icon_url', "-")),
                                 rtime_last_played=str(game.get('rtime_last_played', "-"))))
        return res


    def get_friend_list(self) -> [int]:
        data_dict = r.steam_user_friends_list(int(self.steamid))["friendslist"]["friends"]
        newList = []
        for info in data_dict:
            newList.append(info['steamid'])
        return newList

    def take_friend_list(self) -> []:
        res = []
        for sid in self.list_of_friends:
            res.append(SteamProfile(steamid=sid))
        return res



def get_profiles(steamid=[76561197960435530]) -> [SteamProfile]:
    res = []
    url_profiles = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?" \
                   f"key={r.api}&steamids="

    list_ids = [steamid[i:i + 100] for i in range(0, len(steamid), 100)]

    for ids in list_ids:
        profiles = r.get_response(url_profiles + ",".join(map(str, ids)))['response']['players']
        for profile in profiles:
            res.append(SteamProfile(profileurl=str(profile.get('profileurl', "-")),
                                    real_name=str(profile.get('realname', "-")),
                                    personaname=str(profile.get('personaname', "-")),
                                    timecreated=str(profile.get('timecreated', "-")),
                                    avatarfull=str(profile.get('avatarfull', "-"))))
    return res







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
