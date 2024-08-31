def ends_with_a(text):
    if not text:
        return "Rejected"
    return "Accepted" if text[-1] == 'a' else "Rejected"


def base(text, input_base, output_base):
    if not (2 <= input_base <= 36) and not (2 <= output_base <= 36):
        raise ValueError('Base must be between 2 and 36')

    dec_value = int(text, input_base)
    if dec_value == 0:
        return "0"
    
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    
    while dec_value > 0:
        dec_value, remainder = divmod(dec_value, output_base)
        result.append(digits[remainder])
    
    return ''.join(reversed(result))


def slice_string(text, start=0, end=None, step=1):
    return text[start:end:step]


def con1(text):
    return slice_string(text)


def con2(text, slicing_parameters):
    start, end, step = slicing_parameters
    return slice_string(text, start, end, step)


def int_to_roman(num):
    value_symbol_pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = []
    
    for value, symbol in value_symbol_pairs:
        if num == 0:
            break
        count, num = divmod(num, value)
        result.append(symbol * count)
    
    return ''.join(result)


# Test the functions
print(int_to_roman(56))  # Outputs: LVI
print(con2("programming", [len("programming") - 1, -1, -1]))  # Outputs: gnimmargorp
print(base('1100', 2, 16))  # Outputs: C
print(ends_with_a("babaabbaba"))  # Outputs: Rejected
