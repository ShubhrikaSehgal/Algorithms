# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:58:41 2020

@author: Shubhrika
"""

class UnionFind:
    def __init__(self,N):
        ## Input: Integer N
        ## defines that the total objects are N 
        self.values=list(range(0,N))
        print(self.values)

    def union(self,p,q):
        ## Input Integer p ,q
        ## connects p and q in the system
        p_value=self.values[p]
        q_value=self.values[q]
        for index,value in enumerate(self.values):
            if(value==q_value):
                self.values[index]=p_value
        print(self.values)
        
    def connected(self,p,q):
        ## Input Integer p,q
        ## Checks if p and q object is connected in system 
        ## Output: Boolean value
        if(self.values[p]==self.values[q]):
            return True
        return False
if __name__ == '__main__':
    n = int(input().strip())
    UF=UnionFind(n)
    print("Enter Exit for Exit")
    while(True):
        value=input().strip()
        try:
            if("Exit" in value):
                break
            else:
                numbers=value.split()
                p=int(numbers[0])
                q=int(numbers[1])
                if(not UF.connected(p,q)):
                    UF.union(p,q)
                else:
                    print("connected")
        except:
            print("Invalid Input")

        



        