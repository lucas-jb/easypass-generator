# easypass-generator ( W O R K I N G . . . )
Password generator in python.

```python
import random
import string

lista = list(string.ascii_letters+string.digits+":,~!@#$%^&*_:,~!@#$%^&*_")
random.shuffle(lista)

def generator(length:int):
    passwd = []
    for i in range(length):
        passwd.append(random.choice(lista))
    return ''.join(passwd)

print(generator(16))
```
