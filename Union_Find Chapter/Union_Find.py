#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:49:19 2019

@author: kartiktanksali
"""
#A typical example of Union-Find Algorithm
#Complexity N^2

class Union_Find:
    lst = []
    def __init__(self,n):
        if n==0:
            print("No Nodes created")
        else:
            for i in range(n+1):
                self.lst.append(i)
            print("Nodes Created")
    
    def isConnected(self,p,q):
        if self.lst[p]==self.lst[q]:
            return "Connected"
        else:
            return "Not Connected"
        
    def Union(self,p,q):
        firstVal = self.lst[p]
        secondVal = self.lst[q]
        for i in range(len(self.lst)):
            if self.lst[i]==firstVal:
                self.lst[i]=secondVal
        return "Union Done"
                
        
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
        print(uf.isConnected(p,q))
    
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


    
    
