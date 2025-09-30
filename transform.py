import duckdb
import logging

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    filename='transform.log'
)
logger = logging.getLogger(__name__)

def transforms():
    con = None
    try:
        # Connect to local DuckDB instance
        con = duckdb.connect(database='emissions.duckdb', read_only=False)
        logger.info("Connected to DuckDB instance")
        
        #calculate yellow co2 per trip
        con.execute("""
            -- ALTER TABLE yellow_tripdata_2024 DROP COLUMN IF EXISTS trip_co2_kgs;       
            -- ALTER TABLE yellow_tripdata_2024 ADD COLUMN trip_co2_kgs DOUBLE;
            -- UPDATE yellow_tripdata_2024
            -- SET trip_co2_kgs = trip_distance * ( SELECT co2_grams_per_mile / 1000.0 FROM vehicle_emissions WHERE vehicle_type = 'yellow_taxi');
                    
            -- ALTER TABLE green_tripdata_2024 DROP COLUMN IF EXISTS trip_co2_kgs;       
            -- ALTER TABLE green_tripdata_2024 ADD COLUMN trip_co2_kgs DOUBLE;
            -- UPDATE green_tripdata_2024
            -- SET trip_co2_kgs = trip_distance * ( SELECT co2_grams_per_mile / 1000.0 FROM vehicle_emissions WHERE vehicle_type = 'green_taxi');
                    
            ALTER TABLE yellow_tripdata_full DROP COLUMN IF EXISTS trip_co2_kgs;       
            ALTER TABLE yellow_tripdata_full ADD COLUMN trip_co2_kgs DOUBLE;
            UPDATE yellow_tripdata_full
            SET trip_co2_kgs = trip_distance * ( SELECT co2_grams_per_mile / 1000.0 FROM vehicle_emissions WHERE vehicle_type = 'yellow_taxi');
                    
            ALTER TABLE green_tripdata_full DROP COLUMN IF EXISTS trip_co2_kgs;       
            ALTER TABLE green_tripdata_full ADD COLUMN trip_co2_kgs DOUBLE;
            UPDATE green_tripdata_full
            SET trip_co2_kgs = trip_distance * ( SELECT co2_grams_per_mile / 1000.0 FROM vehicle_emissions WHERE vehicle_type = 'green_taxi');      
""")
        print("CO2 per trip added to yellow_tripdata_full, and green_tripdata_full")
        logger.info("CO2 per trip added to yellow_tripdata_full, and green_tripdata_full")

        #calculate average mph per trip
        con.execute("""
            -- ALTER TABLE yellow_tripdata_2024 DROP COLUMN IF EXISTS avg_mph;       
            -- ALTER TABLE yellow_tripdata_2024 ADD COLUMN avg_mph DOUBLE;
            -- UPDATE yellow_tripdata_2024 
            -- SET avg_mph = (trip_distance / (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime)) / 3600.0));

            -- ALTER TABLE green_tripdata_2024 DROP COLUMN IF EXISTS avg_mph;       
            -- ALTER TABLE green_tripdata_2024 ADD COLUMN avg_mph DOUBLE;
            -- UPDATE green_tripdata_2024 
            -- SET avg_mph = (trip_distance / (EXTRACT(EPOCH FROM (lpep_dropoff_datetime - lpep_pickup_datetime)) / 3600.0));
                    
            ALTER TABLE yellow_tripdata_full DROP COLUMN IF EXISTS avg_mph;       
            ALTER TABLE yellow_tripdata_full ADD COLUMN avg_mph DOUBLE;
            UPDATE yellow_tripdata_full 
            SET avg_mph = (trip_distance / (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime)) / 3600.0));
                    
            ALTER TABLE green_tripdata_full DROP COLUMN IF EXISTS avg_mph;       
            ALTER TABLE green_tripdata_full ADD COLUMN avg_mph DOUBLE;
            UPDATE green_tripdata_full 
            SET avg_mph = (trip_distance / (EXTRACT(EPOCH FROM (lpep_dropoff_datetime - lpep_pickup_datetime)) / 3600.0));
""")
        print("Avg mph per trip added to yellow_tripdata_full, and green_tripdata_full")
        logger.info("Avg mph per trip added to yellow_tripdata_full, and green_tripdata_full")
        
        #calculating the hour trip started
        con.execute("""
            -- ALTER TABLE yellow_tripdata_2024 DROP COLUMN IF EXISTS hour_of_day;       
            -- ALTER TABLE yellow_tripdata_2024 ADD COLUMN hour_of_day INTEGER;
            -- UPDATE yellow_tripdata_2024 SET hour_of_day = EXTRACT(HOUR FROM tpep_pickup_datetime);

            -- ALTER TABLE green_tripdata_2024 DROP COLUMN IF EXISTS hour_of_day;       
            -- ALTER TABLE green_tripdata_2024 ADD COLUMN hour_of_day INTEGER;
            -- UPDATE green_tripdata_2024 SET hour_of_day = EXTRACT(HOUR FROM lpep_pickup_datetime);
                    
            ALTER TABLE yellow_tripdata_full DROP COLUMN IF EXISTS hour_of_day;       
            ALTER TABLE yellow_tripdata_full ADD COLUMN hour_of_day INTEGER;
            UPDATE yellow_tripdata_full SET hour_of_day = EXTRACT(HOUR FROM tpep_pickup_datetime);
                    
            ALTER TABLE green_tripdata_full DROP COLUMN IF EXISTS hour_of_day;       
            ALTER TABLE green_tripdata_full ADD COLUMN hour_of_day INTEGER;
            UPDATE green_tripdata_full SET hour_of_day = EXTRACT(HOUR FROM lpep_pickup_datetime);
""")
        print("Trip hour added to yellow_tripdata_full, and green_tripdata_full")
        logger.info("Trip hour added to yellow_tripdata_full, and green_tripdata_full")

        #calculating trip day of week
        con.execute("""
            -- ALTER TABLE yellow_tripdata_2024 DROP COLUMN IF EXISTS day_of_week;       
            -- ALTER TABLE yellow_tripdata_2024 ADD COLUMN day_of_week INTEGER;
            -- UPDATE yellow_tripdata_2024 SET day_of_week = EXTRACT(DOW FROM tpep_pickup_datetime);

            -- ALTER TABLE green_tripdata_2024 DROP COLUMN IF EXISTS day_of_week;       
            -- ALTER TABLE green_tripdata_2024 ADD COLUMN day_of_week INTEGER;
            -- UPDATE green_tripdata_2024 SET day_of_week = EXTRACT(DOW FROM lpep_pickup_datetime);
                    
            ALTER TABLE yellow_tripdata_full DROP COLUMN IF EXISTS day_of_week;       
            ALTER TABLE yellow_tripdata_full ADD COLUMN day_of_week INTEGER;
            UPDATE yellow_tripdata_full SET day_of_week = EXTRACT(DOW FROM tpep_pickup_datetime);
                    
            ALTER TABLE green_tripdata_full DROP COLUMN IF EXISTS day_of_week;
            ALTER TABLE green_tripdata_full ADD COLUMN day_of_week INTEGER;
            UPDATE green_tripdata_full SET day_of_week = EXTRACT(DOW FROM lpep_pickup_datetime);
""")
        print("Trip day of week added to yellow_tripdata_full, and green_tripdata_full")
        logger.info("Trip day of week added to yellow_tripdata_full, and green_tripdata_full")

        #calculating week number of year
        con.execute("""
            -- ALTER TABLE yellow_tripdata_2024 DROP COLUMN IF EXISTS week_of_year;       
            -- ALTER TABLE yellow_tripdata_2024 ADD COLUMN week_of_year INTEGER;
            -- UPDATE yellow_tripdata_2024 SET week_of_year = EXTRACT(WEEK FROM tpep_pickup_datetime);

            -- ALTER TABLE green_tripdata_2024 DROP COLUMN IF EXISTS week_of_year;       
            -- ALTER TABLE green_tripdata_2024 ADD COLUMN week_of_year INTEGER;
            -- UPDATE green_tripdata_2024 SET week_of_year = EXTRACT(WEEK FROM lpep_pickup_datetime);
                    
            ALTER TABLE yellow_tripdata_full DROP COLUMN IF EXISTS week_of_year;       
            ALTER TABLE yellow_tripdata_full ADD COLUMN week_of_year INTEGER;
            UPDATE yellow_tripdata_full SET week_of_year = EXTRACT(WEEK FROM tpep_pickup_datetime);
                    
            ALTER TABLE green_tripdata_full DROP COLUMN IF EXISTS week_of_year;       
            ALTER TABLE green_tripdata_full ADD COLUMN week_of_year INTEGER;
            UPDATE green_tripdata_full SET week_of_year = EXTRACT(WEEK FROM lpep_pickup_datetime);
""")
        print("Week number added to yellow_tripdata_full, and green_tripdata_full")
        logger.info("Week number added to yellow_tripdata_full, and green_tripdata_full")

        #calculating month
        con.execute("""
            -- ALTER TABLE yellow_tripdata_2024 DROP COLUMN IF EXISTS month_of_year;       
            -- ALTER TABLE yellow_tripdata_2024 ADD COLUMN month_of_year INTEGER;
            -- UPDATE yellow_tripdata_2024 SET month_of_year = EXTRACT(MONTH FROM tpep_pickup_datetime);
                    
            -- ALTER TABLE green_tripdata_2024 DROP COLUMN IF EXISTS month_of_year;
            -- ALTER TABLE green_tripdata_2024 ADD COLUMN month_of_year INTEGER;
            -- UPDATE green_tripdata_2024 SET month_of_year = EXTRACT(MONTH FROM lpep_pickup_datetime);
                    
            ALTER TABLE yellow_tripdata_full DROP COLUMN IF EXISTS month_of_year;       
            ALTER TABLE yellow_tripdata_full ADD COLUMN month_of_year INTEGER;
            UPDATE yellow_tripdata_full SET month_of_year = EXTRACT(MONTH FROM tpep_pickup_datetime);
                    
            ALTER TABLE green_tripdata_full DROP COLUMN IF EXISTS month_of_year;       
            ALTER TABLE green_tripdata_full ADD COLUMN month_of_year INTEGER;
            UPDATE green_tripdata_full SET month_of_year = EXTRACT(MONTH FROM lpep_pickup_datetime);
""")
        print("Month added to yellow_tripdata_full, and green_tripdata_full")
        logger.info("Month added to yellow_tripdata_full, and green_tripdata_full")

    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    transforms()
