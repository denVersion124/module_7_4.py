team1_name = "Мастера кода"
team2_name = "Волшебники Данных"
team1_num = 5
print("В команде Мастера кода участников: %s!" % team1_num)
team2_num = 6
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {score_2}!".format(score_2=42))
score_2 = 42
score_1 = 40
team1_time = 1552.512
team2_time = 2153.31451
print("{team2_name} решили задачи за {team1_time} с!".format(team1_time=18015.2, team2_name="Волшебники Данных"))
print(f"Команды решили {score_1} и {score_2} задач.")
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f"Победа команды {team1_name}!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_name:
    challenge_result = f"Победа команды {team2_name}!"
else:
    challenge_result = "Ничья!"
task_total = score_1 + score_2
time_avg = ((team1_time / score_1) + (team2_time / score_2)) / 2
time_avg = round(time_avg, 2)
print(f"Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!")
print(challenge_result)