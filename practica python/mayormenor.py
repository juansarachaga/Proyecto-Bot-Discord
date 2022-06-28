 preg= int(input("Cantidad de preguntas realizadas: "))
 corr= int(input("Cantidad de respuestas correctas: "))
 porc= (corr * 100) /preg
 
 if porc>=90:
    print ("Nivel maximo")
 else:
     if porc>=75:
         print ("Nivel medio")
     else:
         if porc>=50:
             print("Nivel regular")
         else:
             if porc<50:
                 print("Fuera de nivel")      