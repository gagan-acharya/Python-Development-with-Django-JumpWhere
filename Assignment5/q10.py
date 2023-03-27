wordString = input("Input words: ")
word_list = wordString.split(",")
word_list.sort()
word_list2 = []
[word_list2.append(x) for x in word_list if x not in word_list2]
print((', ').join(word_list2))