data = ["apple", "", "banana", "  cherry  ", None, "date"]
clean_data = [i.strip() for i in data if i and i.strip()]

data = [[1, 2], [3, 4], [1, 2]]
unique_data = list(set(tuple(x) for x in data))
#print([t for j in unique_data for t in j])  

items = ["apple", "banana", "apple", "cherry", "banana"]
ue_data= list(set(tuple((x) for x in items)))

user_roles = {"user", "premium", "beta_tester"}
required_for_feature = {"user", "premium"}
required_for_feature.issubset(user_roles)