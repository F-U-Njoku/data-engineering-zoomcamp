# Module 1 Homework: Docker & SQL

## Question 1. Understanding Docker images
`docker run -it --entrypoint bash --rm python:3.13`
![alt text](/images/image.png)
What's the version of `pip` in the image? **25.3**

# Question 2. Understanding Docker networking and docker-compose
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database? `postgres:5432` and `db:5432`.

# Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between `2025-11-01` and `2025-12-01`, exclusive of the upper bound), how many trips had a `trip_distance` of less than or equal to 1 mile? **8007**
``` sql
SELECT COUNT(*)
FROM green_tripdata
WHERE lpep_pickup_datetime>='2025-11-01' AND lpep_pickup_datetime<'2025-12-01'
AND trip_distance<=1;
```

# Question 4. Longest trip for each day
Which was the pick up day with the longest trip distance? Only consider trips with `trip_distance` less than 100 miles (to exclude data errors). **2025-11-14**
``` sql
SELECT lpep_pickup_datetime
FROM green_tripdata
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;
```
# Question 5. Biggest pickup zone
Which was the pickup zone with the largest `total_amount` (sum of all trips) on November 18th, 2025? **East Harlem North**
``` sql
SELECT t."Zone", SUM(g.total_amount)
FROM green_tripdata g 
JOIN taxi_zone_lookup t
ON g."PULocationID" = t."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
``` 
# Question 6. Largest tip
For the passengers picked up in the zone named `East Harlem North` in November 2025, which was the drop off zone that had the largest tip? **Yorkville West**
``` sql
SELECT df."Zone", g.tip_amount
FROM green_tripdata g 
JOIN taxi_zone_lookup pu ON g."PULocationID" = pu."LocationID"
JOIN taxi_zone_lookup df ON g."DOLocationID" = df."LocationID"
WHERE pu."Zone" = 'East Harlem North'
  AND g.lpep_pickup_datetime >= '2025-11-01' 
  AND g.lpep_pickup_datetime < '2025-12-01'
ORDER BY g.tip_amount DESC
LIMIT 1;
``` 

# Question 7. Terraform Workflow
Which of the following sequences, respectively, describes the workflow for:

  1. Downloading the provider plugins and setting up backend,
  2. Generating proposed changes and auto-executing the plan
  3. Remove all resources managed by terraform`

`terraform init, terraform apply -auto-approve, terraform destroy` 
