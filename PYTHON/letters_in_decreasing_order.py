
def most_frequent ():
    test_str = input("Please enter a string ")

    all_freq = {}
    result = {}
  
    for i in test_str: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1

    result = dict(sorted(all_freq.items(), key=lambda item: item[1], reverse=True))

    print(result)

most_frequent()
