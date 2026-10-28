#membuat array baru

#importing 'array untuk array baru

import array as arr

#membuat array degan tipe data integer (i)

a = arr.array('i',[1,2,3])

#cetak Array

print ('Array Baru Yang Dibuat Adalah : ',end ='')
for i in range (0,3):
     print (a[i],end ='')
print()