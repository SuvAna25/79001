players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

rest_a_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]

training_a_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]

travel_a_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]

print('Все члены команды А, которые отдыхают.', rest_a_members)
print('Все члены команды B, которые тренируются.', training_a_members)
print('Все члены команды C, которые путешествуют.', travel_a_members)
