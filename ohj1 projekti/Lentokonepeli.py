import mysql.connector
import random
from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c
    return distance


def get_random_countries(num_countries=2):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="apina5223",
        database="Flight_game"
    )
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM country WHERE continent = 'EU' ORDER BY RAND() LIMIT %s", (num_countries,))
        countries = cursor.fetchall()
        return countries
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
    finally:
        cursor.close()
        conn.close()


def select_country_option(countries, coins):
    print("Select a country option:")
    for i, country in enumerate(countries):
        print(f"{i + 1}. {country[1]}")
    print(f"{len(countries) + 1}. Stay in the same country")
    print(f"Coins available: {coins}")
    choice = input("Enter your choice: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(countries) + 1:
            if choice <= len(countries):
                cost = 40
            else:
                cost = 5
            if coins >= cost:
                coins -= cost
                print(f"Coins deducted: {cost}")
                return countries[choice - 1][1] if choice <= len(countries) else None, coins
            else:
                print("Insufficient coins. You need more coins for this flight.")
                return None, coins
        else:
            print("Invalid choice.")
            return None, coins
    else:
        print("Invalid choice.")
        return None, coins


def select_airport_option(airports, coins):
    print("Select an airport option:")
    for i, airport in enumerate(airports):
        print(f"{i + 1}. {airport[3]}")
    print(f"{len(airports) + 1}. Return to main menu")
    print(f"Coins available: {coins}")
    choice = input("Enter your choice: ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(airports):
            if coins >= 40:
                if choice <= len(airports):  # If flying within the same country
                    coins -= 5
                    print("Coins... -5")
                else:  # If flying to another country
                    coins -= 40
                    print("Coins... -40")
                return airports[choice - 1], coins
            else:
                print("Insufficient coins. You need 40 coins to fly to another country.")
                return None, coins
        elif choice == len(airports) + 1:
            return None, coins
        else:
            print("Invalid choice.")
            return None, coins
    else:
        print("Invalid choice.")
        return None, coins


def get_random_airport_in_europe():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="apina5223",
        database="Flight_game"
    )
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM airport WHERE continent = 'EU' ORDER BY RAND() LIMIT 1")
        airport = cursor.fetchone()
        return airport
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
    finally:
        cursor.close()
        conn.close()


def get_neighboring_countries(current_lat, current_lon, limit=3):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="apina5223",
        database="Flight_game"
    )
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM country WHERE continent = 'EU'")
        countries = cursor.fetchall()

        if not countries:
            print("No neighboring countries found.")
            return None
        else:
            # Randomly select 3 neighboring countries
            neighboring_countries = random.sample(countries, min(limit, len(countries)))
            return neighboring_countries
    except Exception as e:
        print("Error fetching neighboring countries:", e)
        return None
    finally:
        cursor.close()
        conn.close()


def get_airports_in_selected_country(country_iso, num_airports=3):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="apina5223",
        database="Flight_game"
    )
    cursor = conn.cursor()

    try:
        sql_query = "SELECT * FROM airport WHERE iso_country = %s AND type NOT IN ('heliport', 'helipad') ORDER BY RAND() LIMIT %s"
        print("SQL Query:", sql_query)
        print("Parameters:", (country_iso, num_airports))

        cursor.execute(sql_query, (country_iso, num_airports))
        airports = cursor.fetchall()

        print("Number of airports:", len(airports))  # Print the number of airports retrieved
        print("Airports:", airports)  # Print the airports retrieved

        return airports
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
    finally:
        cursor.close()
        conn.close()


def travel_between_countries(current_lat, current_lon, destination_lat, destination_lon, current_points):
    print("Traveling from one country to another...")

    current_lat += random.uniform(-1, 1)
    current_lon += random.uniform(-1, 1)

    distance_to_destination = haversine(current_lat, current_lon, destination_lat, destination_lon)

    if distance_to_destination < current_points:
        points_gained = 2  # Gain 3 points if getting closer
        current_points += points_gained
        print("You're getting closer to the final destination. Gained {} points.".format(points_gained))
    else:
        points_lost = 1  # Lose 1 point if getting further away
        current_points -= points_lost
        print("You're moving away from the final destination. Lost {} point.".format(points_lost))

    print("You've arrived in a new country!")
    print("Current Latitude:", current_lat)
    print("Current Longitude:", current_lon)

    return current_lat, current_lon, current_points


# Function to get a random country in Europe
def get_random_european_country():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="apina5223",
        database="Flight_game"
    )
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name FROM country WHERE continent = 'EU' ORDER BY RAND() LIMIT 1")
        country = cursor.fetchone()
        if country:
            return country[0]
        else:
            return None
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
    finally:
        cursor.close()
        conn.close()

# Function to get a random airport in a given country
def get_random_airport_in_country(country):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="apina5223",
        database="Flight_game"
    )
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name FROM airport WHERE iso_country = %s ORDER BY RAND() LIMIT 1", (country,))
        airport = cursor.fetchone()
        if airport:
            return airport[0]
        else:
            return None
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
    finally:
        cursor.close()
        conn.close()

# Select a random final destination
final_destination_country = get_random_european_country()
final_destination_airport = get_random_airport_in_country(final_destination_country)

print("Goal Destination:", final_destination_country)


def main():
    attempts = 0
    closer_attempts = 0
    max_attempts_before_hint = 10
    current_lat = None
    current_lon = None
    current_points = 0
    coins = 500
    starting_airport = None

    while True:
        if starting_airport is None:
            starting_airport = get_random_airport_in_europe()
            if starting_airport:
                print("Starting Airport:", starting_airport[3])  # Assuming airport name is in the fourth column
                current_lat, current_lon = float(starting_airport[4]), float(starting_airport[5])
                destination_lat = float(starting_airport[4])  # Assuming latitude is stored in the fifth column
                destination_lon = float(starting_airport[5])  # Assuming longitude is stored in the sixth column

        print("\nCurrent Airport:", starting_airport[3])  # Print current airport
        #print("Current Points:", current_points)  # Print current points
        print("Coins left:", coins)
        print("\nOptions:")
        print("1. Choose a neighboring country")
        print("2. Choose an airport in the same country")
        print("3. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            neighboring_countries = get_neighboring_countries(current_lat, current_lon)
            selected_country, coins = select_country_option(neighboring_countries, coins)
            if selected_country is not None:
                print("Selected country:", selected_country)
                attempts += 1
                if selected_country == final_destination_country:
                    print("You've reached the final destination! Game over.")
                    break
                if attempts % max_attempts_before_hint == 0:
                    print("You've made", max_attempts_before_hint, "attempts. Getting closer to the destination.")
                    closer_attempts += 1
                closer_attempts = 0  # Reset closer_attempts when choosing a new country
                confirm = input("Are you sure you want to choose this country? (yes/no): ")
                if confirm.lower() == "yes":
                    if selected_country is not None:
                        airports_in_country = get_airports_in_selected_country(selected_country)
                        if airports_in_country:
                            selected_airport, coins = select_airport_option(airports_in_country, coins)
                            if selected_airport:
                                print("Selected airport:", selected_airport[3])
                                attempts += 1
                                if selected_airport[3] == final_destination_airport:
                                    print("You've reached the final destination! Game over.")
                                    break
                                if attempts % max_attempts_before_hint == 0:
                                    print("You've made", max_attempts_before_hint, "attempts. Getting closer to the destination.")
                                    closer_attempts += 1
                                current_lat, current_lon, current_points = travel_between_countries(current_lat,
                                                                                                    current_lon,
                                                                                                    float(selected_airport[4]),
                                                                                                    float(selected_airport[5]),
                                                                                                    current_points)
                                starting_airport = selected_airport  # Update starting airport here
        elif choice == "2":
            if starting_airport:
                airports_in_country = get_airports_in_selected_country(starting_airport[8])
                if airports_in_country:  # Check if airports are available in the current country
                    selected_airport, coins = select_airport_option(airports_in_country, coins)
                    if selected_airport:
                        print("Selected airport:", selected_airport[3])
                        attempts += 1
                        if selected_airport[3] == final_destination_airport:
                            print("You've reached the final destination! Game over.")
                            break
                        if attempts % max_attempts_before_hint == 0:
                            print("You've made", max_attempts_before_hint, "attempts. Getting closer to the destination.")
                            closer_attempts += 1
                        current_lat, current_lon, current_points = travel_between_countries(current_lat,
                                                                                            current_lon,
                                                                                            float(selected_airport[4]),
                                                                                            float(selected_airport[5]),
                                                                                            current_points)
                        starting_airport = selected_airport  # Update starting airport here
                else:
                    print("No airports available in the current country.")
            else:
                print("No starting airport selected.")
        elif choice == "3":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        if closer_attempts == 3:
            print("You're getting closer to the destination.")
            closer_attempts = 0

if __name__ == "__main__":
    main()
