station = []
human = 0

for _ in range(10) :

    minus, plus = map(int, input().split())

    human -= minus
    human += plus

    station.append(human)

print(max(station))