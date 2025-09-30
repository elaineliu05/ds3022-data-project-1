import duckdb
import logging

import time

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    filename='analysis.log'
)
logger = logging.getLogger(__name__)

def analysis():
    con = None
    try:
        # Connect to local DuckDB instance
        con = duckdb.connect(database='emissions.duckdb', read_only=False)
        logger.info("Connected to DuckDB instance")

        # select max trip_co2_kgs 
        yellow_2024_max_co2 = con.execute(f"""
            SELECT MAX(trip_co2_kgs) AS max FROM yellow_tripdata_2024;                           
            """).fetchone()[0]
        green_2024_max_co2 = con.execute(f"""
            SELECT MAX(trip_co2_kgs) AS max_co2 FROM green_tripdata_2024;                           
            """).fetchone()[0]
        yellow_full_max_co2 = con.execute(f"""
            SELECT MAX(trip_co2_kgs) AS max FROM yellow_tripdata_full;
            """).fetchone()[0]
        green_full_max_co2 = con.execute(f"""
            SELECT MAX(trip_co2_kgs) AS max_co2 FROM green_tripdata_full;
            """).fetchone()[0]
        print("Largest CO2 producing trip for yellow taxis 2024 (kgs):", yellow_2024_max_co2)
        print("Largest CO2 producing trip for green taxis 2024 (kgs):", green_2024_max_co2)
        print("Largest CO2 producing trip for yellow taxis from 2015 to 2024 (kgs):", yellow_full_max_co2)
        print("Largest CO2 producing trip for green taxis from 2015 to 2024 (kgs):", green_full_max_co2)
        logger.info("Calculated largest CO2 producing trip for taxis")

        #most carbon heavy and carbon light hours of the day
        yellow_2024_heavy_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY hour_of_day ORDER BY total DESC LIMIT 1;                           
        """).fetchone()[0]
        yellow_2024_light_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY hour_of_day ORDER BY total ASC LIMIT 1;                           
        """).fetchone()[0]
        yellow_full_heavy_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY hour_of_day ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        yellow_full_light_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY hour_of_day ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        green_2024_heavy_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY hour_of_day ORDER BY total DESC LIMIT 1;                           
        """).fetchone()[0]
        green_2024_light_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY hour_of_day ORDER BY total ASC LIMIT 1;                           
        """).fetchone()[0]
        green_full_heavy_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY hour_of_day ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        green_full_light_hour = con.execute(f"""
            SELECT hour_of_day, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY hour_of_day ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        print("Hour of day with highest CO2 emissions for yellow taxis 2024:", yellow_2024_heavy_hour)
        print("Hour of day with lowest CO2 emissions for yellow taxis 2024:", yellow_2024_light_hour)
        print("Hour of day with highest CO2 emissions for green taxis 2024:", green_2024_heavy_hour)
        print("Hour of day with lowest CO2 emissions for green taxis 2024:", green_2024_light_hour)
        print("Hour of day with highest CO2 emissions for yellow taxis from 2015 to 2024:", yellow_full_heavy_hour)
        print("Hour of day with lowest CO2 emissions for yellow taxis from 2015 to 2024:", yellow_full_light_hour)
        print("Hour of day with highest CO2 emissions for green taxis from 2015 to 2024:", green_full_heavy_hour)
        print("Hour of day with lowest CO2 emissions for green taxis from 2015 to 2024:", green_full_light_hour)
        logger.info("Calculated hour of day with highest and lowest CO2 emissions for yellow and green taxis")

        #most carbon heavy and carbon light days of the week
        yellow_2024_heavy_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY day_of_week ORDER BY total DESC LIMIT 1;                           
        """).fetchone()[0]
        yellow_2024_light_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY day_of_week ORDER BY total ASC LIMIT 1;                           
        """).fetchone()[0]
        yellow_full_heavy_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY day_of_week ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        yellow_full_light_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY day_of_week ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        green_2024_heavy_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY day_of_week ORDER BY total DESC LIMIT 1;                           
        """).fetchone()[0]
        green_2024_light_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY day_of_week ORDER BY total ASC LIMIT 1;                           
        """).fetchone()[0]
        green_full_heavy_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY day_of_week ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        green_full_light_dow = con.execute(f"""
            SELECT day_of_week, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY day_of_week ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        print("Day of week with highest CO2 emissions for yellow taxis 2024:", days[yellow_2024_heavy_dow])
        print("Day of week with lowest CO2 emissions for yellow taxis 2024:", days[yellow_2024_light_dow])
        print("Day of week with highest CO2 emissions for green taxis 2024:", days[green_2024_heavy_dow])
        print("Day of week with lowest CO2 emissions for green taxis 2024:", days[green_2024_light_dow])
        print("Day of week with highest CO2 emissions for yellow taxis from 2015 to 2024:", days[yellow_full_heavy_dow])
        print("Day of week with lowest CO2 emissions for yellow taxis from 2015 to 2024:", days[yellow_full_light_dow])
        print("Day of week with highest CO2 emissions for green taxis from 2015 to 2024:", days[green_full_heavy_dow])
        print("Day of week with lowest CO2 emissions for green taxis from 2015 to 2024:", days[green_full_light_dow])
        logger.info("Calculated day of week with highest and lowest CO2 emissions for yellow and green taxis")

        #most carbon heavy and carbon light weeks of the year
        yellow_2024_heavy_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY week_of_year ORDER BY total DESC LIMIT 1;                           
        """).fetchone()[0]
        yellow_2024_light_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY week_of_year ORDER BY total ASC LIMIT 1;                           
        """).fetchone()[0]
        yellow_full_heavy_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY week_of_year ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        yellow_full_light_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY week_of_year ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        green_2024_heavy_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY week_of_year ORDER BY total DESC LIMIT 1;                           
        """).fetchone()[0]
        green_2024_light_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY week_of_year ORDER BY total ASC LIMIT 1;                           
        """).fetchone()[0]
        green_full_heavy_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY week_of_year ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        green_full_light_woy = con.execute(f"""
            SELECT week_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY week_of_year ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        print("Week of year with highest CO2 emissions for yellow taxis 2024:", yellow_2024_heavy_woy)
        print("Week of year with lowest CO2 emissions for yellow taxis 2024:", yellow_2024_light_woy)
        print("Week of year with highest CO2 emissions for green taxis 2024:", green_2024_heavy_woy)
        print("Week of year with lowest CO2 emissions for green taxis 2024:", green_2024_light_woy)
        print("Week of year with highest CO2 emissions for yellow taxis from 2015 to 2024:", yellow_full_heavy_woy)
        print("Week of year with lowest CO2 emissions for yellow taxis from 2015 to 2024:", yellow_full_light_woy)
        print("Week of year with highest CO2 emissions for green taxis from 2015 to 2024:", green_full_heavy_woy)
        print("Week of year with lowest CO2 emissions for green taxis from 2015 to 2024:", green_full_light_woy)
        logger.info("Calculated week of year with highest and lowest CO2 emissions for yellow and green taxis")

        #most carbon heavy and carbon light months of the year
        yellow_2024_heavy_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY month_of_year ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        yellow_2024_light_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY month_of_year ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        yellow_full_heavy_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY month_of_year ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        yellow_full_light_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY month_of_year ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        green_2024_heavy_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY month_of_year ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        green_2024_light_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY month_of_year ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        green_full_heavy_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY month_of_year ORDER BY total DESC LIMIT 1;
        """).fetchone()[0]
        green_full_light_moy = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY month_of_year ORDER BY total ASC LIMIT 1;
        """).fetchone()[0]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        print("Month of year with highest CO2 emissions for yellow taxis 2024:", months[yellow_2024_heavy_moy - 1])
        print("Month of year with lowest CO2 emissions for yellow taxis 2024:", months[yellow_2024_light_moy - 1])
        print("Month of year with highest CO2 emissions for green taxis 2024:", months[green_2024_heavy_moy - 1])
        print("Month of year with lowest CO2 emissions for green taxis 2024:", months[green_2024_light_moy - 1])
        print("Month of year with highest CO2 emissions for yellow taxis from 2015 to 2024:", months[yellow_full_heavy_moy - 1])
        print("Month of year with lowest CO2 emissions for yellow taxis from 2015 to 2024:", months[yellow_full_light_moy - 1])
        print("Month of year with highest CO2 emissions for green taxis from 2015 to 2024:", months[green_full_heavy_moy - 1])
        print("Month of year with lowest CO2 emissions for green taxis from 2015 to 2024:", months[green_full_light_moy - 1])
        logger.info("Calculated month of year with highest and lowest CO2 emissions for yellow and green taxis")

        #time series with month co2 total for yellow and green taxis 2024
        import matplotlib.pyplot as plt
        yellow_2024_monthly = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_2024
            GROUP BY month_of_year ORDER BY month_of_year;
        """).fetchdf()
        green_2024_monthly = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_2024
            GROUP BY month_of_year ORDER BY month_of_year;
        """).fetchdf()
        plt.figure(figsize=(10, 6))
        plt.plot(yellow_2024_monthly['month_of_year'], yellow_2024_monthly['total'], label='Yellow Taxi', color='gold')
        plt.plot(green_2024_monthly['month_of_year'], green_2024_monthly['total'], label='Green Taxi', color='green')
        plt.xticks(range(1, 13), months) 
        plt.yscale('log')   
        plt.xlabel('Month of Year')
        plt.ylabel('CO2 Total Emissions (kilograms)')
        plt.title('Monthly Total CO2 Emissions for Yellow and Green Taxis in 2024')
        plt.legend()
        plt.grid()
        plt.savefig('monthly_co2_emissions_2024.png')
        plt.close()
        print("Monthly CO2 emissions plot saved as monthly_co2_emissions.png")
        logger.info("Monthly CO2 emissions plot saved as monthly_co2_emissions.png")

        #time series with month co2 total for yellow and green taxis across all years
        yellow_full_monthly = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM yellow_tripdata_full
            GROUP BY month_of_year ORDER BY month_of_year;
        """).fetchdf()
        green_full_monthly = con.execute(f"""
            SELECT month_of_year, SUM(trip_co2_kgs) AS total
            FROM green_tripdata_full
            GROUP BY month_of_year ORDER BY month_of_year;
        """).fetchdf()
        plt.figure(figsize=(10, 6))
        plt.plot(yellow_full_monthly['month_of_year'], yellow_full_monthly['total'], label='Yellow Taxi', color='gold')
        plt.plot(green_full_monthly['month_of_year'], green_full_monthly['total'], label='Green Taxi', color='green')
        plt.xticks(range(1, 13), months)
        plt.yscale('log')
        plt.xlabel('Month of Year')
        plt.ylabel('CO2 Total Emissions (kilograms)')
        plt.title('Monthly Total CO2 Emissions for Yellow and Green Taxis (2015-2024)')
        plt.legend()
        plt.grid()
        plt.savefig('monthly_co2_emissions_full.png')
        plt.close()


    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    analysis()