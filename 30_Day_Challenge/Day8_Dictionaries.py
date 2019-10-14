# Enter your code here. Read input from STDIN. Print output to STDOUT

num_test_case=int(input())
new_dict = {}
for i in range(num_test_case):
    test_string = input()
    a = test_string.split(' ')
    new_dict[a[0]] = a[1]

try: 
    while True:
        query = input()
        if query == '':
            break
        elif query not in new_dict.keys():
            print("Not found")
        else:
            print(query + '=' +new_dict[query])
except:
    pass
