drama = ["宫廷剧","悬疑剧","偶像剧"]
kind = ["喜欢","讨厌","既不喜欢也不讨厌"]
caicai = {}
for i in drama:
    if i == '宫廷剧':
        caicai[kind[1]] = i
    elif i == '悬疑剧':
        caicai[kind[0]] = i
    else:
        caicai[kind[2]] = i
print(caicai)