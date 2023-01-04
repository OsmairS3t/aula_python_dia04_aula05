from datetime import date
import math as matematica
import matplotlib.pyplot as plt

def salario_descontado_imposto(salario, imposto=27.):
	return salario - (salario * imposto * 0.01)

def new_user(active=False, admin=False):
    print(active)
    print(admin)

def unpacking_experiment(*args):
		arg1 = args[0]
		arg2 = args[1]
		outroArg = args[2:]
		print(arg1)
		print(arg2)
		print(outroArg)

def unpacking(**kargs):
    print(kargs)

if __name__ == '__main__':
    #print(salario_descontado_imposto(5000))
    #print(salario_descontado_imposto(5000,11))
    #d = (2023, 1, 3)
    #date(d[0], d[1], d[2])
    #d = (2023, 1, 3)
    #print(date(*d))
    #config={"active": False, "admin": True}
    #new_user(config.get("active"), config.get("admin"))
    #new_user(config)
    #unpacking_experiment(1, 2, 3, 4, 5, 6, 7, 8, 9)
    #unpacking(named="Teste", other="Outro parametro")
    #raiz = matematica.sqrt(25)
    #print(raiz)
	x = [1, 2, 3, 4]
	y = [2, 3, 4, 3]
	plt.plot(x, y)
	plt.show()

