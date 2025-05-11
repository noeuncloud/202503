a = int(input("영희 점수 : "))
b = int(input("철수 점수 : "))
c = int(input("기용 점수 : "))

max_score = a
if b > max_score:
    max_score = b
if c > max_score:
    max_score = c

if a == max_score:
    print("최고점",a,"인 영희에게 장학금 지급.")
if b == max_score:
    print("최고점",b,"인 철수에게 장학금 지급.")
if c == max_score:
    print("최고점",c,"인 기용에게 장학금 지급.")
