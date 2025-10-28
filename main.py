from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

@app.get("/")
async def hello_world():
    """
    Rota principal que retorna uma mensagem de Hello World
    """
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    """
    Rota de health check para verificar se a aplicação está funcionando
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
