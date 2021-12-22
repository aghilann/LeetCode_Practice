def last_word(s):
    return len(s.split()[-1])


print(last_word("Hello World"))  # -> 5
print(last_word("   fly me   to   the moon  "))  # -> 4
print(last_word("luffy is still joyboy"))  # -> 6
