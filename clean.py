import duckdb
import logging

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    filename='clean.log'
)
logger = logging.getLogger(__name__)

def clean_tables():
    con = None
    try:
        # Connect to local DuckDB instance
        con = duckdb.connect(database='emissions.duckdb', read_only=False)
        logger.info("Connected to DuckDB instance")
        
        #remove duplicates
        con.execute("""
            -- CREATE TABLE yellow_tripdata_2024_clean AS 
            -- SELECT DISTINCT * FROM yellow_tripdata_2024;
            -- DROP TABLE yellow_tripdata_2024;
            -- ALTER TABLE yellow_tripdata_2024_clean RENAME TO yellow_tripdata_2024;
        
            -- CREATE TABLE green_tripdata_2024_clean AS 
            -- SELECT DISTINCT * FROM green_tripdata_2024;
            -- DROP TABLE green_tripdata_2024;
            -- ALTER TABLE green_tripdata_2024_clean RENAME TO green_tripdata_2024;
            
            CREATE TABLE yellow_tripdata_full_clean AS 
            SELECT DISTINCT * FROM yellow_tripdata_full;
            DROP TABLE yellow_tripdata_full;
            ALTER TABLE yellow_tripdata_full_clean RENAME TO yellow_tripdata_full;
            
            CREATE TABLE green_tripdata_full_clean AS 
            SELECT DISTINCT * FROM green_tripdata_full;
            DROP TABLE green_tripdata_full;
            ALTER TABLE green_tripdata_full_clean RENAME TO green_tripdata_full;
                    """)
        
        print("Duplicates removed from yellow_tripdata_full, and green_tripdata_full")
        logger.info("Duplicates removed from yellow_tripdata_full, and green_tripdata_full")

        #remove trips w 0 passengers 
        con.execute("""
            -- CREATE TABLE yellow_tripdata_2024_clean AS 
            -- SELECT * FROM yellow_tripdata_2024
            -- WHERE passenger_count > 0;
            -- DROP TABLE yellow_tripdata_2024;
            -- ALTER TABLE yellow_tripdata_2024_clean RENAME TO yellow_tripdata_2024;
        
            -- CREATE TABLE green_tripdata_2024_clean AS 
            -- SELECT * FROM green_tripdata_2024
            -- WHERE passenger_count > 0;
            -- DROP TABLE green_tripdata_2024;
            -- ALTER TABLE green_tripdata_2024_clean RENAME TO green_tripdata_2024;
                    
            CREATE TABLE yellow_tripdata_full_clean AS
            SELECT * FROM yellow_tripdata_full
            WHERE passenger_count > 0;
            DROP TABLE yellow_tripdata_full;
            ALTER TABLE yellow_tripdata_full_clean RENAME TO yellow_tripdata_full;
                    
            CREATE TABLE green_tripdata_full_clean AS
            SELECT * FROM green_tripdata_full
            WHERE passenger_count > 0;
            DROP TABLE green_tripdata_full;
            ALTER TABLE green_tripdata_full_clean RENAME TO green_tripdata_full;
                    """)
        print("Trips with 0 passengers removed yellow_tripdata_full and green_tripdata_full")
        logger.info("Trips with 0 passengers removed from yellow_tripdata_full, and green_tripdata_full")

        #remove trips w 0 distance or greater than 100 miles
        con.execute("""
            -- CREATE TABLE yellow_tripdata_2024_clean AS 
            -- SELECT * FROM yellow_tripdata_2024
            -- WHERE trip_distance > 0 AND trip_distance < 100;
            -- DROP TABLE yellow_tripdata_2024;
            -- ALTER TABLE yellow_tripdata_2024_clean RENAME TO yellow_tripdata_2024;
        
            -- CREATE TABLE green_tripdata_2024_clean AS 
            -- SELECT * FROM green_tripdata_2024
            -- WHERE trip_distance > 0 AND trip_distance < 100;
            -- DROP TABLE green_tripdata_2024;
            -- ALTER TABLE green_tripdata_2024_clean RENAME TO green_tripdata_2024;
                    
            CREATE TABLE yellow_tripdata_full_clean AS
            SELECT * FROM yellow_tripdata_full
            WHERE trip_distance > 0 AND trip_distance < 100;
            DROP TABLE yellow_tripdata_full;
            ALTER TABLE yellow_tripdata_full_clean RENAME TO yellow_tripdata_full;
                    
            CREATE TABLE green_tripdata_full_clean AS
            SELECT * FROM green_tripdata_full
            WHERE trip_distance > 0 AND trip_distance < 100;
            DROP TABLE green_tripdata_full;
            ALTER TABLE green_tripdata_full_clean RENAME TO green_tripdata_full;
                    """)
        print("Trips with distance of 0 miles or greater than 100 miles removed from yellow_tripdata_full, and green_tripdata_full")
        logger.info("Trips with distance of 0 miles or greater than 100 miles removed from yellow_tripdata_full, and green_tripdata_full")

        #remove trips greater than 24 hrs in length
        con.execute("""
            -- CREATE TABLE yellow_tripdata_2024_clean AS 
            -- SELECT * FROM yellow_tripdata_2024
            -- WHERE (tpep_dropoff_datetime - tpep_pickup_datetime) < INTERVAL '24' HOUR;
            -- DROP TABLE yellow_tripdata_2024;
            -- ALTER TABLE yellow_tripdata_2024_clean RENAME TO yellow_tripdata_2024;
        
            -- CREATE TABLE green_tripdata_2024_clean AS 
            -- SELECT * FROM green_tripdata_2024
            -- WHERE (lpep_dropoff_datetime - lpep_pickup_datetime) < INTERVAL '24' HOUR;
            -- DROP TABLE green_tripdata_2024;
            -- ALTER TABLE green_tripdata_2024_clean RENAME TO green_tripdata_2024;
                    
            CREATE TABLE yellow_tripdata_full_clean AS
            SELECT * FROM yellow_tripdata_full
            WHERE (tpep_dropoff_datetime - tpep_pickup_datetime) < INTERVAL '24' HOUR;
            DROP TABLE yellow_tripdata_full;
            ALTER TABLE yellow_tripdata_full_clean RENAME TO yellow_tripdata_full;
                    
            CREATE TABLE green_tripdata_full_clean AS
            SELECT * FROM green_tripdata_full
            WHERE (lpep_dropoff_datetime - lpep_pickup_datetime) < INTERVAL '24' HOUR;
            DROP TABLE green_tripdata_full;
            ALTER TABLE green_tripdata_full_clean RENAME TO green_tripdata_full;
        """)
        print("Trips longer than 24 hours removed from yellow_tripdata_full, and green_tripdata_full")
        logger.info("Trips longer than 24 hours removed from yellow_tripdata_full, and green_tripdata_full")

    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")

def tests():
    con = None
    try:
        # Connect to local DuckDB instance
        con = duckdb.connect(database='emissions.duckdb', read_only=False)
        logger.info("Connected to DuckDB instance")

        # testing no trips w 0 passengers
        # yellow_2024_no_passengers = con.execute(f"""
        # SELECT COUNT(*) AS n FROM yellow_tripdata_2024 WHERE passenger_count <= 0;                           
        #     """).fetchone()[0]
        # green_2024_no_passengers = con.execute(f"""
        # SELECT COUNT(*) AS n FROM green_tripdata_2024 WHERE passenger_count <= 0;                           
        #     """).fetchone()[0]
        yellow_full_no_passengers = con.execute(f"""
        SELECT COUNT(*) AS n FROM yellow_tripdata_full WHERE passenger_count <= 0;
            """).fetchone()[0]
        green_full_no_passengers = con.execute(f"""
        SELECT COUNT(*) AS n FROM green_tripdata_full WHERE passenger_count <= 0;
            """).fetchone()[0]
        # print("Number of trips from yellow taxies in 2024 with 0 passengers:", yellow_2024_no_passengers)
        # print("Number of trips from green taxies in 2024 with 0 passengers:", green_2024_no_passengers)
        print("Number of trips from yellow taxies from 2015 to 2024 with 0 passengers:", yellow_full_no_passengers)
        print("Number of trips from green taxies from 2015 to 2024 with 0 passengers:", green_full_no_passengers)
        logger.info("Tested for trips with 0 passengers")

        # testing no trips w 0 distance or greater than 100 miles
        # yellow_2024_invalid_distance = con.execute(f"""
        # SELECT COUNT(*) AS n FROM yellow_tripdata_2024 WHERE trip_distance <= 0 OR trip_distance >= 100;                           
        #     """).fetchone()[0]
        # green_2024_invalid_distance = con.execute(f"""
        # SELECT COUNT(*) AS n FROM green_tripdata_2024 WHERE trip_distance <= 0 OR trip_distance >= 100;                           
        #     """).fetchone()[0]  
        yellow_full_invalid_distance = con.execute(f"""
        SELECT COUNT(*) AS n FROM yellow_tripdata_full WHERE trip_distance <= 0 OR trip_distance >= 100;                           
            """).fetchone()[0]
        green_full_invalid_distance = con.execute(f"""
        SELECT COUNT(*) AS n FROM green_tripdata_full WHERE trip_distance <= 0 OR trip_distance >= 100;                           
            """).fetchone()[0]
        # print("Number of trips from yellow taxies in 2024 with invalid distance:", yellow_2024_invalid_distance)
        # print("Number of trips from green taxies in 2024 with invalid distance:", green_2024_invalid_distance)
        print("Number of trips from yellow taxies from 2015 to 2024 with invalid distance:", yellow_full_invalid_distance)
        print("Number of trips from green taxies from 2015 to 2024 with invalid distance:", green_full_invalid_distance)
        logger.info("Tested for trips with invalid distance")

        # testing no trips greater than 24 hrs in length
        # yellow_2024_long_trips = con.execute(f"""
        # SELECT COUNT(*) AS n FROM yellow_tripdata_2024 WHERE (tpep_dropoff_datetime - tpep_pickup_datetime) >= INTERVAL '24' HOUR;                           
        #     """).fetchone()[0]  
        # green_2024_long_trips = con.execute(f"""
        # SELECT COUNT(*) AS n FROM green_tripdata_2024 WHERE (lpep_dropoff_datetime - lpep_pickup_datetime) >= INTERVAL '24' HOUR;                           
        #     """).fetchone()[0]  
        yellow_full_long_trips = con.execute(f"""
        SELECT COUNT(*) AS n FROM yellow_tripdata_full WHERE (tpep_dropoff_datetime - tpep_pickup_datetime) >= INTERVAL '24' HOUR;                           
            """).fetchone()[0]
        green_full_long_trips = con.execute(f"""
        SELECT COUNT(*) AS n FROM green_tripdata_full WHERE (lpep_dropoff_datetime - lpep_pickup_datetime) >= INTERVAL '24' HOUR;                           
            """).fetchone()[0]
        # print("Number of trips from yellow taxies in 2024 longer than 24 hours:", yellow_2024_long_trips)
        # print("Number of trips from green taxies in 2024 longer than 24 hours:", green_2024_long_trips)
        print("Number of trips from yellow taxies from 2015 to 2024 longer than 24 hours:", yellow_full_long_trips)
        print("Number of trips from green taxies from 2015 to 2024 longer than 24 hours:", green_full_long_trips)
        logger.info("Tested for trips longer than 24 hours")


    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    clean_tables()
    tests()