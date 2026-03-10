with source as (
    select * from {{ source('raw', 'fhv_tripdata') }}
),

renamed as (
    select
        -- identifiers
        cast(dispatching_base_num as string) as dispatching_base_number,
        cast(Affiliated_base_number as string) as affiliated_base_number,

        -- timestamps
        cast(pickup_datetime as timestamp) as pickup_datetime,
        cast(dropOff_datetime as timestamp) as dropOff_datetime,

        -- trip info
        cast(PUlocationID as integer) as pickup_location_id,
        cast(DOlocationID as integer) as dropoff_location_id,
        cast(SR_Flag as string) as shared_request_flag,
        
    from source
    where dispatching_base_num is not null
)

select * from renamed