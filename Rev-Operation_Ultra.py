unk_arr0 = [32, 0, 27, 30, 84, 79, 86, 22, 97, 100, 63, 95, 60, 34, 1, 71, 0, 15, 81, 68, 6, 4, 91, 40, 87, 0, 9, 59, 81, 83, 102, 21]

def decrypt(unk_arr0):
  st=['']*32
  j=0
  for i in range(0,32,2):
    if j+3>=32:
      break
    st[j]=unk_arr0[i]
    st[j+1]=unk_arr0[i+1]
    st[j+2]=unk_arr0[16+i]
    st[j+3]=unk_arr0[16+i+1]
    j+=4

  unk_str1 = bytearray("Shadow2024", 'utf-8')
  flag=""
  
  for i in range(32):
    flag += chr(int(st[i]) ^ unk_str1[i % 10])

  print(flag)
decrypt(unk_arr0)
