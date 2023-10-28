users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dictionary = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
Total_number = len(users)
Unique_visits = len(set(users))
dictionary["Общее количество"] = Total_number
dictionary["Уникальные посещения"] = Unique_visits
print(dictionary)
