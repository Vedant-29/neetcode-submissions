from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set()

    for item in words:
        if item in my_set:
            return True

        my_set.add(item)
    return False        

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
