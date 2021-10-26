from fastapi import FastAPI, Depends
from database import Base, engine

# from routers import vessels

Base.metadata.create_all(engine)


app = FastAPI(title="Lean and Green API platform", openapi_url="/openapi.json")

# app.include_router(vessels.router)


@app.get("/")
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "I am ROOT"}

    if __name__ == "__main__":
        # For debugging
        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port="8001", log_level="debug")
