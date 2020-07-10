print("LLevar un estilo de vida saludable permite prevenir diversas enfermedades. "
      "\n" "El siguiente test te ayudará a conoceer como estas llevando tu estilo de vida")

test = ["¿Cuántas horas duerme por día?""\n"
        "A. Menos de seis""\n""B. Entre seis y siete""\n""C. Como mínimo siete",
        "¿Qué cantidad de agua toma por día?""\n"
        "A. Menos de cuatro vasos""\n""B. Entre cuatro y siete vasos""\n""C. Ocho o más vasos",
        "¿Come frutas y verduras (ambas)?""\n"
        "A. Casi nunca""\n""B. Casi siempre""\n""C. Todos los días",
        "¿En qué consiste su típico desayuno?""\n"
        "A. Infusión con frituras o más de dos rodajas de pan, tostadas o galletitas con mermelada, dulce de leche o manteca""\n"
        "B. Infusión con una o dos rodajas de pan, tostadas o galletitas de agua con queso o mermelada light siempre""\n"
        "C. Alterno entre la opción B e infusión con frutas o yogurt o queso bajo en grasas",
        "En las 14 comidas principales (almuerzos y cenas) que realiza en una semana, ¿qué tipo de comida prevalece?""\n"
        "A. Comidas rápidas (pizzas, hamburguesas, alimentos precocidos/prefritos)""\n"
        "B. Solo frutas y verduras""\n"
        "C. Variedad de frutas, verduras, pescados, carne magra, pollo, pastas, legumbres",
        "¿Realiza entre cuatro y seis comidas?""\n"
        "A. No""\n""B. Cuando puedo""\n""C. Sí",
        "Después de cenar…"
        "\n""A. Se acuesta inmediatamente""\n""B. Deja pasar una hora y después se acuesta""\n""C. Espera más de una hora antes de irse a dormir",
        "¿Cuántas veces por semana hace ejercicio (mínimo media hora por día)?""\n"
        "A. Cuando tiene tiempo o nunca""\n""B. Dos o tres veces""\n""C. Por lo menos cuatro veces",
        "¿Cuántas horas seguidas pasa sentado durante el día?""\n""A. Más de seis""\n""B. Entre tres y seis""\n""C. Tres o menos",
        "¿Cuánto alcohol bebe por día?""\n""A. Más de un vaso""\n""B. Un vaso""\n""C. Nada",
        "¿Fuma?""\n""A. Sí""\n""B. A veces (uno o dos cigarrillos por día mínimo)""\n""C. No"
             ]

contA = 0
contB = 0
contC = 0

A = "No está llevando un estilo de vida saludable.Deberá enfocarse en mejorar su alimentación, disminuir la cantidad de ""\n""tiempo que pasa sentado y realizar actividad física con regularidad. ¡No se desanime! Al contrario, para ""\n""poder realizar las modificaciones necesarias para mejorar ""\n""su calidad de vida tiene que estar de buen ""\n""ánimo y predispuesto a ir para adelante. Empiece lentamente y ""\n""verá cómo de a poco se va a sentir mejor."
B = "Su estilo de vida es medianamente saludable, sin embargo hay puntos claves a mejorar. Intente ir modificando los ""\n""malos hábitos de a poco. ¡Hay cosas que las está realizando muy bien! Solo falta un último empujoncito para ""\n""llegar a un estado óptimo que le brindará importantes beneficios. ""\n""¡Cuánto antes accione, será mejor!"
C = "Usted lleva un estilo de vida saludable en líneas generales. Es importante ser constante, mantener los buenos ""\n""hábitos y prolongarlos en el tiempo. Si algunas de sus respuestas fueron A o B, intente modificar ese hábito ""\n""para mejorar lo que le falta. Siga en esa dirección y estará más fuerte y sano."

for i in range(len(test)):
    print(test[i], end=" ")
    r = input("\n""Respuesta: ")
    if r == "A":
        contA += 1
    elif r == "B":
        contB += 1
    elif r == "C":
        contC += 1



if contA > contB and contA > contC:
    print(A)
elif contB > contA and contB > contC:
    print(B)
elif contC > contB and contC > contA:
    print(C)