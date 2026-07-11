from geeztranslit import geez_to_latin, latin_to_geez


def is_geez(text):
    """
    Check if text contains Ethiopic (Geez) characters.
    """
    for char in text:
        if "\u1200" <= char <= "\u137F":
            return True
    return False


def translate(text):
    """
    Automatically translate Geez <-> Latin.
    """
    if is_geez(text):
        return geez_to_latin(text)
    else:
        return latin_to_geez(text)


print("=================================")
print(" Fidel Geez ↔ Latin Translator")
print(" Type 'exit' to close")
print("=================================")

while True:
    user_input = input("\nEnter text: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.strip() == "":
        continue

    result = translate(user_input)

    print("Translation:", result)