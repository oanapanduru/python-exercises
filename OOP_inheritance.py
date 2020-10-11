# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:55:59 2020

@author: oanap
"""


class Old_management:
    def __init__(self, p_general_manager, p_marketing_manager):
        self.general_manager = p_general_manager
        self.marketing_manager = p_marketing_manager
    def get_general_manager(self):
        return self.general_manager
    def get_marketing_manager(self):
        return self.marketing_manager
class New_management(Old_management):
    def __init__(self, p_general_manager, p_marketing_manager, p_financial_manager):
        Old_management.__init__(self, p_general_manager, p_marketing_manager)
        self.financial_manager = p_financial_manager
    def get_financial_manager(self):
        return self.financial_manager
    
def main():    
    p_general_manager= input('please enter the name of the previous general manager:')
    p_marketing_manager = input('please enter the name of the previous marketing manager:')
    print()
    old_structure = Old_management(p_general_manager, p_marketing_manager)


    print('Here is the structure of the previous management:')
    print('the previous G.M :', old_structure.get_general_manager())
    print('the previous M.M:', old_structure.get_marketing_manager())

main()

def new():
    p_general_manager= input('please enter the name of the new general manager:')
    p_marketing_manager = input('please enter the name of the new marketing manager:')
    p_financial_manager = input('please enter the name of the new fiancial manager:')
    print()

    new_structure = New_management(p_general_manager, p_marketing_manager, p_financial_manager)

    print('Here is the structure of the new management:')
    print('the new G.M :', new_structure.get_general_manager())
    print('the new M.M:', new_structure.get_marketing_manager())
    print('the new F.M:', new_structure.get_financial_manager())
    
new()
    
    
    