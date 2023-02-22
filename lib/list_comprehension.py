#!/usr/bin/env python3



def return_evens(num_list):
    some_nums = [n for n in num_list if n % 2 == 0]
    return(some_nums)

return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])





def make_exclamation(sentence_list):
    yell = [n+"!" for n in sentence_list]
    return yell
make_exclamation(['I like computers', 'I require coffee', 'Live long and prosper'])
