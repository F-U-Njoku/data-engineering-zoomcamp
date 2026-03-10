### Question 1. dbt Lineage and Execution
Given a dbt project with the following structure:

```
models/
├── staging/
│   ├── stg_green_tripdata.sql
│   └── stg_yellow_tripdata.sql
└── intermediate/
    └── int_trips_unioned.sql (depends on stg_green_tripdata & stg_yellow_tripdata)
```

If you run `dbt run --select int_trips_unioned`, what models will be built? **int_trips_unioned only**

### Question 2. dbt Tests

You've configured a generic test like this in your `schema.yml`:

```yaml
columns:
  - name: payment_type
    data_tests:
      - accepted_values:
          arguments:
            values: [1, 2, 3, 4, 5]
            quote: false
```

Your model `fct_trips` has been running successfully for months. A new value `6` now appears in the source data.

What happens when you run `dbt test --select fct_trips`? **dbt will fail the test, returning a non-zero exit code**

### Question 3. Counting Records in fct_monthly_zone_revenue
What is the count of records in the fct_monthly_zone_revenue model?
```SQL
SELECT COUNT(*) 
FROM `zoomca.dbt_unjoku.fct_monthly_zone_revenue`;
```
**15,579**

### Question 4. Best Performing Zone for Green Taxis (2020)

Using the `fct_monthly_zone_revenue` table, find the pickup zone with the **highest total revenue** (`revenue_monthly_total_amount`) for **Green** taxi trips in 2020.
```SQL
SELECT pickup_zone, revenue_monthly_total_amount, revenue_month
FROM `zoomca.dbt_unjoku.fct_monthly_zone_revenue` 
where service_type='Green' and extract(year FROM revenue_month) = 2020
order by revenue_monthly_total_amount desc 
limit 1;
```

Which zone had the highest revenue? **East Harlem North,	43,4092.46,	2020-01-01**

### Question 5. Green Taxi Trip Counts (October 2019)

Using the `fct_monthly_zone_revenue` table, what is the **total number of trips** (`total_monthly_trips`) for Green taxis in October 2019? **384,624**
```SQL
SELECT sum(total_monthly_trips)
FROM `zoomca.dbt_unjoku.fct_monthly_zone_revenue` 
where service_type='Green' and revenue_month = '2019-10-01';
```

### Question 6. Build a Staging Model for FHV Data

What is the count of records in stg_fhv_tripdata? **43,244,693**
```SQL
SELECT count(*) 
FROM prod.stg_fhv_tripdata
```