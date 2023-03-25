num_matches = int(input("How many matches?: "))
match_dict = {}
for i in range(num_matches):
    x = input(f"Team nums for match {i+1} (separated by spaces): ")
    xls = list(x.split(" "))
    match_dict[i+1] =  xls
print(match_dict)