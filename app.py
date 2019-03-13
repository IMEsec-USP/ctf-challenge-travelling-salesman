import falcon

from resources.healthcheck import HealthCheck
from resources.check import Check

def create():
    api = application = falcon.API(middleware = [
    ])

    healthcheck_resource = HealthCheck()
    check_resource = Check()

    api.add_route('/_healthcheck', healthcheck_resource)
    api.add_route('/check', check_resource)
    return api

app = application = create()
