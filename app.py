import falcon

from resources.status import Status
from resources.healthcheck import HealthCheck
from resources.check import Check
from resources.current_leader import CurrentLeader

def create():
    api = application = falcon.API(middleware = [
    ])

    healthcheck_resource = HealthCheck()
    status_resource = Status()
    check_resource = Check()
    current_leader_resource = CurrentLeader()

    api.add_route('/_healthcheck', healthcheck_resource)
    api.add_route('/status', status_resource)
    api.add_route('/check', check_resource)
    api.add_route('/', current_leader_resource)
    return api

app = application = create()
