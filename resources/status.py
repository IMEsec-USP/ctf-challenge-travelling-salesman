import falcon
from model.best_distance import BestDistance

class Status:

    def on_get(self, req, res):
        distance = BestDistance.get()
        res.status = falcon.HTTP_200
        res.data = f'A menor distância encontrada foi de {distance.distance} por {distance.author}.'.encode('utf-8')
