"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.


"""

def expanded_form(num):
    number_as_string = list(str(num))
    expanded_form = []
    
    for i in range(len(number_as_string)):
        if number_as_string[i] == "0":
            continue
        place_value = int(number_as_string[i]) * (10 ** (len(number_as_string) - i - 1))
        
        expanded_form.append(str(place_value))
        
    return " + ".join(expanded_form)