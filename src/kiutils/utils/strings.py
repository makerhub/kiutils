"""Functions for string manipulation

Author:
    (C) Marvin Mager - @mvnmgrx - 2022

License identifier:
    GPL-3.0

Major changes:
    28.02.2022 - created
"""

def dequote(input: str) -> str:
    """Escapes double-quotes in a string using a backslash

    Args:
        - input (str): String to replace double-quotes

    Returns:
        - str: String with replaced double-quotes
    """
    return str(input).replace("\"", "\\\"")


def remove_prefix(input: str, prefix: str) -> str:
    """Removes the given prefix from a string (to remove incompatibility of ``str.removeprefix()``
    for Python versions < 3.9)

    Args:
        - input (str): String to remove the prefix from
        - prefix (str): The prefix

    Returns:
        - str: String with removed prefix, or the ``input`` string as is, if the prefix was not found
    """
    return input[len(prefix):] if input.startswith(prefix) else input

def float_to_kicad_str(number: float, precision: int = None) -> str:
    """Converts a float to a string, adding or removing trailing zeros based on the specified precision

    Args:
        - number (float): Number to convert
        - precision (int, optional): Number of digits of precision

    Returns:
        - str: Number as string
    """
    if precision is not None:
        format_str = f"{{:.{precision}f}}"
        formatted_number = format_str.format(number)
        if '.' in formatted_number:
            integer_part, decimal_part = formatted_number.split('.')
            if len(decimal_part) < precision:
                formatted_number = f"{integer_part}.{decimal_part.ljust(precision, '0')}"
        return formatted_number       
    return str(number).rstrip('0').rstrip('.') if '.' in str(number) else str(number)