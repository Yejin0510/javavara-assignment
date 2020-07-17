

#1번

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True



#2번

x = int(input())
y = int(input())
z = int(input())
n = int(input())
answer = [[x,y,z]for x in range(x+1) for y in range(y+1) for z in range(z+1) if x + y + z != n]
print(answer)



#3번


# 수업을 못 들어서 그런지 이번주 내용 어려워요.... 주말에 다시 복습하면서 내용 익혀오겠스습니다... 
# 열심히 하겠습니다... 자바장님 항상 수고가 많으세요 감사합니다 담주 수업 땐 꼭 들어가겠습니다 !!!