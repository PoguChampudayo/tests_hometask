ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}

result = []
for user in list(ids.values()):
    result.extend(user)
    
def delete_nonunique(values:list):
    return sorted(list(set(values)), reverse = True)

print(delete_nonunique(result))