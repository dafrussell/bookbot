def main():
    path_to_file = "books/frankenstein.txt"
    book_contents = get_contents(path_to_file)
    book_wordcount = get_wordcount(book_contents)
    letter_count = calc_lettercount(book_contents)
    letter_count_report = generate_letter_report(letter_count)


    # Print report (output)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"There are {book_wordcount} words present in this book")
    print("")
    for string in letter_count_report:
        print(f"{string}")
    print("")
    print("--- End of report ---")


def get_contents(filepath_tobook):
    with open(filepath_tobook, 'r') as file:
        file_contents = file.read()
        return file_contents

def get_wordcount(text):
        wordcount = len(text)
        return wordcount
    
def calc_lettercount(words):
        # Put words into lower case
        all_as_lower = words.lower()

        # Split the lower case text into strings by word
        all_as_lower_aswords = all_as_lower.split()
        
        # Save the values of each character into a list
        all_characters = []
        list(map(all_characters.extend, all_as_lower_aswords))

        # Calculate each characters occurence from all_characters list
        dict = {}
        for char in all_characters:
            if char in dict:
                dict[char] += 1
            else:
                 dict[char] = 1
            
        return dict
def generate_letter_report(top_level_dict):

    # Order keys in inputted dictionary
    sort_dict = sorted(top_level_dict.keys())
    output = []

    # Populate output list by iteration
    for item in sort_dict:
         
         # Only add keys to list if alphabetical
         if item.isalpha() == True:
                list_item = f"The letter {item} appears was found {top_level_dict[item]} times"
                output.append(list_item)
    return output

main()