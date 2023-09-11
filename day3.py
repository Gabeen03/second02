#집합
my_set = {5, 8, 3, 7, 1, "h"}

#생성
my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)
set_tmp = set("hello")

print(set_tmp)

#합집합
my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)
my_set = {5, 8, 3, 7, 1, "h"}

# print(my_set l set_item)

print(my_set.union(set_item))

#차집합
my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)

print(my_set - set_item)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)

# print(my_set - set_item)

print(my_set.difference(set_item))

#교집합
my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item )

# print(my_set & set_item)

print(my_set.intersection(set_item))

#추가
my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)

my_set.add(9)

print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)

my_set.update([5, 9, 7, 4])

print(my_set)

#삭제
my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)

my_set.clear()

my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)

my_set.discard(2)
print(my_set)

#remove와 discard의 차이점 확인
my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set)

my_set.difference_update(set_item)
print(my_set)

#타입 변환
my_int = 10
print(my_int)

print(my_int  + 10)

#변환 진행
my_int = 10
print(my_int)

#변환 값 연산
my_int = 10
print(my_int)

print(my_int + 10)
my_str = str(my_int)

print(my_str)

print(my_str + 10)

my_int = 10 
print(my_int)

print(my_int + 10)
my_str = str(my_int)

print(my_str)

print(my_str + "hello")

#변환확인
my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

#변환 값 연산
my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)

#다른 변환 예시
my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)

my_int2 = int("ten")
print(my_int2)

# 산술 연산자
x=10
y= 8

print(x + y)    
print(x - y)    
print(x * y)    
print(x / y)    
print(x % y)    
print(x // y)   
print(x ** y)   

#비교, 관계 연산자

a = 10
b = 4

# a > b
# a < b
# a >= b
# a <= b
# a != b

print(a > b)    
print(a < b)    
print(a >= b)   
print(a <= b)   
print(a == b)   
print(a != b)   

#논리 연산자

a = 1
b = 0

x = True
y = False

print(x and y)  
print(x or y)   
print(not x)    
print(not y)    

#비트 연산자

a = 10
b = 3

# c = a & b   
# c = a | b   
# c = a ^ b   
# c = ~a      
c = a << 2
print(c)

#멤버 연산자

my_list = [9, 4, 3, 7, 8, 'hi']

print(2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print("k" in my_dic)





  




