from xgboost import XGBClassifier
import os
import logging

logger = logging.getLogger(__name__)

MODEL_DIRECTORY = os.path.join(os.getcwd(), "client")

def run_prediction(feature):
    xgb_clf = XGBClassifier()
    xgb_clf.load_model(os.path.join(MODEL_DIRECTORY, "xgb.model"))
    return ''


