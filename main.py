from fastapi import FastAPI, HTTPException
import response as r


app = FastAPI()

@app.get("/profile")
def get_profile(steamid: str):
    try:
        tr = r.get_profile(steamid=steamid)
    except Exception as ex:
        raise HTTPException(status_code=404,
                            detail="Failed to fetch profile data from the API.")
    return tr


@app.get("/list_friends")
def get_list_friends(steamid: str):
    try:
        tr = r.get_friend_list(steamid=steamid)
    except Exception as ex:
        raise HTTPException(status_code=404,
                            detail="Failed to fetch list friends data from the API.")
    return tr


@app.get("/game_list")
def get_game_list(steamid: str):
    try:
        tr = r.get_game_list(steamid=steamid)
    except Exception as ex:
        raise HTTPException(status_code=404,
                            detail="Failed to fetch game list data from the API")
    return tr




