# 식별 연산
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  

# 식별 예시
a = 5
b = 5

print(a is b)
print(a is not b)

# print(5 == 5.0)
# print(5 is 5.0)

# 식별 예시2 (a=인트형 와 b=실수형: 객체가 다름)
a = 3
b= 3.0

print(a == b)
print(a is b)
print(a is not b)

print(a is b)

a = 258
print(a is b)

#특성
a = [3, 5, 1]
b = a

print(a is b)

a[0] = 2

print(a,b)

print(a is b)

# 연산자 결합 순서
# a= 2 + 3 * 4
# a = 10 / 5/ 2
# a = 10 % 3 % 2
# a = 1 + 2 > 3 and 4 - 1 < 2
# a = not False and True 
# a = nor True or False and True
# a = 1 * 2 | 3 ^ 4
# a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# a = 2 * -3 // 2
# a = 1==2 
# a = 1==2!= 3

print(a)

# 조건문 if 예시
x = 10
#  = -1
# x = 0

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")

# if 짝수, 홀수
num = 23
if num % 2 == 0:
        print("짝수")
else:
        print("홀수")

# if 두 수 비교
a = 2
b = 3
if a == b:
    print("같습니다.")
else:
    print("다릅니다.")

# if a or b 인지
char = "a"
if char == "a" or char == "b":
    print("'a' 또는 'b'입니다.")
else:
    print("'a' 또는 'b'가 아닙니다.")

# for 예시
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# 이중 for문 예시
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)

# for 0 ~ 9 출력
for i in range(10) :
    print(i)

# for 문자열 한 글자씩 출력
for char in "python":
    print(char)

# for 역순 출력 reversed
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits): 
    print(fruit)

# for 역순 출력 sorted
for fruit in sorted(fruits, reverse=True):
    print(fruit)
    
# for 구구단 
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
        
# for ~ else 문
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process")
 
# 반복문 제어
for i in range(10):
    if i == 7:
        print("break", i)
    elif i == 1:
        print("continue", i)
    else:
        print("pass", i)

    print(i)

# while 1 ~ 5 출력
i = 1

while i <= 5:
    print(i)
    i += 1
    
#  while 0 ~ 9 출력
i = 0

while i < 10:
    print(i)
    i+= 1
    
# whlle 문자열 낱자 출력
str_word = "python"
i = 0

while i < len(str_word):
    print(str_word[i])
    i += 1
    
# while 1 ~ 10 총합
sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1
    
print(sum)

# while 1 ~ 100까지의 짝수, 홀수 출력
i = 1

while i <= 100:
    if i % 2 == 0:
        print("짝수 : ", i)
    elif i % 2 == 1:
        print("홀수 : ", i)
    i += 1
    
#  while 1 ~100까지 7의 배수만 출력
i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1