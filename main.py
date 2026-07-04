from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

FILE_NAME = "bookings.csv"

@app.get("/")
def home():
    return {"message": "Hotel Management System Running"}

@app.post("/book")
def book_room(name: str, room: str):

    new_data = {
        "Customer Name": [name],
        "Room Type": [room]
    }

    df_new = pd.DataFrame(new_data)

    # If file exists, append data
    if os.path.exists(FILE_NAME):
        df_old = pd.read_csv(FILE_NAME)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(FILE_NAME, index=False)

    return {"message": "Booking Successful"}