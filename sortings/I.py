from string import ascii_letters as alph

def adding(lst, char):
    if char in alph:
        lst[alph.index(char)]+=1
    else: 
        lst[29+int(char)]+=1

def check(fword, sword):
    control_lst1 = [0]*39
    control_lst2 = [0]*39
    if len(sword) != len(fword):
        print('NO')
        return
    for i in range(len(fword)):
        adding(control_lst1, fword[i])
        adding(control_lst2, sword[i])
    print('YES' if control_lst1 == control_lst2 else 'NO')
    return

first_word = input()
second_word = input()
check(first_word, second_word)
    
    
    