## Question 1. Counting records

What is count of records for the 2024 Yellow Taxi Data? **20,332,092**

``` sql
SELECT  COUNT(*) 
FROM `zoomca.de_nyc_taxi.yellow_tripdata_parquet`;
```
## Question 2. Data read estimation

Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
 
What is the **estimated amount** of data that will be read when this query is executed on the External Table and the Table?
``` sql
SELECT COUNT(DISTINCT PULocationID) 
FROM `zoomca.de_nyc_taxi.yellow_tripdata_2024_pqt`;
``` 
**155.12 MB**
``` sql
SELECT COUNT(DISTINCT PULocationID) 
FROM `zoomca.de_nyc_taxi.yellow_tripdata_2024_pqt_ext`;
``` 
**0 B**
## Question 3. Understanding columnar storage

Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table.
``` sql
SELECT PULocationID 
FROM `zoomca.de_nyc_taxi.yellow_tripdata_2024_pqt`;
``` 
**155.12 MB**
``` sql
SELECT PULocationID, DOLocationID
FROM `zoomca.de_nyc_taxi.yellow_tripdata_2024_pqt`;
``` 
**310.24 MB**
Why are the estimated number of Bytes different?
- BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires 
## Question 4. Counting zero fare trips

How many records have a fare_amount of 0? **8,333**
```SQL
SELECT COUNT(*) 
FROM `zoomca.de_nyc_taxi.yellow_tripdata_2024_pqt`
WHERE fare_amount=0;
```

## Question 5. Partitioning and clustering

What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)
- Partition by tpep_dropoff_datetime and Cluster on VendorID
```SQL
CREATE OR REPLACE TABLE `zoomca.de_nyc_taxi.yellow_tripdata_2024_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM `zoomca.de_nyc_taxi.yellow_tripdata_2024_pqt`;
```

## Question 6. Partition benefits

Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime
2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values? 

- 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7. External table storage

Where is the data stored in the External Table you created?

- GCP Bucket

## Question 8. Clustering best practices

It is best practice in Big Query to always cluster your data: **False**

## Question 9. Understanding table scans

No Points: Write a `SELECT count(*)` query FROM the materialized table you created. How many bytes does it estimate will be read? **0 B**

Why?

```BigQuery keeps a live, cached count of the total number of rows in every table. Since reading metadata doesn't require scanning the columns stored in Colossus (BigQuery’s storage engine), the cost is $0 and the bytes processed is 0.```