# write a function number of palandrome in the string

# def count_palindrome(sentance):
    
#     sentence=sentence.split(" ")
#     count=0
#     for word in word(len(sentence)):
#      if sentence[word][::-1] == sentence[word]:
#          palindrome_exists=True
#          count+=1
#          print("palindromes present in this string")
#     if palindrome_exists==False:
#         print("hear there is no palindromes")
        
#         sentence="my family comsists of amma anna nanna akka"
         
#     count_palindrome(sentence)
    
#     print("hear",count_palindrome(sentence),"present")

# def count_palindrome(sentence):
#     words = sentence.split(" ")
#     count = 0
#     palindrome_exists = False

#     for word in words:
#         word = word.strip()
#         if word == word[::-1]:
#             palindrome_exists = True
#             count += 1
#             print("palindrome present:", word)

#     if not palindrome_exists:
#         print("Here there are no palindromes")
#     else:
#         print("Total palindromes in string:", count)


# sentence = "my family consists of amma anna nanna akka"
# count_palindrome(sentence)



def count_palindrome(sentence):
    sentence=sentence.split(" ")
    count=0
    palindrome_exists=False
    
    for k in range(len(sentence)):
        word=sentence[k].strip()
        if word == word[::-1]:
            palindrome_exists = True
            count+=1
            print("Palindrome present:",word)
            
    if not palindrome_exists:
        print("Here there are no palindromes")
    else:
        print("Total palindromes in string:", count)
        
    sentence = "apple level wow eye"
    count_palindrome(sentence)  

        
        
        
        
        