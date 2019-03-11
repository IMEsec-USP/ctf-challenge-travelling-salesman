from falcon import HTTP_200

class HealthCheck:

    def on_get(self, req, res):
        res.status = HTTP_200