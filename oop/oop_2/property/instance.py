from oop_properties import Email

ml = Email("sylvernusakubo@yahoo.com")
print(ml.email)
ml.email = "akubo@gmail.com"
print(ml.email)
ml.email = "haha.com"
print(ml)
del ml.email


'''
sylvernusakubo@yahoo.com
akubo@gmail.com
not a valid mail address
<oop_properties.Email object at 0x0303A470>
erasing mail...
'''