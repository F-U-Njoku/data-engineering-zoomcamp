"""
NYC Taxi Data Pipeline using dlt REST API Source

This pipeline extracts NYC taxi data from a paginated REST API and loads it into DuckDB.
"""

import dlt
from dlt.sources.rest_api import rest_api_source


def load_taxi_data() -> None:
    """
    Load NYC taxi data from the REST API into DuckDB.
    
    The API returns paginated JSON data with 1,000 records per page.
    Pagination continues until an empty page is returned.
    """
    
    # Configure the REST API source
    config = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
        },
        "resources": [
            {
                "name": "taxi_data",
                "endpoint": {
                    "path": "",  # Base URL is the endpoint itself
                    "params": {
                        "offset": 0,
                        "limit": 1000,
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 1000,
                        "offset": 0,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": None,  # API doesn't provide total count
                        "stop_after_empty_page": True,  # Stop when empty page is returned
                    },
                },
            },
        ],
    }
    
    # Create the source
    source = rest_api_source(config)
    
    # Create the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="taxi_pipeline",
        destination="duckdb",
        dataset_name="nyc_taxi_data",
        dev_mode=True,  # Enable dev mode for development
    )
    
    # Run the pipeline
    load_info = pipeline.run(source)
    
    # Print load information
    print(load_info)
    
    # Print summary of loaded data
    print("\n--- Load Summary ---")
    print(f"Pipeline: {pipeline.pipeline_name}")
    print(f"Destination: {pipeline.destination}")
    print(f"Dataset: {pipeline.dataset_name}")
    

if __name__ == "__main__":
    load_taxi_data()
