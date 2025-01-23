def main():
   book_path = "books/frankenstein.txt"
   text = book_text(book_path)
   word_count = count(text)
   char_count = unique_characters(text)
   sorted_characters = sort_on(char_count)
   print(f"--- Begin report of {book_path} ---")
   print(word_count, "words found in the document")
   for i in sorted_characters:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    
def count(text):
    words = text.split()
    return len(words)

def book_text(book_path):
    with open(book_path) as f:
        return f.read()

def unique_characters(text):
    characters_dict = {
        
    }
    lowered_text = text.lower()
    for i in lowered_text:
        if i.isalpha():
            if i in characters_dict:
                characters_dict[i] += 1
            else:
                characters_dict[i] = 1
    return characters_dict

def sort_on(char_count):
    sorted_char_dict_list = []
    for char, count in char_count.items():
        sorted_char_dict_list.append({"char": char, "num": count})
    sorted_char_dict_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_char_dict_list
main()