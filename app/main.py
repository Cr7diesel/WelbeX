import csv

from fastapi import FastAPI, UploadFile, File, HTTPException, responses

from app.base_models import Routes, SessionLocal
from app.models import Route
from app.utils import calculate_optimal_route

app = FastAPI()


@app.get("/api/routes/{route_id}", response_model=Route)
def get_route(route_id: int):
    try:
        with SessionLocal() as db:
            route = db.query(Routes).filter(Routes.id == route_id).first()
            return route
    except HTTPException as e:
        return responses.JSONResponse({"error": "Route not found"}, e.status_code)


@app.post("/api/routes", response_model=Route)
def create_route_from_csv(file: UploadFile = File('example.csv')):
    try:
        points = []
        content = file.file.read().decode("utf-8")

        with open(content, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                lat = float(row[0])
                lng = float(row[1])
                point = {'lat': lat, 'lng': lng}
                points.append(point)

        optimal_route = Routes(points=calculate_optimal_route(points))
        with SessionLocal() as db:
            db.add(optimal_route)
            db.commit()
        return optimal_route
    except HTTPException as e:
        return responses.JSONResponse({"error": "Route not found"}, e.status_code)


