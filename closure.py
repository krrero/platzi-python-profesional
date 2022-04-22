# Cuando una variable de scope superior es recordada.
#
# Incluso, podemos eliminar al scope superior que contiene a la variable,
# pero si ya está definida entonces seguirá manteniendo su valor


def main():
    a = 1


    def nested():
        print(a)


    return nested


my_func = main()
my_func()





# Example

def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier


times10 = make_multiplier(10)
times4 = make_multiplier(4)


print(times10(3))
print(times4(5))
print(times10(times4(2)))