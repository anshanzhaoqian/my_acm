#!/usr/bin/env python
# coding=utf-8
import sys

sys.setrecursionlimit(999999)

#kk = int(input())
kk = 5
max = 10
max_n = 4
max_now = 20
result = []
close = 0

def try_fifth(nn_three,queue_301):
  close22=1
  for m in range(0,nn_three):
    if queue_301[m]!=0:
      close22=0
  return close22


def try_third(nn_three,queue_201,queue_202):
  global close
  global result
  if close:
    return
  #print(queue_202)
  if try_fifth(nn_three,queue_201):
    result.append(queue_202)
    #print(nn_three,queue_201,queue_202)
    close=1
  return

def insert11(now_ten,nn_ten,queue_111,queue_102,queue_103,ii):
        for j in range(0,ii):
          queue_111[j]=queue_111[j]+1
          now_ten+=1
          queue_121=queue_111.copy()
          queue_122=queue_102.copy()
          queue_421=queue_111.copy()
          queue_421.append(now_ten)
          queue_421.append(nn_ten)
          queue_103.append(queue_421)
          try_second(now_ten,nn_ten,queue_121,queue_122,queue_103)
          now_ten-=1
        return

def insert12(now_11,nn_ten,queue_111,queue_102,queue_103):
          now_11+=1
          queue_141=queue_111.copy()
          queue_142=queue_102.copy()
          queue_441=queue_111.copy()
          queue_441.append(now_11)
          queue_441.append(nn_ten)
          queue_103.append(queue_441)
          try_second(now_11,nn_ten,queue_141,queue_142,queue_103)
          return

def insert13(now_three,nn_three,queue_101,queue_102,queue_103,i22):
    if (i22+1)==queue_101[i22]:
      queue_111=queue_101.copy()
      queue_111[i22]=0
      if i22>0:
        insert11(now_three,nn_three,queue_111,queue_102,queue_103,i22)
      if i22==0:
        insert12(now_three,nn_three,queue_111,queue_102,queue_103)
    return

def try_second(now_three,nn_three,queue_101,queue_102,queue_320):
  global close
  global kk
  global max
  #print(now_three,nn_three,queue_101,queue_102)
  queue_303=queue_320.copy()
  if close:
    return
  if now_three==(nn_three+kk):
    #print(now_three,nn_three,queue_101,queue_102,queue_303)
    try_third(nn_three,queue_101,queue_102)
    return
  if now_three>(nn_three+kk):
    return
  if try_fifth(nn_three,queue_101):
    return
  for i in range(0,nn_three):
    print(now_three,nn_three,queue_101,queue_102,queue_303,i)
    insert13(now_three,nn_three,queue_101,queue_102,queue_303,i)

  return

def try_first(nn_two,queue_31):
  global close
  global max_now
  if close:
    return
  #print(queue_31)
  for i in range(0,max_now+1):
    queue_six=queue_31.copy()
    queue_32=[]
    try_second(i,nn_two,queue_six,queue_31,queue_32)
  return

def make_second(now_two,nn_two,queue_21):
  global close
  global max
  if close:
    return
  #print(queue_21)
  if now_two==nn_two:
      #print(queue_21)
      try_first(nn_two,queue_21)
      return 
  for j in range(1,max+1):
    if queue_21[-1]<=j:
      queue_seven=queue_21.copy()
      queue_seven.append(j)
      now_seven=now_two+1
      nn_seven=nn_two
      #print(queue_21)
      make_second(now_seven,nn_seven,queue_seven)
  return 

def make_first_11(now_41,nn_41,queue_41):
  global close
  global max
  if close:
    return
  #for j in range(1,max+1):
  for j in range(1,3):
    if queue_41[-1]<=j:
      queue_51=queue_41.copy()
      queue_51.append(j)
      now_51=now_41+1
      nn_51=nn_41
      #print(queue_21)
      make_second(now_51,nn_51,queue_51)
  return

def make_first(nn_one):
  global close
  global max
  if close:
    return
  #for j in range(0,max+1):
  for j in range(0,2):
    output_one=[]
    output_one.append(j)    
    make_first_11(1,nn_one,output_one)
  return

for o in range(2,max_n+1):
  make_first(o)

if close:
  result2=result[0]
  len_result=len(result2)
  print(len_result)
  #for p in range(0,len_result-2):
    #print(result2[p], end = " ")
  print(result[-1])
else:
  print("Daydream!")