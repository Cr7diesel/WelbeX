from fastapi import FastAPI


app = FastAPI()


@app.post('/api/routes')
async def create_routes():
    ...


@app.get('/api/routes/{id}')
async def get_routes_by_id():
    ...

