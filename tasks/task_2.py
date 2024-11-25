def extraction(input):
    extracted = ""
    for x in input:
        if (64 < ord(x) < 123 or ord(x) == 32):
            extracted += x
    return extracted


def reverseWord(input):
    reversed = ""
    reversed = input[-1:-(len(extracted)):-1]
    return reversed


def removeVowels(input):
    vowels = "aeiouAEIOU"
    output = ""
    for x in input:
        if (x not in vowels):
            output += x
    return output


input = "###!!@emocleW EPGTQ!!!6789"
extracted = extraction(input)
words = extracted.split()
output = reverseWord(words[0])
output += " "
output += removeVowels(words[1])
print(output)
