from collections import Counter


def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        print(file_contents)

        word_count = len(file_contents.split())
        
        
        
        char_count = Counter(file_contents)

        

        char_list = []

        for char, count in char_count.items():
            if char.isalpha():
                char_dict = {"char": char, "count": count}
                char_list.append(char_dict)

        

        char_list.sort(key=lambda x: x['count'], reverse=True)  # Sorts the list

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        
        for item in char_list:
            print(f"The '{item['char']}' character was found {item['count']} times")
        
        print("--- End report ---")



        
if __name__ == "__main__":
    main()
