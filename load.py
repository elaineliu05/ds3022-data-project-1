#to activate env: \ds\Scripts\Activate.ps1
#duckdb: C:\duckdb_cli-windows-amd64\duckdb.exe
import duckdb
import logging
import time

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    filename='load.log'
)
logger = logging.getLogger(__name__)

def load_parquet_files():

    con = None

    try:
        # Connect to local DuckDB instance
        con = duckdb.connect(database='emissions.duckdb', read_only=False)
        logger.info("Connected to DuckDB instance")

        # # loading in yellow taxi 2024
        # con.execute(f"""
        #     DROP TABLE IF EXISTS yellow_tripdata_2024;
        #     CREATE TABLE yellow_tripdata_2024 AS
        #     SELECT *
        #     FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet');
        #      """)
        # logger.info("Dropped yellow_tripdata_2024 table if exists")
        # for i in range(2, 13): # looping through months 
        #     link = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-{i:02d}.parquet"
        #     con.execute(f"""
        #         INSERT INTO yellow_tripdata_2024 SELECT * FROM read_parquet('{link}');
        #     """)
        #     print(f"yellow: Finished month {i}, sleeping for 60 seconds...")
        #     time.sleep(60)
        # #yellow_tripdata_2024 row counts
        # yellow_2024_rows = con.execute(f"""
        #     SELECT COUNT(*) FROM yellow_tripdata_2024; """).fetchone()[0]
        # print("Number of rows in yellow_tripdata_2024:", yellow_2024_rows)
        # logger.info("Calculated num rows in yellow_tripdata_2024")

        # #loading in green taxi 2024
        # con.execute(f"""
        #     DROP TABLE IF EXISTS green_tripdata_2024;
        #     CREATE TABLE green_tripdata_2024 AS
        #     SELECT *
        #     FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-01.parquet');
        #      """)
        # logger.info("Dropped green_tripdata_2024 table if exists")
        # for i in range(2, 13): #looping through months
        #     link = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-{i:02d}.parquet"
        #     con.execute(f"""
        #         INSERT INTO green_tripdata_2024 SELECT * FROM read_parquet('{link}');
        #     """)
        #     print(f"green: Finished month {i}, sleeping for 60 seconds...")
        #     time.sleep(60)
        # #green_tripdata_2024 row counts
        # green_2024_rows = con.execute(f"""
        #     SELECT COUNT(*) FROM green_tripdata_2024;
        #         """).fetchone()[0]
        # print("Number of rows in green_tripdata_2024:", green_2024_rows)
        # logger.info("Calculated num rows in green_tripdata_2024")

        # #loading in emissions data
        # con.execute(f"""
        #     DROP TABLE IF EXISTS vehicle_emissions;
        #     CREATE TABLE vehicle_emissions AS
        #     SELECT *
        #     FROM read_csv('C:/Users/elain/OneDrive/Documents/DS/Systems II/ds3022-data-project-1/data/vehicle_emissions.csv');
        #      """)
        # logger.info("Dropped green_tripdata_2024 table if exists")

        #loading in yellow taxi 2015 to 2024
        con.execute(f"""
            DROP TABLE IF EXISTS yellow_tripdata_full;
            CREATE TABLE yellow_tripdata_full AS
            SELECT tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, fare_amount, tip_amount
            FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2015-01.parquet') WHERE 1=0;
             """)
        logger.info("Dropped yellow_tripdata_full table if exists")
        for year in range(2015, 2025): #looping through years
            for month in range(1, 13):
                link = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet"
                con.execute(f"""
                    INSERT INTO yellow_tripdata_full SELECT tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, fare_amount, tip_amount FROM read_parquet('{link}');
                """)
                print(f"yellow_full: Finished month {month}, sleeping for 60 seconds...")
                time.sleep(60)
            print("yellow_full: Finished year", year)
        #yellow_tripdata_full row counts
        yellow_full_rows = con.execute(f"""
            SELECT COUNT(*) FROM yellow_tripdata_full; """).fetchone()[0]
        print("Number of rows in yellow_tripdata_full:", yellow_full_rows)
        logger.info("Calculated num rows in yellow_tripdata_2024")

        #loading in green taxi 2015 to 2024
        con.execute(f"""
            DROP TABLE IF EXISTS green_tripdata_full;
            CREATE TABLE green_tripdata_full AS
            SELECT lpep_pickup_datetime, lpep_dropoff_datetime, passenger_count, trip_distance, fare_amount, tip_amount
            FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2015-01.parquet') WHERE 1=0;
             """)   
        logger.info("Dropped green_tripdata_full table if exists")
        for year in range(2015, 2025): #looping through years
            for month in range(1, 13):
                link = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet"
                con.execute(f"""
                    INSERT INTO green_tripdata_full SELECT lpep_pickup_datetime, lpep_dropoff_datetime, passenger_count, trip_distance, fare_amount, tip_amount FROM read_parquet('{link}');
                """)
                print(f"green_full: Finished month {month}, sleeping for 60 seconds...")
                time.sleep(60)
            print("green_full: Finished year", year)
        #green_tripdata_full row counts
        green_full_rows = con.execute(f"""
            SELECT COUNT(*) FROM green_tripdata_full; """).fetchone()[0]
        print("Number of rows in green_tripdata_full:", green_full_rows)
        logger.info("Calculated num rows in green_tripdata_2024")

    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")


def data_summarization():
    con = None
    try:
        # Connect to local DuckDB instance
        con = duckdb.connect(database='emissions.duckdb', read_only=False)
        logger.info("Connected to DuckDB instance")

        # # yellow taxis 2024 number of trips
        # yellow_num_trips_2024 = con.execute(f"""
        #     SELECT COUNT(*) FROM yellow_tripdata_2024;
        #     """).fetchone()[0]
        # print("Number of trips made by yellow taxis 2024:", yellow_num_trips_2024)
        # logger.info("Num trips of yellow taxis 2024 calculated")
        # # yellow taxis 2024 average stats
        # yellow_avgs_2024 = con.execute(f"""
        #     SELECT AVG(passenger_count) AS avg_passengers, AVG(trip_distance) AS avg_distance, AVG(fare_amount) AS avg_fare, AVG(tip_amount) AS avg_tip
        #     FROM yellow_tripdata_2024;
        #     """).fetchdf()
        # print("Averages for yellow taxis 2024:\n", yellow_avgs_2024)
        # logger.info("Averages for yellow taxis 2024 calculated")

        # # green taxis 2024 number of trips
        # green_num_trips = con.execute(f"""
        #     SELECT COUNT(*)
        #     FROM green_tripdata_2024;
        #     """).fetchone()[0]
        # print("Number of trips made by green taxis 2024:", green_num_trips)
        # logger.info("Num trips of green taxis 2024 calculated")
        # # green taxis 2024 average stats
        # green_avgs = con.execute(f"""
        #     SELECT AVG(passenger_count) AS avg_passengers, AVG(trip_distance) AS avg_distance, AVG(fare_amount) AS avg_fare, AVG(tip_amount) AS avg_tip
        #     FROM green_tripdata_2024;
        #     """).fetchdf()
        # print("Averages for green taxis 2024:\n", green_avgs)
        # logger.info("Averages for green taxis 2024 calculated")

        # yellow taxis full number of trips
        yellow_num_trips_full = con.execute(f"""
            SELECT COUNT(*) FROM yellow_tripdata_full;
            """).fetchone()[0]
        print("Number of trips made by yellow taxis full:", yellow_num_trips_full)
        logger.info("Num trips of yellow taxis full calculated")
        # yellow taxis full average stats
        yellow_full_avgs = con.execute(f"""
            SELECT AVG(passenger_count) AS avg_passengers, AVG(trip_distance) AS avg_distance, AVG(fare_amount) AS avg_fare, AVG(tip_amount) AS avg_tip
            FROM yellow_tripdata_full;
            """).fetchdf()
        print("Averages for yellow taxis full:\n", yellow_full_avgs)
        logger.info("Averages for yellow taxis full calculated")

        # green taxis full number of trips
        green_num_trips_full = con.execute(f"""
            SELECT COUNT(*) FROM green_tripdata_full;
            """).fetchone()[0]
        print("Number of trips made by green taxis full:", green_num_trips_full)
        logger.info("Num trips of green taxis full calculated")
        # green taxis full average stats
        green_full_avgs = con.execute(f"""
            SELECT AVG(passenger_count) AS avg_passengers, AVG(trip_distance) AS avg_distance, AVG(fare_amount) AS avg_fare, AVG(tip_amount) AS avg_tip
            FROM green_tripdata_full;
            """).fetchdf()
        print("Averages for green taxis full:\n", green_full_avgs)
        logger.info("Averages for green taxis full calculated")

    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    load_parquet_files()
    data_summarization()