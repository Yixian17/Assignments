"""
PROBLEM DEFINITION
-----------------
Reverse each word in the input string.
The order of the words will be unchanged.
A word is made up of letters and/or numbers.
Other characters (spaces, punctuation) will not be reversed.

NOTES
-----
Write production quality code
We prefer clarity over performance (though if you can achieve both- great!)
You can use the language that best highlights your programming ability.


As such in this Assignment1 and Assignment2, I will be using Python to write my codes.
"""


def reverse_words(s: str) -> str:
    # split the whole string into individual words
    word = s.split(" ")

    # array to store each character
    characters = []

    # array to store the reversed words
    reversed_words = []

    # array to store the final concatenated string
    final_result = []

    for each in word:
        # save spaces in the string
        if each == "":
            final_result.append(each)
        else:
            index = 0
            # Extract the alphanumeric characters from the string
            for i in each:
                if i.isalnum():
                    characters.append(i)

            # reverse the characters
            characters = characters[::-1]

            # compare the reversed string with the original string
            for i in each:
                if i.isalnum():
                    reversed_words.append(characters[index])
                    index += 1
                else:
                    reversed_words.append(i)

            temp = "".join(reversed_words)
            final_result.append(temp)
            reversed_words = []

    # join the reversed words with spaces in the middle
    final_result = " ".join(final_result)
    return final_result


def batch_test():
    """Test cases to validate the solution"""

    assert reverse_words("String;  2be  reversed...") == "gnirtS;  eb2  desrever..."
    assert reverse_words("abc123") == "321cba"
    assert reverse_words("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert reverse_words("Test 123!") == "tseT 321!"
    assert reverse_words("!!!") == "!!!"
    assert reverse_words("") == ""
    assert reverse_words("x") == "x"
    assert reverse_words("NoChange") == "egnahCoN"
    assert reverse_words("1234 5678") == "4321 8765"
    assert reverse_words("a1!b2@c3#") == "3c!2b@1a#"
    assert (
        reverse_words("A man, a plan, a canal: Panama")
        == "A nam, a nalp, a lanac: amanaP"
    )
    assert reverse_words("Palindrome? Not!") == "emordnilaP? toN!"
    assert (
        reverse_words("a" * 10000 + "!" + "1" * 10000)
        == "1" * 10000 + "!" + "a" * 10000
    )

    print("All test cases passed!\n")


if __name__ == "__main__":
    # Example usage
    assert reverse_words("String;  2be  reversed...") == "gnirtS;  eb2  desrever..."

    batch_test()
