#takes a string and  counts the number  of words
def word_count(book):
    word_list = book.split()
    num_of_words = len(word_list)
    return num_of_words

#takes a string and  counts the number of characters
def char_count(book):
    book = book.lower()
    charlist  = {}
    for letter in book:
        if letter not in charlist:
            charlist[letter] = 0


    for letter in  book:
        if letter in charlist:
            charlist[letter] +=1
    return(charlist)


        
