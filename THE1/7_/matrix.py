#!usr/bin/python3

#7_matrix.py
#Version 1.0.0
#3-27-22

import math
from typing import Any

class Matrix:
    ''' Python class to represent a mathematical matrix. '''
    def __init__(self, u_left: int, u_right: int, l_left: int, l_right: int) -> None:
        self.u_left=u_left
        self.u_right=u_right
        self.l_left=l_left
        self.l_right=l_right
        
    def add(self, addend_matrix: "Matrix") -> None:
        ''' add two matricies. '''
        res_u_left=self.u_left+addend_matrix.u_left
        res_u_right=self.u_right+addend_matrix.u_right
        res_l_left=self.l_left+addend_matrix.l_left
        res_l_right=self.l_right+addend_matrix.l_right
        return Matrix(u_left=res_u_left, 
                      u_right=res_u_right, 
                      l_left=res_l_left, 
                      l_right=res_l_right)
        
    def mult(self, product_matrix: "Matrix") -> None:
        ''' multiply two matricies. '''
        res_u_left=(self.u_left*product_matrix.u_left) + (self.u_right*product_matrix.l_left)
        res_u_right=(self.u_left*product_matrix.u_right) + (self.l_left*product_matrix.l_right)
        res_l_left=(self.l_left*product_matrix.u_left) + (self.l_right*product_matrix.l_left)
        res_l_right=(self.l_left*product_matrix.u_right) + (self.l_right*product_matrix.l_right)
        return Matrix(u_left=res_u_left, 
                      u_right=res_u_right, 
                      l_left=res_l_left, 
                      l_right=res_l_right)
        
    def __str__(self):
        return f'|   {self.u_left}   {self.u_right}|\n|   {self.l_left}   {self.l_right}|\n'
    
if __name__ == '__main__':
    a = Matrix(1,2,3,4)
    b = Matrix(0,1,-1,0)
    c = a.add(b)
    d = b.mult(b).add(a)
    print('a=')
    print(a)
    print('b=')
    print(b)
    print('c=')
    print(c)
    print('d=')
    print(d)

