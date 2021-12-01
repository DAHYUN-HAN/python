import operator

dict = {'P' :9, 'Y' :2, 'O' :5, 'L' :4}

# key 값을 기준으로 정렬
sort_dict_key = sorted(dict.items())
print(sort_dict_key)

# value 값을 기준으로 정렬
sort_dict_value = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
print(sort_dict_value)