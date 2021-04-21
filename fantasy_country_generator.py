import random
import countryInfo as countryInfo

def fantasy_country():

    # Generates a random number
    randomly_chosen_size = random.choice(range(1, 30))

    # Used to determine the country size
    country_size = randomly_chosen_size

    # Number of cities, towns and villages will be generated later on
    num_of_cities = 0
    num_of_towns = 0
    num_of_villages = 0
    population = 0

    # If the number in randomly_chosen_size is smaller or equal to 10, then the country will be considered a small one.
    if country_size <= 10:
        print()
        print("Small Sized Country")
        print("----------------------------------------------------")
        # I might remove this later, but for the time being it is only used to help drive the fact that this is a small country.
        country_size = "small"
        # Here the cities, towns, and villages are generated, the amount of said places are determind by the country size.
        num_of_cities = random.choice(range(1, 5))
        num_of_towns = random.choice(range(1, 7))
        num_of_villages = random.choice(range(1, 10))
        country_name = random.choice(countryInfo.country_names)
        print("Country Name:", country_name)
        print("----------------------------------------------------")
        print("----------------------------------------------------")
        print()
        print("Num of Cities:", num_of_cities)
        print("----------------------------------------------------")
        print("Num of Towns:", num_of_towns)
        print("----------------------------------------------------")
        print("Num of Villages:", num_of_villages)
        print("----------------------------------------------------")
        print()
        print("City Names: ")
        print()
        city_names = random.sample(countryInfo.city_names, num_of_cities)
        for names in city_names:
            print(names)
        print()
        print("----------------------------------------------------")
        print()
        print("Town Names: ")
        print()
        town_names = random.sample(countryInfo.town_names, num_of_towns)
        for names in town_names:
            print(names)
        print()
        print("----------------------------------------------------")
        print()
        print("Village Names: ")
        print()
        village_names = random.sample(countryInfo.village_names, num_of_villages)
        for names in village_names:
            print(names)
        print()
        print("----------------------------------------------------")

    # If the number in randomly_chosen_size is greater than 10, and is smaller or equal to 20, then the country will be considered a medium one.
    elif country_size > 10 and country_size <= 20:
        print()
        print("Medium Sized Country")
        print("----------------------------------------------------")
        country_size = "medium"
        num_of_cities = random.choice(range(2, 7))
        num_of_towns = random.choice(range(2, 10))
        num_of_villages = random.choice(range(1, 15))
        country_name = random.choice(countryInfo.country_names)
        print("Country Name:", country_name)
        print("----------------------------------------------------")
        print("----------------------------------------------------")
        print()
        print("Num of Cities:", num_of_cities)
        print("----------------------------------------------------")
        print("Num of Towns:", num_of_towns)
        print("----------------------------------------------------")
        print("Num of Villages:", num_of_villages)
        print("----------------------------------------------------")
        print()
        print("City Names: ")
        print()
        city_names = random.sample(countryInfo.city_names, num_of_cities)
        for names in city_names:
            print(names)
        print()
        print("----------------------------------------------------")
        print()
        print("Town Names: ")
        print()
        town_names = random.sample(countryInfo.town_names, num_of_towns)
        for names in town_names:
            print(names)
        print()
        print("----------------------------------------------------")
        print()
        print("Village Names: ")
        print()
        village_names = random.sample(countryInfo.village_names, num_of_villages)
        for names in village_names:
            print(names)
        print()
        print("----------------------------------------------------")

    # If the number in randomly_chosen_size is greater than 20, and is smaller or equal to 30, then the country will be considered a large one.
    elif country_size > 20 and country_size <= 30:
        print()
        print("Large Sized Country")
        print("----------------------------------------------------")
        country_size = "large"
        num_of_cities = random.choice(range(3, 10))
        num_of_towns = random.choice(range(3, 15))
        num_of_villages = random.choice(range(1, 20))
        country_name = random.choice(countryInfo.country_names)
        
        print("Country Name:", country_name)
        print("----------------------------------------------------")
     
        print("----------------------------------------------------")
        print()
        print("Num of Cities:", num_of_cities)
        print("----------------------------------------------------")
        print("Num of Towns:", num_of_towns)
        print("----------------------------------------------------")
        print("Num of Villages:", num_of_villages)
        print("----------------------------------------------------")
        print()
        print("City Names: ")
        print()
        city_names = random.sample(countryInfo.city_names, num_of_cities)
        for names in city_names:
            print(names)
        print()
        print("----------------------------------------------------")
        print()
        print("Town Names: ")
        print()
        town_names = random.sample(countryInfo.town_names, num_of_towns)
        for names in town_names:
            print(names)
        print()
        print("----------------------------------------------------")
        print()
        print("Village Names: ")
        print()
        village_names = random.sample(countryInfo.village_names, num_of_villages)
        for names in village_names:
            print(names)
        print()
        print("----------------------------------------------------")

