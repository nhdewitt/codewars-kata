"""
We need a method in the List Class that may count specific digits from a given list of integers. This marked digits will be given in a second list. The method .count_spec_digits()/.countSpecDigits() will accept two arguments, a list of an uncertain amount of integers integers_lists/integersLists (and of an uncertain amount of digits, too) and a second list, digits_list/digitsList that has the specific digits to count which length cannot be be longer than 10 (It's obvious, we've got ten digits). The method will output a list of tuples, each tuple having two elements, the first one will be a digit to count, and second one, its corresponding total frequency in all the integers of the first list. This list of tuples should be ordered with the same order that the digits have in digitsList

Let's see some cases:

l = List()

integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]
l.count_spec_digits(integers_list, digits_list) == [(1, 3), (3, 2)]

integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list) == [(1, 7), (8, 5), (4, 0)]

integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list) == [(1, 0), (8, 0), (4, 0)]
Enjoy it!!

https://www.codewars.com/kata/56311e4fdd811616810000ce/train/python
"""

class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        d = []                                                      # create initial list to hold integers
        for i in integers_list:
            d.extend(list(map(int, str(abs(i)))))                   # abs(i) to ignore -, map each integers individual digits back to an int and extend d
        digit_freq = {k: 0 for k in digits_list}                    # only care about freq of digits in digits_list
        for i in d:
            if i in digit_freq.keys():
                digit_freq[i] += 1                                  # count digits
        return list((k, digit_freq[k]) for k in digits_list)        # return list of tuples in order of digits_list