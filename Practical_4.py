def change_case(text, style):
    if style == 'c' or style == 'C':
        return cap(text)
    elif style == 's' or style == 'S':
        return small(text)
    elif style == 'r' or style == 'R':
        return reverse(text)
    elif style == 'u' or style == 'U':
        return alter(text)
    else:
        return "Enter valid Input"


def cap(text):
    ans = ""
    for i in range(len(text)):
        if text[i] >= 'a' and text[i] <= 'z':
            ans += chr(ord(text[i]) - 32)  # Convert lowercase to uppercase
        else:
            ans += text[i]  # If not a lowercase letter, just append as is
    return ans


def small(text):
    ans = ""
    for i in range(len(text)):
        if text[i] >= 'A' and text[i] <= 'Z':
            ans += chr(ord(text[i]) + 32)  # Convert uppercase to lowercase
        else:
            ans += text[i]
    return ans


def reverse(text):
    ans = ""
    for i in range(len(text)):
        if text[i] >= 'A' and text[i] <= 'Z':
            ans += chr(ord(text[i]) + 32)  # Convert uppercase to lowercase
        elif text[i] >= 'a' and text[i] <= 'z':
            ans += chr(ord(text[i]) - 32)  # Convert lowercase to uppercase
        else:
            ans += text[i]
    return ans


def alter(text):
    ans = ""
    flag = True  # Start with flag as True for alternating case
    for i in range(len(text)):
        if text[i] >= 'a' and text[i] <= 'z':  # For lowercase
            if flag:
                ans += chr(ord(text[i]) - 32)  # Convert to uppercase
            else:
                ans += text[i]
            flag = not flag  # Alternate the flag
        elif text[i] >= 'A' and text[i] <= 'Z':  # For uppercase
            if flag:
                ans += text[i]
            else:
                ans += chr(ord(text[i]) + 32)  # Convert to lowercase
            flag = not flag  # Alternate the flag
        else:
            ans += text[i]  # If not a letter, just append it
    return ans


# Test case
print(change_case("*-+&&&543###Tanmay Raut", 'u'))

