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
SELECT COUNT(*) FROM `zoomca.dbt_unjoku.fct_monthly_zone_revenue`;
```
**15,579**

