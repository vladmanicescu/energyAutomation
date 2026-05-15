#name = input("Va rog sa va introduceti numele:")
#print("Neata", name)


# import requests as rq
#
# numele_orasului = "Bucharest"
# API_key = "814cee81777d34406378ca413e79f2e0"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={numele_orasului}&appid={API_key}&units=metric"
#
# response = rq.get(url)
# if response.status_code == 200:
#     print(response.json())
#     temperatura = response.json()["main"]["temp"]
#     print(temperatura)
# else:
#     print(response.status_code)

import requests as rq
import tkinter as tk
from tkinter import font

# ── Configurare API ──────────────────────────────────────
numele_orasului = "Bucharest"
API_key = "814cee81777d34406378ca413e79f2e0"
url = f"https://api.openweathermap.org/data/2.5/weather?q={numele_orasului}&appid={API_key}&units=metric&lang=ro"

# ── Funcție fetch date ───────────────────────────────────
def get_weather():
    response = rq.get(url)
    if response.status_code == 200:
        data = response.json()

        temperatura = data["main"]["temp"]
        lbl_temp.config(text=f"🌡️ Temperatura: {temperatura}°C")
        lbl_status.config(text="✅ Date actualizate!", fg="green")
    else:
        lbl_status.config(text=f"❌ Eroare: {response.status_code}", fg="red")

# ── Fereastra principală ─────────────────────────────────
root = tk.Tk()
root.title("🌤️ Vremea în București - app Beatrice") # titlul aplicatiei
root.geometry("400x200")
root.configure(bg="purple")

# Fonturi
font_title  = font.Font(family="Arial", size=18, weight="bold")
font_info   = font.Font(family="Arial", size=13)
font_btn    = font.Font(family="Arial", size=12, weight="bold")
font_status = font.Font(family="Arial", size=10)

# Titlu e din root
tk.Label(root, text="🌍 Vremea în București",          # titlul afisat pe pagina
         font=font_title, bg="purple", fg="yellow").pack(pady=15)

# Frame date
frame = tk.Frame(root, bg="#55efc4", bd=0, relief="groove")
frame.pack(padx=20, pady=5, fill="both", expand=True)

# Label temperatura sa apara in frame-ul de date
lbl_temp = tk.Label(frame, text="🌡️ Temperatura: --",
                    font=font_info, bg="#2c3e50", fg="white", anchor="center")
lbl_temp.pack(padx=15, pady=10, fill="x")

# ── Buton Refresh
tk.Button(root, text="🔄 Actualizează",
          font=font_btn, bg="#0984e3", fg="white",
          bd=0, padx=10, pady=6,
          command=get_weather).pack(pady=12)

# ── Status ───────────────────────────────────────────────
lbl_status = tk.Label(root, text="Se încarcă...",
                      font=font_status, bg="purple", fg="white")
lbl_status.pack()

# ── Start ────────────────────────────────────────────────
get_weather()
root.mainloop()