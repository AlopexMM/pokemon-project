from main import app

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/health/database")
def database_health_check():
    return {"status": "ok"}