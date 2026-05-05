# On this project i will to review the fundamentals of python, like lists, enumarate(), unpacking, none as a default value, if __name__ == "__main__", and list comprehensions. I will to create a simple program that receives a list of weather reports for different cities, and then it will print the coldest city among them. Each report will include the city name, temperature, and weather condition.


def main():

    coldest_city = None

    reports = [
        ("Lima", 18.2, "Parcialmente nublado"),
        ("Trujillo", 23.1, "Despejado"),
        ("Arequipa", 12.8, "Nublado"),
        ("Cusco", 9.4, "Lluvia leve"),
    ]

    for i, (city, temp, condition) in enumerate(reports, start=1):
        if coldest_city is None or temp < coldest_city[1]:
            coldest_city = (city, temp)
        print(f"{i}. {city:<10} -> {temp:>5}°C, {condition}")

    print(f"\nThe coldest city is {coldest_city[0]} with {coldest_city[1]}°C.")

    warm_cities = [city for city, temp, _ in reports if temp > 15]

    print(f"Cities with temperatures above 15°C: {warm_cities}")


if __name__ == "__main__":
    main()
