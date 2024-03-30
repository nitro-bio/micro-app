import sqlite3

from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse("static/index.html")


# anytime we get /assets/*, we want to serve the static files in the assets folder
# used in prod to serve react build
@app.get("/assets/{file_path}")
async def static_assets(file_path: str):
    return FileResponse(f"static/assets/{file_path}")


@app.get("/api/users")
async def fetch_users():
    # get users from db
    conn = get_db_connection()
    with conn:
        users = conn.execute("SELECT * FROM Users").fetchall()
        return {"users": users}


conn = None


def get_db_connection():
    global conn
    if conn is None:
        conn = sqlite3.connect("database.db")
    return conn


def setup_dev_db():
    conn = get_db_connection()
    with conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """
        )

        # Insert dummy data
        users = [
            ("Alice", "alice@example.com"),
            ("Bob", "bob@example.com"),
            ("Charlie", "charlie@example.com"),
        ]

        conn.executemany(
            "INSERT OR IGNORE INTO Users (name, email) VALUES (?, ?)", users
        )
    print("Dev Database setup completed")


setup_dev_db()
