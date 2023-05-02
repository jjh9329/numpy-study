#python 다차원 배열의 이해

##숫자 자료형
# python에서는 숫자형 변수로 데이터를 표현할 수 있다.

# 세 명의 학생의 수학과목 점수 선언
math1 = 11
math2 = 12
math3 = 13
# 합과 평균 구하기
total = math1 + math2 + math3
average = total/3

print(f'수학점수 합:{total}')
print(f'수학점수 평균:{average}')

# 새로 전학온 학생의 수학 점수가 추가 된다면
# 새로운 변수 선언과 합과 평균을 구하는 코드를 수정해야 할 필요가 생김
math4 = 14
total = math1 + math2 + math3 + math4
average = total/4
print(f'수학점수 합:{total}')
print(f'수학점수 평균:{average}')

# 1.2 리스트 자료형
math_list = [11, 12, 13]

total = 0
average = 0
for math in math_list:
    total += math
average = total/len(math_list)

print(f'수학점수 합:{total}')
print(f'수학점수 평균:{average:.2f}')

# 전학온 4번째 학생의 수학점수 추가
math_list.append(14)

total = 0
average = 0
for math in math_list:
    total += math
average = total/len(math_list)

print(f'수학점수 합:{total}')
print(f'수학점수 평균:{average:.2f}')

# 그런데 시험 문제에 오류가 발견되어 모든 학생의 점수를 1점씩 올려줘야 하는 상황이 발생된다면
math_list = [ math+1 for math in math_list]
print(math_list)