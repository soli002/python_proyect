import xlrd
#No de filas= sheet.nrows
#No de columnas= sheet.ncols)

filePath = "C:\\python_proyect\\DATA PROYECTO 2 ICC.xlsx"
openFile= xlrd.open_workbook(filePath)

sheet = openFile.sheet_by_name("Tipo")
sheet1 = openFile.sheet_by_name("Femenino")
sheet2 = openFile.sheet_by_name("Masculino")
sheet3 = openFile.sheet_by_name("Departamento")

w =input("Mostrar tablas de cancer por genero y total? ")
if w.lower()=="si":
    print("General")
    for i in range(sheet.nrows):
        print(sheet.cell_value(i,0)," ",sheet.cell_value(i,1)," ",sheet.cell_value(i,2)," ",sheet.cell_value(i,3)," ",sheet.cell_value(i,4)," ",sheet.cell_value(i,5)," ",sheet.cell_value(i,6)," ",sheet.cell_value(i,7)," ",sheet.cell_value(i,8)," ",sheet.cell_value(i,9)," ", sheet.cell_value(i,10))
    print("")
    print("")
    print("Femenino")
    for e in range(sheet1.nrows):
        print(sheet1.cell_value(e,0)," ",sheet1.cell_value(e,1)," ",sheet1.cell_value(e,2)," ",sheet1.cell_value(e,3)," ",sheet1.cell_value(e,4)," ",sheet1.cell_value(e,5)," ",sheet1.cell_value(e,6)," ",sheet1.cell_value(e,7)," ",sheet1.cell_value(e,8)," ",sheet1.cell_value(e,9)," ", sheet1.cell_value(e,10))
    print("")
    print("")
    print("Masculino")
    for I in range(sheet2.nrows):
        print(sheet2.cell_value(I,0)," ",sheet2.cell_value(I,1)," ",sheet2.cell_value(I,2)," ",sheet2.cell_value(I,3)," ",sheet2.cell_value(I,4)," ",sheet2.cell_value(I,5)," ",sheet2.cell_value(I,6)," ",sheet2.cell_value(I,7)," ",sheet2.cell_value(I,8)," ",sheet2.cell_value(I,9)," ", sheet2.cell_value(I,10))
    print("")
    print("")
else: print("")

Q=input("Quiere saber los numeros de cancer por año? ")

if Q.lower()=="si":
    x=int(input("ingrese año para cancer masculino: "))
    if 2008<x<2019:
        if x==2009:
            x=1
        if x==2010:
            x=2
        if x==2011:
            x=3
        if x==2012:
            x=4
        if x==2013:
            x=5
        if x==2014:
            x=6
        if x==2015:
            x=7
        if x==2016:
            x=8
        if x==2017:
            x=9
        if x==2018:
            x=10
        else:
            print("No tenemos esos datos")
        if 0<x<11:
            for o in range(sheet2.nrows):
                print(sheet2.cell_value(o,0),sheet2.cell_value(o,x))
        print("")
        print("")

if Q.lower()=="si":
    y=int(input("ingrese año para cancer femino: "))
    if 2008<y<2019:
        if y==2009:
            y=1
        if y==2010:
            y=2
        if y==2011:
            y=3
        if y==2012:
            y=4
        if y==2013:
            y=5
        if y==2014:
            y=6
        if y==2015:
            y=7
        if y==2016:
            y=8
        if y==2017:
            y=9
        if y==2018:
            y=10
        else:
            print("No tenemos esos datos")
        if 0<y<11:
            for O in range(sheet1.nrows):
                print(sheet1.cell_value(O,0),sheet1.cell_value(O,y))
        print("")
        print("")

if Q.lower()=="si":
    z=int(input("ingrese año para cancer para todas las personas: "))
    if 2008<z<2019:
        if z==2009:
            z=1
        if z==2010:
            z=2
        if z==2011:
            z=3
        if z==2012:
            z=4
        if z==2013:
            z=5
        if z==2014:
            z=6
        if z==2015:
            z=7
        if z==2016:
            z=8
        if z==2017:
            z=9
        if z==2018:
            z=10
        else:
            print("No tenemos esos datos")
        if 0<z<11:
            for o in range(sheet.nrows):
                print(sheet.cell_value(o,0),sheet.cell_value(o,z))
        print("")
        print("")
else:
    print("")

r=input("Quiere saber la cantidad de personas con cancer por genero? ")
if r.lower()=="si":
    R=input("Masculino: ")
    if R.lower()=="si":
        for I in range(sheet2.nrows):
            print(sheet2.cell_value(I,0)," ",sheet2.cell_value(I,1)," ",sheet2.cell_value(I,2)," ",sheet2.cell_value(I,3)," ",sheet2.cell_value(I,4)," ",sheet2.cell_value(I,5)," ",sheet2.cell_value(I,6)," ",sheet2.cell_value(I,7)," ",sheet2.cell_value(I,8)," ",sheet2.cell_value(I,9)," ", sheet2.cell_value(I,10))
    else:
        print("")
    F=input("Femenino: ")
    if F.lower()=="si":
        for e in range(sheet1.nrows):
            print(sheet1.cell_value(e,0)," ",sheet1.cell_value(e,1)," ",sheet1.cell_value(e,2)," ",sheet1.cell_value(e,3)," ",sheet1.cell_value(e,4)," ",sheet1.cell_value(e,5)," ",sheet1.cell_value(e,6)," ",sheet1.cell_value(e,7)," ",sheet1.cell_value(e,8)," ",sheet1.cell_value(e,9)," ", sheet1.cell_value(e,10))
    else:
        print("")
else:
    print("")

K=input("Quiere saber la cantidad de personas por departamento en el Perú con cancer? ")
if K.lower()=="si":
    M=input("Que departamento? ")
    if M.lower() == "amazonas":
        M=1
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "ancash":
            M=2
            for I in range(sheet2.ncols+1):
                print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "apurimac":
        M=3
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "arequipa":
        M=4
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "ayacucho":
        M=5
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "cajamarca":
        M=6
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "callao":
        M=7
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "cusco":
        M=8
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "huancavelica":
        M=9
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "huanuco":
        M=10
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "ica":
        M=11
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "junin":
        M=12
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "la libertad":
        M=13
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "lambayeque":
        M=14
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "lima":
        M=15
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "provincia de lima":
        M=16
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "region de lima":
        M=17
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "loreto":
        M=18
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "madre de dios":
        M=19
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "moquegua":
        M=20
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "pasco":
        M=21
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "piura":
        M=22
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "puno":
        M=23
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "san martin":
        M=24
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "tacna":
        M=25
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "tumbes":
        M=26
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "ucayali":
        M=27
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
    elif M.lower() == "total":
        M=28
        for I in range(sheet2.ncols+1):
            print(sheet3.cell_value(0,I), sheet3.cell_value(M,I))
