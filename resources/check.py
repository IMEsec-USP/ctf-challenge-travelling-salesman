import falcon
import json
from utils.data_parser import parse_cities
from checker.check_travel import is_valid_travel, calculate_distance
from model.best_distance import BestDistance

cities_file = 'data/texas.txt'

class Check:

    def __init__(self):
        with open(cities_file) as f:
            self.cities = parse_cities(f)

    def on_post(self, req, res):
        try:
            body = json.load(req.bounded_stream)
            cities = body['cities']
            author = body['author']

        except KeyError as e:
            res.status = falcon.HTTP_400
            res.body = e.__repr__().encode('utf-8')
            return
        except json.decoder.JSONDecodeError as e:
            res.status = falcon.HTTP_400
            res.body = 'Bad request: JSON Malformado no corpo da mensagem. Cheque se seu arquivo de cidades está correto!'.encode('utf-8')
            return
        except Exception as e:
            res.status = falcon.HTTP_500
            res.body = str(e).encode('utf-8')
            return

        if not isinstance(cities, list): 
            res.status = falcon.HTTP_400
            res.body = b'Erro inesperado. Reporte para @pedro823 no telegram.'
            return

        if not is_valid_travel(self.cities, cities):
            res.status = falcon.HTTP_400
            res.body = 'A viagem não é válida, lembre-se: é necessário passar por todas as cidades apenas 1 vez.'.encode('utf-8')
            return

        distance = calculate_distance(self.cities, cities)
        
        best_distance = BestDistance.get()

        if best_distance.distance < distance:
            res.status = falcon.HTTP_400
            res.body = f'Oh não! A melhor distância é {best_distance.distance} por {best_distance.author}. Sua distância foi {distance}.'.encode('utf-8')
            return
        
        # We didn't make enough operations to lose precision
        if best_distance.distance == distance:
            all_authors = [i.author for i in BestDistance.get_all()]
            if author in all_authors:
                res.status = falcon.HTTP_400
                res.body = f'Você já está na lista da liderança! A lista é {all_authors}'.encode('utf-8')
                return

            BestDistance.append(distance, author)
            res.status = falcon.HTTP_200
            res.body = f'Você alcançou o melhor atual. A distância foi de {distance}. Você foi adicionado na lista da liderança.'.encode('utf-8')
            return

        BestDistance.set(distance, author)

        res.status = falcon.HTTP_200
        res.body = f'Ótimo! Você é o novo líder do placar com uma distância de {distance}.'.encode('utf-8')