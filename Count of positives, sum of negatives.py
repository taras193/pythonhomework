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