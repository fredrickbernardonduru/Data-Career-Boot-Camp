wedef analyze_words(word)  
print("Total number of words:", len(words))
longest_word = max(words, key=len)
    print("Longest word:", longest_word)

    palindromes = [w for w in words if w == w[::-1]]

    if palindromes:
        print("Palindromes found:", palindromes)
    else:
        print("No Palindromes found") 

#Example usage
word_list = ['python', 'level', 'programming', 'radar', 'algorithm']
analyze_words(word_list)
word_list = ['python', 'level', 'programming', 'radar', 'algorithm']
analyze_words(word_list)
word_list = ['python', 'level', 'programming', 'radar', 'algorithm']
analyze_words(word_list)
word_list = ['python', 'level', 'programming', 'radar', 'algorithm']
analyze_words(word_list)
