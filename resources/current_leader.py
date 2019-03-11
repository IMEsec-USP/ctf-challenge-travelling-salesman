from model.best_distance import BestDistance
import hashlib
import falcon
import json

class CurrentLeader:

    def on_get(self, req, res):
        best_distance = BestDistance.get_all()
        team_list = [{
            'team': dist.author,
            'check': hashlib.md5(dist.author.encode('utf-8')).hexdigest()
        } for dist in best_distance]
        
        res.status = falcon.HTTP_200
        res.data = json.dumps(team_list).encode('utf-8')