SELECT
    yellow_taxi.*,

    -- calculating co2 emissions per trip in kilograms
    yellow_taxi.trip_distance * (vehicle_emissions.co2_grams_per_mile / 1000.0) AS trip_co2_kgs,

    -- average mph
    yellow_taxi.trip_distance / NULLIF(EXTRACT(EPOCH FROM (yellow_taxi.tpep_dropoff_datetime - yellow_taxi.tpep_pickup_datetime)) / 3600.0, 0) AS avg_mph,

    -- hour of day
    EXTRACT(HOUR FROM yellow_taxi.tpep_pickup_datetime) AS hour_of_day,

    -- day of week
    EXTRACT(DOW FROM yellow_taxi.tpep_pickup_datetime) AS day_of_week,

    -- week of year
    EXTRACT(WEEK FROM yellow_taxi.tpep_pickup_datetime) AS week_of_year,

    -- month of year
    EXTRACT(MONTH FROM yellow_taxi.tpep_pickup_datetime) AS month_of_year

FROM "emissions"."main"."yellow_tripdata_2024" AS yellow_taxi
JOIN "emissions"."main"."vehicle_emissions" AS vehicle_emissions
  ON vehicle_emissions.vehicle_type = 'yellow_taxi'