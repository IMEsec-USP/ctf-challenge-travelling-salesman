import falcon
import json
from utils.data_parser import parse_cities
from checker.check_travel import is_valid_travel, calculate_distance, is_good_travel
from data.flag import FLAG

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
        
        if not is_good_travel(distance):
            res.status = falcon.HTTP_400
            res.body = f'Desculpe... Miguel não está disposto a tomar um caminho tão longo!\nSua distância foi de {distance}'.encode('utf-8')
            return

        res.status = falcon.HTTP_200
        res.body = FLAG.encode('utf-8')