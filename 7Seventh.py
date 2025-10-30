from Signature_folder.Signature import sign
number_type = 23 #This is a number data type
text_type = "Hello this is a string" #This is a string data type
float_type = 3.14 #This is a float type data type
list_type = {1,2,3,4,5} #This is list type data type
tuple_type = (1,2,3,4,5) #This is a tuple type data type
dictionary_type = {"Yash":15,
                   "Soumil r":32,
                   "Soumil m":42,
                   "Ankit":7}
def showTypes():
    print(type(number_type))
    print(type(text_type))
    print(type(float_type))
    print(type(list_type))
    print(type(tuple_type))
    print(type(dictionary_type))

showTypes()
sign()