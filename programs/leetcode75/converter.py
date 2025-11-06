import typing
class NumberFormats:
    """
    NumberFormats names
    """

    BINARY = "binary"
    DECIMAL = "decimal"
    HEXADECIMAL = "hexadecimal"
    
def convert_hexadecimal(
    numbers: list,
    to: typing.Optional[str] = "binary",
    bit_width: typing.Optional[int] = 64,
):
    """Converts the hexadecimal number to required format.

    Args:
        numbers: Numbers in list
        to: type to be converted
        bit_width: bit_width number

    returns:
        After converting this method will return a dictionary.

    """
    converted_numbers = {}
    for number in numbers:
        if to == NumberFormats.BINARY:
            converted_numbers[number] = f"{int(number):0{bit_width}b}"
        elif to == NumberFormats.DECIMAL:
            converted_numbers[number] = f"{int(str(number), 16):0{bit_width}}"
        elif to == NumberFormats.HEXADECIMAL:
            converted_numbers[number] = number
    
    return converted_numbers
    


# x = convert_hexadecimal(numbers=[25,32,5,8],to='binary',bit_width=8)
# print(x)

import re
ret = "Bios Knob devices does not currently exist"
# out = re.findall(r"available values for the knob (.*)\n", ret, re.I | re.M)
# print(out)
if (f'Bios Knob devices does not currently exist' in ret
    or f"Verify Fail: Knob = devices" in ret
):
    print(f"Setting up the bios knob Failed for devices")
else:
    print("sample needed")
