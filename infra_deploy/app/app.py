import os
import sys

#sys.path.append(os.getcwd())

from fastapi import FastAPI, status, HTTPException
from infrerence_app import predict
from fastapi.responses import Response

from starlette_exporter import PrometheusMiddleware, handle_metrics
from prometheus_client import Counter
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

TOTAL_COUNTER = Counter("cnt_signal", "cnt of requested to model")

DOWN_COUNTER = Counter("cnt_signal_down", "cnt down signal")
#PCLASS_COUNTER = Counter("pclass", "Number of passengers by class", ["pclass"])
#DOWN_COUNTER = Counter("sell signal", "Number of passengers by class", ["sell"])

@app.get("/")
def health_check() -> dict:
    """Health check"""
    return {"status": "ok"}

@app.get("/test")
def health_check() -> dict:
    """Health check"""
    return {"status test": "ok"}

@app.get(f'/health')
def health() -> Response:
  return Response(status_code=status.HTTP_200_OK)

@app.get(f'/ready')
def ready() -> Response:
  return Response(status_code=status.HTTP_200_OK)

@app.get(f'/startup')
def startup() -> Response:
  return Response(status_code=status.HTTP_200_OK)

@app.get("/predict")
def make_prediction() -> dict:
    """inference model"""

    verdict = predict()
    TOTAL_COUNTER.inc()

    if verdict == 'sell':
      DOWN_COUNTER.inc()

    return {"traide verdict": verdict}
