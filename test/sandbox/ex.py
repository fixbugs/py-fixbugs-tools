from sys import modules
modules.clear()
del modules

__builtins__.dir = None
eval = None
input = None
execfile = None

LEN_PASS = len(open('./password','r').read()) # Length of Password

I_N_P_U_T = ("aaaaaa") # only a-z0-9[]() and length of code must be <= 50

P_A_S_S_W_O_R_D = open('./password','r').read()

assert LEN_PASS >= 1
assert LEN_PASS == len(I_N_P_U_T)
for i in range(LEN_PASS):
    if I_N_P_U_T[i] != P_A_S_S_W_O_R_D[i]:
        from sys import exit
        exit() # Wrong

print 'Here is your flag:',open('./flag','r').read()
