"""
The program ll work with mysql soon. Add this !!!
"""


import time
import pyautogui as py
import tkinter

print("Initilazed... ", time.asctime())

root = tkinter.Tk()
root.title("Lets roll... ")
root.geometry("150x250+200+200")
canvas = tkinter.Canvas(root, width=150, height=250)
canvas.grid(columnspan=3, rowspan=5)

user_entry = tkinter.Entry(root)
user_entry.grid(row=0, column=0, columnspan=3)

coord_list = []


def start_recording(n):
    print("Recording is in progress...//...")
    for n in range(n):
        x1, y1 = py.position()[0], py.position()[1]
        coords = (str(x1)+"-"+str(y1))
        time.sleep(.1)
        coord_list.append(coords)
    with open("recording.csv", "w") as f:
        for line in coord_list:
            line = str(line)
            f.write(f"{line}\n")
    print("Recording complated.")
    return


def play_recording():
    datalist=open("recording.csv", "r")
    if datalist is not None:
        print("Playing is in progress...//...")
        for line in datalist:
            line = line.split("-")
            x1 = int(line[0])
            y1 = line[1]
            y1 = int(y1[0:-1])
            py.moveTo(x1, y1)
    datalist.close
    print("Playing completed.")
    return


def button_click():
    current = user_entry.get()
    current = int(current)
    user_entry.delete(0, tkinter.END)
    print(current)
    start_recording(current)
    return


record_button = tkinter.Button(root,
                               text="Record",
                               font="Raleway",
                               bg="#eb3535",  # Better for logo2:#eb3535//logo1:#20bebe
                               fg="white",
                               height=2, width=13,
                               command=button_click)
record_button.grid(row=2, column=1)


play_button = tkinter.Button(root,
                              text="Play",
                              font="Raleway",
                              bg="#eb3535",  # Better for logo2:#eb3535//logo1:#20bebe
                              fg="white",
                              height=2, width=13,
                              command=play_recording)
play_button.grid(row=3, column=1)


quit_button = tkinter.Button(root,
                             text="Quit",
                             font="Raleway",
                             bg="#eb3535",  # Better for logo2:#eb3535//logo1:#20bebe
                             fg="white",
                             height=2, width=13,
                             command=root.destroy)
quit_button.grid(row=4, column=1)


root.mainloop()
print("Terminated...", time.asctime())
