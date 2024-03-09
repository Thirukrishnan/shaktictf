import random

seed = 123  # Known seed
random.seed(seed)  # Seed the random number generator
key=[]
# Generate and print random numbers
for i in range(36):
    key.append(random.randint(0,256)) 
key=[1,5,1,14,7,11,11,14,10,1,0,12,1,11,4,5,5,7,6,1,14,5,11,7,0,14,12,12,15,12,13,0,1,14,15]
arr=[0]*35

arr[0] = 0x72
arr[1] = 0x6d
arr[2] = 0x60
arr[3] = 0x65
arr[4] = 0x73
arr[5] = 0x62
arr[6] = 0x68
arr[7] = 0x7a
arr[8] = 0x6c
arr[9] = 0x7a
arr[10] = 0x77
arr[11] = 100
arr[12] = 0x31
arr[13] = 0x54
arr[14] = 0x77
arr[15] = 0x31
arr[16] = 0x6c
arr[17] = 99
arr[18] = 0x59
arr[19] = 0x67
arr[20] = 0x62
arr[21] = 0x31
arr[22] = 0x6c
arr[23] = 0x58
arr[24] = 0x31
arr[25] = 0x7d
arr[26] = 0x53
arr[27] = 0x7e
arr[28] = 0x3b
arr[29] = 0x62
arr[30] = 0x69
arr[31] = 0x30
arr[32] = 0x6c
arr[33] = 0x31
arr[34] = 0x72

flag=""
for i in range(35):
    flag+=chr(key[i]^arr[i])
print(flag)

