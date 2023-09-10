def most_frequent(input_string):
    
    letter_frequency = {}

    
    input_string = input_string.replace(" ", "").lower()

    
    for char in input_string:
        
        if char.isalpha():
            
            letter_frequency[char] = letter_frequency.get(char, 0) + 1

    
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

    
    for letter, frequency in sorted_frequency:
        print(f"{letter}: {frequency}")


input_string = input("Please Enter a String: ")
most_frequent(input_string)
