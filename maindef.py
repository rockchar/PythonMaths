#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:47:53 2019

@author: rockchar
"""

################### namescript.py ####################
def main():
    foo()
       
def foo():   
    print("The name of the __name__ variable is "+__name__)
   
if __name__ == "__main__":
    main()
   

           