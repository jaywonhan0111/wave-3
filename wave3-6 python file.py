def find_first_vowel(word):
    
    cur_ind = 0

   

    while (cur_ind < len(word)) and (word[cur_ind] not in "aeiou"):
        cur_ind += 1
    return cur_ind

def for_loop_ver(word):
    for ind, letter in enumerate(word):
        if letter in "aeiou":
            return ind

def pig_latin(word):
    if word.lower()[0] in "aeiou":
        return word + "way"
    else:
        first_vowel = find_first_vowel(word)

       
        return word[first_vowel : ] + word[ : first_vowel] + "ay"

def main():
    word = input("Enter a word: ")
    translated = pig_latin(word)
    print("Translated to:", translated)

if __name__ == "__main__":
    main()