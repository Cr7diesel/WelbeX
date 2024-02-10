import csv
import math
from itertools import permutations


def calculate_optimal_route(points: list[dict]) -> list[dict]:
    if len(points) == 0:
        return []

    # Функция для вычисления расстояния между двумя точками
    def distance(point1, point2):
        return math.sqrt((point1['lat'] - point2['lat']) ** 2 + (point1['lng'] - point2['lng']) ** 2)

    # Генерируем все возможные перестановки точек
    permutations_list = list(permutations(points))

    # Инициализируем переменные для хранения оптимального маршрута и его длины
    optimal_route = None
    optimal_distance = float('inf')

    # Вычисляем длину каждого маршрута и выбираем оптимальный
    for route in permutations_list:
        route_distance = sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))

        if route_distance < optimal_distance:
            optimal_distance = route_distance
            optimal_route = route

    return list(optimal_route)


