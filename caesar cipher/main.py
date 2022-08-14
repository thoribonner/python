from art import logo

lowerAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'D', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphaLength = len(lowerAlphabet)
translate = True

print(-28 % 26)

def indexFinder(index, toShift):
    index += toShift

    if index > alphaLength - 1 or index < 0:
        index = index % alphaLength
        
    return index



def caesar(cryptDirection, cryptText, cryptShift):
    
    translatedText = ""
    if cryptDirection == "decode":
        cryptShift *= -1
    
    for char in cryptText:
        if char not in lowerAlphabet and char not in upperAlphabet:
            translatedText += char
        elif char in lowerAlphabet:
            currentIndex = lowerAlphabet.index(char)
            shiftedIndex = indexFinder(currentIndex, cryptShift)
            translatedText += lowerAlphabet[shiftedIndex]
        else:
            currentIndex = upperAlphabet.index(char)
            shiftedIndex = indexFinder(currentIndex, cryptShift)
            translatedText += upperAlphabet[shiftedIndex]

    print(f"The {cryptDirection}ed message is:\n**\t{translatedText}\t**")

print(logo)

while translate:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(cryptDirection=direction, cryptText=text, cryptShift=shift)
    continueCypher = input("Would you like to translate more? Yes or No?\n").lower()
    if continueCypher == "no":
        translate = False

print("Thank you! Come back anytime!")