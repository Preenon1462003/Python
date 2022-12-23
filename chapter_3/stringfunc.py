word="Hello my name is Preenon . I live in Malda which is located in WestBengal. I am currently pursuing CSE from KIIT University."

print("The sentence is :\n",word)
print("Length of the sentence:\n",len(word))
print("Find the word Preenon:\n", word.find("Preenon"))
print("Total number of time when the a term came in the sentence:\n",word.count("a"))
print("Replace Preenon with Saha:\n", word.replace("Preenon","Saha"))
print("Does the string ends with ity:\n", word.endswith("ity."))