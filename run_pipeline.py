import click
from pipelines.training_pipeline import ml_pipeline
import mlflow


@click.command()
def main():
    """
    Run the ML pipeline and start the MLflow UI for experiment tracking.
    """
    # Run the pipeline
    run = ml_pipeline()

    # Get the MLflow tracking URI (default is ./mlruns)
    tracking_uri = mlflow.get_tracking_uri()

    print(
        "Now run \n "
        f"    mlflow ui --backend-store-uri '{tracking_uri}'\n"
        "To inspect your experiment runs within the mlflow UI.\n"
        "You can find your runs tracked within the experiment."
    )


if __name__ == "__main__":
    main()
