'''
  PROBLEM DEFINITION
  -----------------
  Reverse each word in the input string.
  The order of the words will be unchanged.
  A word is made upof letters and/or numbers.
  Other characters (spaces, punctuation) will not be reversed.

  NOTES
  -----
  Write production quality code
  We prefer clarity over performance (though if you can achieve both- great!)
  You can use the language that best highlights your programming ability. 
  In this Assignment, I will be using Python to perform my codes.

'''
def reverse_words(s: str) -> str:
    index = 0
    word = s.split(' ')
    result = []

    for each in word:
        for i in each
            if i.isalpha() or i.isdigit():
                result.append(i)
    


    for each in word:

        if word in each.isalnum():
            result.append(temp[index])





            


if __name__ == '__main__':
    # Example usage
    input_string = "String; 2be reversed..."
    reversed_words = reverse_words(input_string)