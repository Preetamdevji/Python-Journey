def game():
    return 220

score = game()

file_path = 'G:\python\game_score.txt'

with open(file_path) as f:
    hiscore = f.read()

if hiscore == '':
    with open(file_path, "wt") as f:
        f.write(str(score))

elif int(hiscore) < score:
    with open(file_path, "wt") as f:
        f.write(str(score))



        