#!/usr/bin/env python
# coding=utf-8
import sys

sys.setrecursionlimit(999999)

kk = int(input())
#kk = 5
max = 99
result = []
close = 0
fail = 0


def zero002(list005):
  return005=-99
  for ii005 in range(0,len(list005)):
    if list005[ii005]==0:
      return005=ii005
      return return005
  return return005

def check002(list006):
  global close
  global result
  #print(list006)
  close006=1
  #pos006=zero002(list006)
  for jj006 in range(0,len(list006)):
      if list006[jj006]<0:
        close006=0
  for ii006 in range(0,len(list006)-1):
      if list006[ii006]>list006[ii006+1]:
        close006=0
  if list006[-1]==0:
      close006=0
  if close006:
      result=list006.copy()
      close=1

def change004(list004,pos004):
  return004=list004.copy()
  return004[pos004]=pos004+1
  if pos004==0:
    return return004
  if pos004>0:
    for ii004 in range(0,pos004):
      return004[ii004]-=1
    return return004

def change002(list003):
  global fail
  pos002=zero002(list003)
  #print(list003,pos002)
  if pos002==-99:
    fail=1
    return  list003

  return change004(list003,pos002)

def dream002(nk002,nn002):
  global fail
  list002=[]
  for ii002 in range(0,nn002):
    list002.append(0)
  result002=[]
  result002.append(list002)
  for jj002 in range(0,nk002):
    result002.insert(jj002+1,change002(result002[jj002]))
    if fail:
      return
    #return002=result002[jj002+1].copy()


  #check002(return002)
  check002(result002[nk002])

  return

def dream001(nn001,kk001):
  global fail
  global max
  if nn001>max:
    return
  if close:
    return
  dream002(nn001+kk001,nn001)
  if close:
    return  
  fail=0
  dream001(nn001+1,kk001)
  
dream001(2,kk)

if close:
  result2=result.copy()
  len_result=len(result2)
  #print(len_result,result2)
  print(len_result)
  for p in range(0,len_result-1):
    print(result2[p], end = " ")
  print(result[-1])
else:
  print("Daydream!")