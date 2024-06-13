# Chapter 4 Comma Code function
# A function that takes a list value as an argument and returns a string with
# all the items separated by a comma and a space, with and inserted before 
# the last item

def comma_coder(word_list):
    if len(word_list) == 0:
        print('You need items in the list')
        return
    elif len(word_list) == 1:
        print(str(word_list[0]))
        return
    else:
        word_string = ''
        while len(word_list) > 1:
            for i in word_list:
                word_string += str(word_list.pop(0)) + ', '
        word_string += 'and ' + str(word_list.pop(-1))
        print(word_string)

print('Empty list')
comma_coder([])

print("['cat', 'dog', 'mouse']")
comma_coder(['cat', 'dog', 'mouse', 3])

print("[cat]")
comma_coder(['cat', ])

print("['cat', 'dog', 'mouse']")
comma_coder(['cat', 'dog', 'mouse'])