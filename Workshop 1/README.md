### Question 1: What is the start date and end date of the dataset?
`2009-06-01 to 2009-07-01`
```SQL
SELECT 
    MIN(trip_dropoff_date_time)::DATE AS min_date, 
    MAX(trip_dropoff_date_time)::DATE AS max_date
FROM "taxi_data";
```

### Question 2: What proportion of trips are paid with credit card? `26.66%`
```SQL
SELECT 
    (COUNT(CASE WHEN payment_type = 'Credit' THEN 1 END) * 1.0 / COUNT(*)) * 100 AS credit_proportion
FROM "taxi_data";
```
### Question 3: What is the total amount of money generated in tips? `$6,063.41`

```SQL
SELECT SUM (tip_amt)
FROM "taxi_data";
```