from fastapi import FastAPI, status, HTTPException

DATABASE = {
    1: {"name": "iron_man_1", "description": "the rise or mr.tony", "rating": 8},
    2: {"name": "iron_man_2", "description": "tony & rhodey fight", "rating": 7},
    3: {"name": "iron_man_3", "description": "multiple iron mechs", "rating": 6},
    4: {"name": "avengers_1", "description": "avengers, assemble!", "rating": 9},
    5: {"name": "avengers_2", "description": "ultron attacks fast", "rating": 10},
}

app = FastAPI()


# GET
@app.get("/movie")
def get_movie_by_id(movie_id: int):
    try:
        return DATABASE[movie_id]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item not found")

# POST
@app.post("/", status_code=status.HTTP_201_CREATED)
def create_movie(name: str, desc: str, rating: int):
    obj = {"name": name, "description": desc, "rating": rating}
    key = len(DATABASE) + 1
    DATABASE[key] = obj
    return {"message": "movie added"}

