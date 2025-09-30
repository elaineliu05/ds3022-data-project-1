SELECT
    green_taxi.*,

    -- calculating co2 emissions per trip in kilograms
    green_taxi.trip_distance * (vehicle_emissions.co2_grams_per_mile / 1000.0) AS trip_co2_kgs,

    -- average mph
    green_taxi.trip_distance / NULLIF(EXTRACT(EPOCH FROM (green_taxi.lpep_dropoff_datetime - green_taxi.lpep_pickup_datetime)) / 3600.0, 0) AS avg_mph,

    -- hour of day
    EXTRACT(HOUR FROM green_taxi.lpep_pickup_datetime) AS hour_of_day,

    -- day of week
    EXTRACT(DOW FROM green_taxi.lpep_pickup_datetime) AS day_of_week,

    -- week of year
    EXTRACT(WEEK FROM green_taxi.lpep_pickup_datetime) AS week_of_year,

    -- month of year
    EXTRACT(MONTH FROM green_taxi.lpep_pickup_datetime) AS month_of_year

FROM "emissions"."main"."green_tripdata_full" AS green_taxi
JOIN "emissions"."main"."vehicle_emissions" AS vehicle_emissions
  ON vehicle_emissions.vehicle_type = 'green_taxi'