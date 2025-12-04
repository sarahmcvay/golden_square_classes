def get_most_common_letter(text):
    counter = {}
    for char in text:
        # this is used to count, not sure how it is returning.  
        counter[char] = counter.get(char, 0) + 1
        #print(counter.get(char,0) + 1) #this is the counter loop, does not seem to be linked to the letters 
        # print(sorted(counter.items())) 
        #this shows the loop running correctly, returns a list of tuples, and the correct answer is identified ('o', 7). 
        # note that the counter is also counting spaces. (' ', 8)
        # sorted by the key, " ", ! , e f h i n o r s t .... not the number of times it is found. 
    # letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    # key=lambda item: item[1] this is sorting by the value, number of counts. 
    # but [0] takes the first pair, which will have the smallest value
    # and [1] means from that pair take the value. 
    # this last bit is all confused. 
    # sorted_list = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    # print(sorted_list)

    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    return letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
