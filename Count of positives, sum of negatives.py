#Given an array of integers.
#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#If the input array is empty or null, return an empty array.
def count_positives_sum_negatives(arr):
    positive_numbers =[]
    negative_numbers = []
    result = []
    for x in arr:
        if x>0:
            positive_numbers.append(x)
            pn = len(positive_numbers)
        elif x<0:
            negative_numbers.append(x)
            nn = sum(negative_numbers)
    result.append(pn)
    result.append(nn)
    return result