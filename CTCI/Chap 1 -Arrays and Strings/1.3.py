def urlify(input):
    input = input.strip()
    output = ""
    for c in input:
        if c == " ":
            output += "%20"
        else:
            output += c

    return output

print(urlify("Mr John Smith    "))