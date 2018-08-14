c =[12, 24,-10,33]
f = [(9.0/5.0)*x + 32 for x in c]
print(f)

dict_f = {str(x)+ " Celcjusza": str((9.0/5.0)*x + 32) + " Fahrenheita" for x in c}
print(dict_f)