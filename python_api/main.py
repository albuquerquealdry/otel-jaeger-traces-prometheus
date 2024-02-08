import logging
import os
import random
import time
from typing import Optional

import httpx
import uvicorn
from fastapi import FastAPI, Response, HTTPException

EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 8000)

TARGET_ONE_SVC = os.environ.get("TARGET_ONE_SVC", "localhost:8000")
TARGET_TWO_SVC = os.environ.get("TARGET_TWO_SVC", "localhost:8000")

app = FastAPI()

@app.get("/pikachu")
async def read_root():
    logging.error("Hello World")
    return {"response": "Pika pika! Welcome to the world of Pokemon!"}

@app.get("/charizard/{move}")
async def read_item(move: str, q: Optional[str] = None):
    logging.error("charizard")
    return {"move": move, "q": q, "response": "Charizard used Flamethrower! It's super effective!"}

@app.get("/bulbasaur")
async def io_task():
    time.sleep(1)
    logging.error("io task")
    return {"response": "Bulbasaur used Sleep Powder! Welcome to the lush jungle of async responses!"}

@app.get("/squirtle")
async def cpu_task():
    for i in range(1000):
        _ = i * i * i
    logging.error("cpu task")
    return {"response": "Squirtle used Withdraw! CPU bound task finish! Surrounded by a protective shell of computing power!"}

@app.get("/random_status/mewtwo")
async def random_status(response: Response):
    response.status_code = random.choice([200, 200, 300, 400, 500])
    logging.error("random status")
    return {"response": "Mewtwo is pondering its status... Response status varies like the power of Psystrike!"}

@app.get("/random_sleep/ditto")
async def random_sleep(response: Response):
    time.sleep(random.randint(0, 5))
    logging.error("random sleep")
    return {"response": "Ditto is transforming... Smells like nap time... or a random Pokemon encounter!"}

@app.get("/error_test/meowth")
async def error_test(response: Response):
    logging.error("got error!!!!")
    raise ValueError("Team Rocket's Meowth used Pay Day... but encountered a ValueError instead!")

@app.get("/chain/eevee")
async def chain(response: Response):
    logging.info("Chain Start")

    async with httpx.AsyncClient() as client:
        await client.get(
            "http://localhost:8000/pikachu",
        )
    async with httpx.AsyncClient() as client:
        await client.get(
            f"http://{TARGET_ONE_SVC}/bulbasaur",
        )
    async with httpx.AsyncClient() as client:
        await client.get(
            f"http://{TARGET_TWO_SVC}/squirtle",
        )
    
    # Excluding the last method
    logging.info("Chain Finished (excluding the last method)")
    return {"response": "Eevee is evolving... Master of chaining requests (excluding the last method)!"}

@app.get("/the_best_pokemon/{pokemon_name}")
async def the_best_pokemon(pokemon_name: str):
    if pokemon_name.lower() != "mewtwo":
        raise HTTPException(status_code=400, detail="Sorry but this is far from being the best Pokemon!")
    return {"response": f"The best Pokemon is undoubtedly Mewtwo! Its power is unmatched!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT)
