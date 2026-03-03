"""
NYC Taxi Data Pipeline using dlt with requests

This pipeline extracts NYC taxi data from a paginated REST API and loads it into DuckDB.
The API returns raw JSON arrays, so we use a custom dlt resource with the requests
module to yield pages until an empty page is returned.
"""

import dlt
import requests


BASE_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"


@dlt.resource(name="taxi_data", write_disposition="replace")
def taxi_data_resource():
    """
    Yield NYC taxi records page by page.

    The API uses page-number pagination (?page=1, ?page=2, …) and signals
    the end of data by returning an empty array.
    """
    page = 1
    while True:
        response = requests.get(BASE_URL, params={"page": page}, timeout=30)
        response.raise_for_status()
        records = response.json()

        if not records:
            break

        yield records
        page += 1


def load_taxi_data() -> None:
    """Load NYC taxi data from the REST API into DuckDB."""

    pipeline = dlt.pipeline(
        pipeline_name="taxi_pipeline",
        destination="duckdb",
        dataset_name="nyc_taxi_data",
        dev_mode=True,
    )

    load_info = pipeline.run(taxi_data_resource())

    print(load_info)
    print("\n--- Load Summary ---")
    print(f"Pipeline: {pipeline.pipeline_name}")
    print(f"Destination: {pipeline.destination}")
    print(f"Dataset: {pipeline.dataset_name}")


if __name__ == "__main__":
    load_taxi_data()