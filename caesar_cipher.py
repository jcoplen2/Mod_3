#cipher example

FIRST_CHAR_CODE = 65
LAST_CHAR_CODE = 90
CHAR_RANGE = 26

def caesar_shift(message, shift):

    result = ""

#shift each letter in the message
    for x in message.upper():
        if x.isalpha():
            char_code = ord(x)
            new_code = char_code + shift
        
            if new_code > LAST_CHAR_CODE:
                new_code -= CHAR_RANGE
            if new_code < FIRST_CHAR_CODE:
                new_code += CHAR_RANGE

            new_char = chr(new_code)
            result += new_char
        else:
            result += x

    print(result)

caesar_shift("Hello, World!", 7)
caesar_shift("OLSSV, DVYSK!", -7)