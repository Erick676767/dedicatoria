import turtle
import time
import random
import winsound

# --- CONFIGURACIÓN DE LA VENTANA ---
ventana = turtle.Screen()
ventana.setup(width=1250, height=750)
ventana.bgcolor("black")
ventana.title("Para el amor de mi vida ❤️")
ventana.tracer(0)

# --- REPRODUCIR MÚSICA DE FONDO ---
try:
    winsound.PlaySound("musica.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
except Exception as e:
    print("Aviso de audio:", e)

# --- TU MENSAJE EXACTO Y ORIGINAL ---
mensaje = [
    "AMORCITOOOO como te lo prometí algun dia te",
    "haria algo como esto, te amo muchisimooooo",
    "gracias por estos hermosos 8 meses, fueron",
    "los mejores de mi vida porque llegaste a mi,",
    "quiero agradecerte por cada momento que",
    "pasamos juntos, por cada esfuerzo que hacias",
    "para entenderme HJASSAHJ poke yo sé que",
    "soy ps alguien algo loquito por asi decirlo,",
    "me encanta de verdad me encanta saber que",
    "estas a mi lado y que gracias a ti he logrado",
    "tantas cosas en mi vida, eres el motivo por",
    "el cual sigo adelante, te volviste la persona",
    "mas especial, te volviste mi mundo entero,",
    "solo t quiero a ti por siempre, quiero amarte",
    "y desearte por siempre, quiero que todo esto",
    "siga asi para siempre, poke cada segundo,",
    "cada minuto a tu lado me enseña nuevas",
    "cosas y me hace sentir muchas cosas,",
    "jamas pense amar a alguien como te amo a ti,",
    "eres lo mas hermoso de los 18 años que he",
    "pasado viviendo, gracias por absolutamente",
    "todo mi bb te amo muchisimo y nunca lo",
    "olvides chi?",
    "TE REAMOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO💖💞💖"
]

# --- TORTUGAS ---
girasol = turtle.Turtle()
girasol.hideturtle()
girasol.speed(0)

texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.color("white")

pos_x = 40
pos_y = 330
linea_altura = 16

# --- CORAZONES FLOTANTES (GLOBITOS) ---
corazones_simbolos = ["💕", "💖", "🌸", "✨", "💗", "❤️"]
corazones = []

for _ in range(22):
    t_corazon = turtle.Turtle()
    t_corazon.hideturtle()
    t_corazon.penup()
    if random.choice([True, False]):
        x = random.randint(-580, -450)
    else:
        x = random.randint(420, 580)
    y = random.randint(-350, -100)
    velocidad = random.uniform(2.0, 4.0)
    simbolo = random.choice(corazones_simbolos)
    
    corazones.append({
        "turtle": t_corazon, "x": x, "y": y, "vel": velocidad,
        "simbolo": simbolo, "tamano": random.randint(11, 16)
    })

def actualizar_corazones():
    for c in corazones:
        try:
            c["turtle"].clear()
            c["y"] += c["vel"]
            if c["y"] > 350:
                c["y"] = -360
                c["x"] = random.randint(-580, -450) if random.choice([True, False]) else random.randint(420, 580)
            c["turtle"].goto(c["x"], c["y"])
            c["turtle"].color("#FFB6C1")
            c["turtle"].write(c["simbolo"], align="center", font=("Arial", c["tamano"], "normal"))
        except:
            pass

def escribir_siguiente_linea():
    global pos_y
    if len(mensaje) > 0:
        linea = mensaje.pop(0)
        texto.goto(pos_x, pos_y)
        
        # Estilos en Rosa Pastel
        if "AMORCITOOOO" in linea:
            texto.color("#FFB6C1")
            texto.write(linea, align="left", font=("Georgia", 13, "bold"))
            texto.color("white")
        elif "TE REAMOOOO" in linea:
            texto.color("#FF69B4")
            texto.write(linea, align="left", font=("Georgia", 9, "bold"))
            texto.color("white")
        elif "8 meses" in linea or "18 años" in linea:
            texto.color("#FFC0CB")
            texto.write(linea, align="left", font=("Arial", 9, "bold"))
            texto.color("white")
        else:
            texto.write(linea, align="left", font=("Arial", 9, "normal"))
        pos_y -= linea_altura

# --- DIBUJAR EL GIRASOL ESTILO VIDEO ---
girasol.penup()
girasol.goto(-280, -120)
girasol.pendown()

# 1. Tallo y Hoja
girasol.color("darkgreen")
girasol.pensize(7)
girasol.setheading(90)
girasol.forward(180)

girasol.right(45)
girasol.begin_fill()
girasol.circle(40, 90)
girasol.left(90)
girasol.circle(40, 90)
girasol.end_fill()
girasol.left(45)

escribir_siguiente_linea()
escribir_siguiente_linea()

# 2. Centro del Girasol
centro_x = -280
centro_y = 90

girasol.penup()
girasol.goto(centro_x, centro_y - 25)
girasol.pendown()
girasol.color("#5C4033", "#3B2219")
girasol.begin_fill()
girasol.circle(30)
girasol.end_fill()

escribir_siguiente_linea()
escribir_siguiente_linea()

# 3. Pétalos
girasol.penup()
girasol.goto(centro_x, centro_y)
girasol.pendown()
girasol.pensize(2)

total_petalos = 28
for i in range(total_petalos):
    if i % 2 == 0:
        girasol.color("#FFD700", "#FFCC00")
    else:
        girasol.color("#FFA500", "#FF8C00")
        
    girasol.begin_fill()
    girasol.circle(95, 60)
    girasol.left(120)
    girasol.circle(95, 60)
    girasol.left(180 - (360 / total_petalos) + 60)
    girasol.end_fill()
    
    escribir_siguiente_linea()
    for _ in range(2):
        actualizar_corazones()
        try:
            ventana.update()
        except:
            break
        time.sleep(0.01)

# Escribir el resto del mensaje si queda
while len(mensaje) > 0:
    escribir_siguiente_linea()
    for _ in range(2):
        actualizar_corazones()
        try:
            ventana.update()
        except:
            break
        time.sleep(0.01)

# Mensaje final bajo el girasol
try:
    girasol.penup()
    girasol.goto(-280, -180)
    girasol.color("#FFB6C1")
    girasol.write("🌻 ¡Felices 8 Meses! 🌻", align="center", font=("Georgia", 15, "bold"))
except:
    pass

# Bucle infinito seguro para mantener los corazones flotando
while True:
    try:
        actualizar_corazones()
        ventana.update()
        time.sleep(0.03)
    except:
        break