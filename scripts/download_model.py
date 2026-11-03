import mlflow
import os

# MLflow config
MLFLOW_URI = os.getenv("MLFLOW_URI")
EXPERIMENT_NAME = os.getenv("EXPERIMENT_NAME")

mlflow.set_tracking_uri(MLFLOW_URI)

local_path = mlflow.artifacts.download_artifacts(
    artifact_uri=f"models:/{EXPERIMENT_NAME}/latest",
    dst_path="./models"
)

print(f"Modelo descargado en: {local_path}")