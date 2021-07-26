from client.aws import run_prediction

class PredictService:

    def __init__(self, data):
        self.data = data
        self.prediction = None

    def get_prediction(self):
        if self.prediction is None:
            self._run_prediction()
        return self.prediction

    def _run_prediction(self):
        self.prediction = run_prediction(self.data)
