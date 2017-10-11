'''
multiple resolution order(mro) is used in complex multiple inhritance cases,
python uses a C3[3] algorithm to calculate a linear order among classes involved in multiple inheritance scheme
'''
from solution_to_DP import SubCallA

for c in SubCallA.__mro__:
    print(c)

'''
output:

<class 'solution_to_DP.SubCallA'>
<class 'solution_to_DP.LeftSubClass'>
<class 'solution_to_DP.RightSubClass'>
<class 'solution_to_DP.ClassB'>
<class 'object'>
'''