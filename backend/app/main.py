from fastapi import FastAPI

app = FastAPI(
    title="CloudBackup Manager",
    description="Centralized backup management and monitoring platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "application": "CloudBackup Manager",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
    }
