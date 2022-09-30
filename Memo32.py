import time
import random
from PiedraPapelTijera32 import *
#Memo 32, son dos juegos que tiene en total otros 2 juegos adentro...
#el primero ese de dados y el segundo es piedra papel y tijera. ambos sistemas los cree yo para varios ejercicios que estuve haciendo en python
#anexe todo lo que estuve asiendo aqui, poniendole un sistema de puntaje y un sistema de guardado(con codigos ya programados)
#para obtener esos codigos solo se tiene que ganar puntos, si llega a 100 obtendra al final del juego, un codigo para obtener al principio
#del programa 100 puntos.
#para los demas, simplemente si obtiene buen puntaje en ciertos juegos obtendra el codigo de 500.
#el final del juego se da por la caja misteriosa.  
#--------------------------------------------------------------------------
#OPCIONARIO
apagado=0
puntaje=[]
registro=[]
#----------------------------------------------------------------
def DadosEnfrentar():
	apagar2=0
	print("----------------------")
	print("Dados PVP")
	print("----------------------")
	lista1=[1,2,3,4,5,6]
	eleccion1=random.choice(lista1)
	eleccion2=random.choice(lista1)
	jugador=print(f"{registro} ha sacado",eleccion1)
	guerrerodadedo=print(f"EL GUERRERO HA SACADO",eleccion2)
	print("----------------------")

	if eleccion2 > eleccion1:
		print("EL WARRIOR HA GANADO, FUISTE DOMADO.")
		pPer=-10
		puntaje.append(pPer)
		print(f"Puntaje total: {sumaLista(puntaje)}")
		print("-------------------------------------")

	elif eleccion2 < eleccion1:
		print(f"{registro} ha ganado.")
		pWin=20
		puntaje.append(pWin)
		print(f"Puntaje total: {sumaLista(puntaje)}")
		print("-----------------------")

	else:
		print("Empate.")
		pEmp=0
		puntaje.append(pEmp)
		print(f"Puntaje total: {sumaLista(puntaje)}")
		print("-----------------------")

	while apagar2 != 1:
		try:
			apagar2=int(input("Seguir jugando (1)/ Ir al menu dados (C/N): "))
			if apagar2 == 1:
				print("Continuemos...")
				time.sleep(1)
				DadosEnfrentar()
				break
			else:
				DadosMenu()
				DadosMod()
				break
		except:
			print("Valores no soportados, Intenta de nuevo.")
			continue
			

#-----------------------
def DadosMayores():
	salir=0
	print("-----------------------------------------------------------------------------")
	print("Encuentra el Dado. Suerte")
	print("-----------------------------------------------------------------------------")
	while salir != 1:		
		try:
			num=int(input("Numero de dados: "))
			print("---------------------------------")
			if num <= 0:
				print(f"Imposible, necesitas un numero mas alto que {num}.")

			elif num > 6:
				print(f"Imposible, conseguir un {num}")

			else:
				try:
					valor=int(input("Valor a conseguir: "))
					valoraconseguir=valor

					if valoraconseguir > 6:
						print(f"Imposible conseguir un {valoraconseguir}")
					elif valoraconseguir <= 6:
						ganar=False
						print(f"Dados: ",end=" ")
						for i in range(num):
							dado=random.randrange(1,6)
							print(f"{dado}",end=" ")
							if dado == valoraconseguir:
								ganar = True
						print()
						if ganar:
							print("El jugador ha ganado.")
							pWon=25							
							puntaje.append(pWon)
							print(f"Puntaje total: {sumaLista(puntaje)}")

							salir=int(input("Deseas seguir jugando? 1_Volver al menu C/N_Sigamos jugando: "))

							if salir == 1:
								print("Ok regresando al menu...")
								time.sleep(1)
								print("Cargando...")
								time.sleep(1)
								DadosMenu()
								DadosMod()
								break
							else:
								print("Sigamos jugando estonces...")
								time.sleep(1)
								DadosMayores()
								break
						else:
							print("Pierdes...")
							pLose=-10
							puntaje.append(pLose)
							print(f"Puntaje total: {sumaLista(puntaje)}")

							salir=int(input("Deseas seguir jugando? 1_Volver al menu C/N_Sigamos jugando: "))

							if salir == 1:
								print("Ok regresando al menu...")
								time.sleep(1)
								print("Cargando...")
								time.sleep(1)
								Menu()
								regaloCodigo2()
								break
							else:
								print("Sigamos jugando estonces...")
								time.sleep(1)
								DadosMayores()
								break
				except:
					print("Error intentelo de nuevo.")

		except:
			print("Caracteres no soportados, use los solicitados...")
			DadosMayores()
			break

def DadosMenores():
	print("Los dados que sean menores a todos los jugadores seran los ganadores.suerte")

def DadosMenu():
	print("------------------------------------------------------------------------------------------")
	print(""" ######                                   #     #                                            
 #     #    ##    #####    ####    ####   ##   ##    ##     ####   #   ####    ####    ####  
 #     #   #  #   #    #  #    #  #       # # # #   #  #   #    #  #  #    #  #    #  #      
 #     #  #    #  #    #  #    #   ####   #  #  #  #    #  #       #  #       #    #   ####  
 #     #  ######  #    #  #    #       #  #     #  ######  #  ###  #  #       #    #       # 
 #     #  #    #  #    #  #    #  #    #  #     #  #    #  #    #  #  #    #  #    #  #    # 
 ######   #    #  #####    ####    ####   #     #  #    #   ####   #   ####    ####    ####                                                                                               """)
	print("------------------------------------------------------------------------------------------")
	print(f"Bienvenido {registro}")

def DadosMod():
	apagar=0
	print("""----------------------------------
1.Encuentra el Dado.
2.Dado PVP.
3.Volver Menu.
----------------------------------""")
	print(f"Puntaje: {sumaLista(puntaje)}")
	while apagar != 1:
		try:
			user=int(input("Elije la modalidad de juego: "))
			if user == 1:
				print("Usted elije Encuentra el Dado")
				time.sleep(1)
				print("Cargardo...")
				time.sleep(1)
				DadosMayores()
				break

			elif user == 2:
				print("Usted elije Dado PVP")
				time.sleep(1)
				print("Cargando...")
				time.sleep(1)
				DadosEnfrentar()
				break

			elif user == 3:
				print("----------------------------------------------------------------------------------")
				apagar=int(input("Deseas volver al menu?? 1 para Seguir aqui c/n para volver al menu.: "))
				print("----------------------------------------------------------------------------------")
				if apagar == 1:
					print("ok volviendo al menu de dados.")
					DadosMod()
					break

				else:
					print("OK, volviendo al menu principal.")
					Menu()
					regaloCodigo2()
					break

		except:
			print("Caracteres no soportados, Intentelo de nuevo.")
			continue

#-------------------------------------------------------------------------------
#PIEDRAPAPELTIJERA
def MenuPiedra():
	print("------------------------------------------------------------------------------------------")
	print("""888888                            88888                        8888888                            
8    8 e  eeee eeeee eeeee  eeeee 8    8 eeeee eeeee eeee e       8   e     e  eeee eeeee  eeeee 
8eeee8 8  8    8   8 8   8  8   8 8eeee8 8   8 8   8 8    8       8e  8     8  8    8   8  8   8 
88     8e 8eee 8e  8 8eee8e 8eee8 88     8eee8 8eee8 8eee 8e      88  8e    8e 8eee 8eee8e 8eee8 
88     88 88   88  8 88   8 88  8 88     88  8 88    88   88      88  88 e  88 88   88   8 88  8 
88     88 88ee 88ee8 88   8 88  8 88     88  8 88    88ee 88eee   88  88 8ee88 88ee 88   8 88  8                                                                                                  
------------------------------------------------------------------------------------------""")

partidas=[]
def PiedraPapelTijera():
	user=0

	while user != 1:
		eleccion=["Piedra","Papel","Tijera"]
		eleccion2=["Piedra","Papel","Tijera"]

		guardian=random.choice(eleccion)
		jugador2=random.choice(eleccion)
		print("---------------------------------------------")
		print(f"EL GUARDIAN DEL KERMES ha sacado {guardian}")
		print(f"{registro} sacas",jugador2)
		print("---------------------------------------------")

		if guardian == "Piedra" and jugador2 == "Tijera":
			print("El GUARDIAN DEL KERMES GANA :c")
			print("---------------------------------------------")
			par=1
			partidas.append(par)
			print("Total de partidas: ",sumaLista(partidas))
			puntajePerder=-10
			puntaje.append(puntajePerder)
			print("Puntaje Actual: ",sumaLista(puntaje))

		elif guardian == "Tijera" and jugador2 == "Piedra":
			print(f"{registro} Ganas :3")
			print("---------------------------------------------")
			par=1
			partidas.append(par)
			print("Total de partidas: ",sumaLista(partidas))
			puntajeGanar=15
			puntaje.append(puntajeGanar)
			print("Puntaje Actual: ",sumaLista(puntaje))

		elif guardian == "Papel" and jugador2 == "Tijera":
			print(f"{registro} Ganas :3")
			print("---------------------------------------------")
			par=1
			partidas.append(par)
			print("Total de partidas: ",sumaLista(partidas))
			puntajeGanar=15
			puntaje.append(puntajeGanar)
			print("Puntaje Actual: ",sumaLista(puntaje))

		elif guardian == "Piedra" and jugador2 == "Papel":
			print(f"{registro} Ganas :3")
			print("---------------------------------------------")
			par=1
			partidas.append(par)
			print("Total de partidas: ",sumaLista(partidas))
			puntajeGanar=15
			puntaje.append(puntajeGanar)
			print("Puntaje Actual: ",sumaLista(puntaje))

		elif guardian == "Papel" and jugador2 == "Piedra":
			print("EL GUARDIAN DEL KERMES GANA :c")
			print("---------------------------------------------")
			par=1
			partidas.append(par)
			print("Total de partidas: ",sumaLista(partidas))
			puntajePerder=-10
			puntaje.append(puntajePerder)
			print("Puntaje Actual: ",sumaLista(puntaje))

		elif guardian == "Tijera" and jugador2 == "Papel":
			print("EL GUARDIAN DEL KERMES GANA :C")
			print("---------------------------------------------")
			par=1
			partidas.append(par)
			print("Total de partidas: ",sumaLista(partidas))
			puntajePerder=-10
			puntaje.append(puntajePerder)
			print("Puntaje Actual: ",sumaLista(puntaje))

		else:
			print("Empate.")
			print("---------------------------------------------")
			par=1
			partidas.append(par)
			print("Total de partidas: ",sumaLista(partidas))
			puntajeEmpatar=0
			puntaje.append(puntajeEmpatar)
			print("Puntaje Actual: ",sumaLista(puntaje))		
		
		break	


	while user != 1:
		try:
			print("------------------------------------------------")	
			user=int(input("¿Decides seguir jugando? 1_No C/N Si: "))
			print("------------------------------------------------")

			if user == 1:
				print("Ok volviendo al menu principal")
				time.sleep(1)
				Menu()
				regaloCodigo2()
				break

			else:
				PiedraPapelTijera()
				break
		except:
			print("Caracteres invalidos.")
			continue

#------------------------------------------------------------------------------------------------------
def regaloCodigo1():
	#si el usuario llega a mas de 100 puntos:
	if sumaLista(puntaje) >= 100:
		print("Genial llegaste a mas de 100 puntos, ingresa este codigo para volver a ese puntaje cuando vuelvas a jugar de nuevo.")
		print("CODIGO: 123450")

def regaloCodigo2():
	if sumaLista(puntaje) >= 500:
		print("Genial llegaste a mas de 500 puntos,ingresa este codigo para volver a ese puntaje cuando vuelvas a jugar de nuevo.")
		print("CODIGO: 34521")

def CodigoFinal():
	if sumaLista(puntaje) >= 1000:
		print("No sera un gran premio, pero cuando quieras ingresa 934892 para volver a los 1000 puntos. Gracias.")
		time.sleep(2)
		print(":3 anotalo por que esto se cerrara...")

#--------------------------------------------------------------------------
def Main():
	print("""------------------------------------------------------------------------                                                                                                                                                                                                               
 MMM.   ,PMM                                                     
 M`Mb   d'MM   ____  ___  __    __     _____     ____     ____   
 M YM. ,P MM  6MMMMb `MM 6MMb  6MMb   6MMMMMb   6MMMMb   6MMMMb  
 M `Mb d' MM 6M'  `Mb MM69 `MM69 `Mb 6M'   `Mb MM'  `Mb MM'  `Mb 
 M  YM.P  MM MM    MM MM'   MM'   MM MM     MM       MM      ,MM 
 M  `Mb'  MM MMMMMMMM MM    MM    MM MM     MM      .M9     ,MM' 
 M   YP   MM MM       MM    MM    MM MM     MM   MMMM     ,M'    
 M   `'   MM YM    d9 MM    MM    MM YM.   ,M9      `Mb ,M'      
_M_      _MM_ YMMMM9 _MM_  _MM_  _MM_ YMMMMM9        MM MMMMMMMM 
                                                     MM          
    .creado por Jeff McWill                    MM.  ,M9          
                                                YMMMM9           
""")

def Menu():
	apagado=0
	print("Bienvenido ",registro)
	print("""------------------------------------------------------------------------
el objetivo de estos minijuegos es llegar a mas de 1000 puntos. Suerte.
--------------------------------------

1.Dados

2.Piedra Papel O Tijera

3.Caja Misteriosa (1000)

--------------------------------------
4.Salir
------------------------------------------------------------------------""")
	print(f"Tu puntaje Actual: {sumaLista(puntaje)}")
	while apagado != 4:
		try:
			user=int(input("¿Que minijuego decides jugar?: "))

			if user == 1:
				print("Has Elegido *Dados*")
				print("Cargando...")
				time.sleep(2)
				DadosMenu()
				DadosMod()
				break

			if user == 2:
				print("Has elegido Piedra, Papel o Tijera")
				print("Cargando...")
				time.sleep(2)
				MenuPiedra()
				PiedraPapelTijera()
				break

			if user == 3:
				print("Tocaste la Caja Misteriosa...")
				if sumaLista(puntaje) >= 1000:
					time.sleep(1)
					print("La caja finalmente acepta tus puntos")
					time.sleep(1)
					print("Finalmente se abre...")
					time.sleep(1)
					print("Genial, HAS GANADO mi juego.")
					time.sleep(3)
					print("Muchas gracias por jugar a Memo32")
					time.sleep(3)
					print("Eres el ganador de ganadores o el hacker de hackers XD.")
					time.sleep(3)
					print("Se que pensabas que habria un mejor final, pero este es el final de este simple codigo")
					time.sleep(3)
					print("Gracias por jugar, esto parecera facil pero llevo su tiempo de realizacion.")
					time.sleep(3)
					print(f"Cuidate mucho... ten una larga vida,eres grande {registro}")
					time.sleep(3)
					print("Adios.")
					time.sleep(3)
					print("Jeff McWill. 30/09/22")
					time.sleep(5)
					print("-------------------------------------")
					print(f"Puntaje total: {sumaLista(puntaje)}")
					print("-------------------------------------")
					CodigoFinal()
					time.sleep(10)
					break

				elif sumaLista(puntaje) < 1000:
					print("---------------------------------------------------")
					print("Lo siento, vuelve cuando tengas mas de 1000 puntos.")
					print("---------------------------------------------------")
					Menu()
					break

			if user == 4:
				try:
					apagado=int(input("Decides apagar (4) SI / (cualquier) NO: "))
					if apagado == 4:
						print("De acuerdo.")
						time.sleep(1)
						print("Gracias por jugar.")
						print(f"Puntaje total: {sumaLista(puntaje)}")
						regaloCodigo1()
						break
					else:
						print("volviendo")
						continue
				except:
					print("Caracteres no validos.")
					continue
				break
		except:
			print("Caracteres no soportados, intentalo de nuevo...")
			continue

#------------------------------------------------------------------------------
#REGISTRO Y GUARDADO.
def PartidaGuardada():
	user=0
	apaga3=0
	print("Por cierto...")
	time.sleep(1)
	print("¿Tienes algun codigo de guardado?")

	while user != 2:
		try:		
			user=int(input(" 1. Si/ 2. No : "))
			if user == 1:
				try:
					print("¿De acuerdo dime el codex?: ")
					user=int(input(">> "))

					if user == 123450:
						print("Genial, ese es un codigo valido.")
						print("--------------------------------")
						print("Se te acreditaran 100 puntos.")
						print("--------------------------------")
						save1=100
						puntaje.append(save1)
						print(f"Puntaje actual: {sumaLista(puntaje)}")
						print("Ok continuemos al juego...")
						time.sleep(1)
						print(f"Bienvenido a mi Memo32 {registro}")
						time.sleep(1)
						print("Cargando Juegos...")
						time.sleep(1)
						Main()
						Menu()
						break

					elif user == 34521:
						print("Genial, ese es un codigo valido.")
						print("--------------------------------")
						print("Se te acreditaran 500 puntos.")
						print("--------------------------------")
						save1=500
						puntaje.append(save1)
						print(f"Puntaje actual: {sumaLista(puntaje)}")
						print("Ok continuemos al juego...")
						time.sleep(1)
						print(f"Bienvenido a Memo32 {registro}")
						time.sleep(1)
						print("Cargando Juegos...")
						time.sleep(1)
						Main()
						Menu()
						break

					elif user == 934892:
						print("Genial, ese es un codigo valido.")
						print("--------------------------------")
						print("Se te acreditaran 1000 puntos.")
						print("--------------------------------")
						save1=1000
						puntaje.append(save1)
						print(f"Puntaje actual: {sumaLista(puntaje)}")
						print("Ok continuemos al juego...")
						time.sleep(1)
						print(f"Bienvenido a Memo32 {registro}")
						time.sleep(1)
						print("Cargando Juegos...")
						time.sleep(1)
						Main()
						Menu()
						break

				except:
					print("Caracteres no admitidos. Agregue de nuevo.")
					continue

			elif user == 2:
				print("Ok continuemos al juego...")
				time.sleep(1)
				print(f"Bienvenido a Memo32 {registro}")
				time.sleep(1)
				print("Cargando Juegos...")
				time.sleep(1)
				Main()
				Menu()
				break
		except:
			print("Caracteres no soportados.")
			continue

def Registro():
	print("-----------------------")
	print("Bienvenido a Memo32.")
	print("-----------------------")
	time.sleep(1)
	print("Antes de empezar...")
	time.sleep(1)
	user=0
	while user != 1:

		try:
			print("""Agrega tu nombre de usuario.
Esto servira para que tu nombre aparezca en todos los juegos.""")
			user=input(">>> ")
			registro.append(user)
			PartidaGuardada()
			break

		except:
			print("Caracteres no soportados.")
			print("Los telones se cierran...")

def sumaLista(lista):
	suma=0
	for elem in lista:
		suma+=elem
	return suma

#------------------------------------------------------------------------------
if __name__=="__main__":
	Registro()
	#Recordar que solo registro se tiene que ejecutar.
	
