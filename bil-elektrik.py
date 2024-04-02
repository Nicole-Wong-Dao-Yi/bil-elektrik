#atur cara bagi mengira bayaran bil elektrik

#pengiytiharan pemboleh ubah dan pemalar
kadar1=0.218
kadar2=0.334
kadar3=0.515
kadar4=0.546

#input 
e=float(input("masukkan kadar penggunaan elektrik:"))

#proses
if e<=200:
    bayaran=e*kadar1
elif e<=300:
    bayaran=(200*kadar1)+((e-200)*kadar2)
elif e<=600:
    bayaran=(200*kadar1)+(100*kadar2)+((e-300)*kadar3)
elif e <=900:
    bayaran=(200*kadar1)+(100*kadar2)+(300*kadar3)+((e-600)*kadar4)
    
#output
print (f"bil elektrik=RM{bayaran:.2f}")
