def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    character_counts = count_chars(file_contents.lower())
    chars_sorted_list = dict_to_sorted_list(character_counts)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

    print(f'chars: {character_counts}')

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    output = {}
    for char in text:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output

def sort_on(d):
    return d["num"]

def dict_to_sorted_list(d):
    sorted_list = []
    for char in d:
        sorted_list.append({"char": char, "num": d[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

if __name__ == "__main__":
    main()
