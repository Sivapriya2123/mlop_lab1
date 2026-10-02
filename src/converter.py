def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number.")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Temperature must be a number.")
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number.")

    kelvin = celsius + 273.15

    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero.")

    return kelvin


def kelvin_to_celsius(kelvin):
    if not isinstance(kelvin, (int, float)):
        raise ValueError("Temperature must be a number.")

    if kelvin < 0:
        raise ValueError("Kelvin cannot be negative.")

    return kelvin - 273.15