def is_anagram1(string1, string2):
    if len(string1) != len(string2):
        print("Not same length")
    return sorted(string1.lower()) == sorted(string2.lower())

print(is_anagram1("listen", "SILent"))