#1 Sort an array of numbers WITHOUT USING.sort()
# array = [4,2,7,4,3,8,10,8,44]
# new_array = []

# while array:
#     value = array[0]
#     for x in array:
#         if x < value:
#             value = x 
#     new_array.append(value)
#     array.remove(value)


# print(new_array)

#2 Swap two numbers without a third variable 
# a = 30
# b = 5 

# a = 30 
# b = 5

# a = a + b
# b = a - b
# a = a - b

# print(a,b)




# #3 Find the longest word in a sentence
# sentence = 'This sentence is a good example.'
# sentence_words = sentence.split()
# longest_word = ''
# longest_size = 0

# for word in sentence_words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print(longest_word) 


# #4 Count each letter in a sentence, find the most used letter
sentence = 'This sentence is a good example.'

let_count = {}

for letters in sentence:
    let_count[letters] = let_count.get(letters, 0) + 1
    inverse = [(value, key) for key, value in let_count.items()]

print(max(inverse)[1])