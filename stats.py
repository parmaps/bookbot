def count_words(book_text):
    words = book_text.lower().split()    
    
    return len(words)

def count_characters(book_text):
    words = book_text.lower().split()
    chars_count = {}

    for word in words:
        for char in word:                                   
            chars_count[char] = chars_count.get(char, 0) + 1
    
    return chars_count


# A function that takes a dictionary and returns the value of the "count" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

def sort_dictionaries(chars_count):
    sorted_dictionaries = []

    for (key, value) in chars_count.items():
        if key.isalpha():
            dict = {"char": key, "count": value}
            sorted_dictionaries.append(dict)
    
    sorted_dictionaries.sort(reverse=True, key=sort_on)

    return sorted_dictionaries
