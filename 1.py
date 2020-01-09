if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        tmp = []
        tmp.append(name)
        tmp.append(score)
        python_students.append(tmp)

scores = []
for i in python_students:
    scores.append(i[1])

scores = sorted(scores)
scores = list(dict.fromkeys(scores))
#print(scores[1])

second_lowest = sorted([i for i in python_students if i[1] == scores[1]])
for i in second_lowest:
    print(i[0])