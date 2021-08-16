import tkinter as tk
from PIL import Image, ImageTk
import random
import urllib.request as req

#占い結果
def result():
    happy = ["超ハッピー","ハッピー","アンハッピー"]
    lbl.configure(text="占い結果\n"+random.choice(happy))

#画面用部品
wind = tk.Tk()
wind.geometry("800x800")

lbl = tk.Label(text="ねこねこ占い")
img = tk.Label(text="ねこねこ占い")
btn = tk.Button(text="占う", command = result)

#画面に配置
lbl.pack()
btn.pack()
tk.mainloop()
