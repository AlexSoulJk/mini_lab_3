from fastapi import FastAPI
import response as r


app = FastAPI()

@app.get("/profile")
def get_profile(steamid: str):
    return r.get_profile(steamid=steamid)

@app.get("/list_friends")
def get_list_friends(steamid: str):
    return r.get_friend_list(steamid=steamid)

@app.get("/game_list")
def get_profile(steamid: str):
    return r.get_game_list(steamid=steamid)




