#!/usr/bin/env python
# coding: utf-8

# In[21]:


import random

def main():
    Lst1 = [random.randint(1, 100) for i in range(20)]
    Lst2 = [random.randint(1, 100) for i in range(20)]
    Lst1.sort()
    Lst2.sort()
    print("첫 번째 리스트 입니다.\n", Lst1)
    print("두 번째 리스트 입니다.\n", Lst2)
    list_combine(Lst1, Lst2) #문제1-1
    non_overlap(Lst1, Lst2)  #문제1-2
    
    print("\n\n")
    
    stu_answer(answer()) #문제2
    
    
def list_combine(a, b):
    result = a+b
    result.sort()
    print("두 리스트를 합친 결과입니다.\n", result) 
    
def non_overlap(a, b):
    set1 = set(a)
    set2 = set(b)
    result = list(set1^set2)
    result.sort()
    print("두 리스트의 중복값을 없앤 결과입니다.\n", result)
    
    
#질문에 대한 정답
def answer():
    list = [] #빈 리스트 만들기
    
    for i in range(2): #row2 column10 리스트 만들기
        ans_list = [] #리스트 안 리스트로 사용할 빈 리스트
        for j in range(10):
            ans_list.append(0)
        list.append(ans_list)
    
    for i in range(10): 
        list[0][i] = i #row0에 0부터 9까지 넣기
        list[1][i] = random.choice("ABCDE") #row1에 ABCDE 랜덤으로 넣기
        
    print("질문에 대한 정답")
    print(list)
    print("\n")
        
    return list

#질문에 대한 학생의 답
def stu_answer(list):
    stu_list = [] #빈 리스트 만들기
    
    for i in range(8): #row8 column10 리스트 만들기
        stu_ans_list = []
        for j in range(10):
            stu_ans_list.append(0)
        stu_list.append(stu_ans_list)

    for i in range(8):
        for j in range(10):
            stu_list[i][j] = random.choice("ABCDE")

    print("질문에 대한 학생의 답")
    print(stu_list)

    for i in range(8):
        result = 0 
        for j in range(10):
            if (stu_list[i][j] == list[1][j]):
                result += 1
        print(i, "번 학생의 정답 문항의 개수는", result, "입니다.")
    
    
main()
    


# In[ ]:




