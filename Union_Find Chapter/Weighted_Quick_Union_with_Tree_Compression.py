#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:02:59 2019

@author: kartiktanksali
"""

#A typical example of Weighted Quick Union Algorithm - with tree compression
#Complexity LogN - M + Log^2N - Worst Case

class Union_Find:
    lst = []
    sz = []
    def __init__(self,n):
        if n==0:
            print("No Nodes created")
        else:
            for i in range(n+1):
                self.sz.append(1)
                self.lst.append(i)
            print("Nodes Created")
    
        
    def Union(self,p,q):
        firstVal = self.root(p)
        secondVal = self.root(q)
        if self.sz[firstVal]<self.sz[secondVal]:
            self.lst[firstVal]=secondVal
            self.sz[secondVal]+=self.sz[firstVal]
        else:
            self.lst[secondVal]=firstVal
            self.sz[firstVal]+=self.sz[secondVal]
        
        return "Union Done"
    
    def root(self,i):
        while(i!=self.lst[i]):
            i=self.lst[self.lst[i]]
            i = self.lst[i]
        return i
                
        
ch=0
uf = Union_Find(0)
while(ch<5):
    print("\n 1)Create an unconnected new graph \n 2)Check if nodes are connected \n 3)Union 2 nodes \n 4)Display Nodes\n")
    ch = int(input())
    if ch==1:
        if len(uf.lst)==0:
            n = int(input("\n Enter the number of nodes to be created: "))
            uf = Union_Find(n)
            
    elif ch==2:
        pq = input("\n Enter two nodes to be verified: ").split()
        p = int(pq[0])
        q = int(pq[1])
        if uf.root(p) == uf.root(q):
            print("Connected")
        else:
            print("Not Connected")
    
    elif ch==3:
        pq = input("\n Enter two nodes to be joined: ").split()
        p = int(pq[0])
        q = int(pq[1])
        print(uf.Union(p,q))
    
    elif ch==4:
        print(uf.lst)
        
    else:
        print("\n------Exiting-------")
        break
