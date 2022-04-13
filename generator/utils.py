import random
def random_gen(length,num,s_char,ucase):
    thepass = ""
    charecters = list('abcdefghijklmnopqustuvwxyz')
    if num !=None:
        charecters.extend('0123456789')
    if ucase !=None:
        charecters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if s_char !=None:
        charecters.extend('!@#$%^&*')
    for i in range(int(length)):
        thepass += random.choice(charecters)
    return thepass