import random
def can_construct(word, letters):
    """
    word - type: str
	letters - type: str
	return value - type: bool
	"""
    if len(word) != len(letters):
        return False
    else:
        for i in word:
            if word.count(i) != letters.count(i):
                return False
            else:
                pass
        return True


print(can_construct("apples", "appels"))


# other solution: create a dictionary and increment value for each instance of key