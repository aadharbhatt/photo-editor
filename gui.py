import Tkinter as tk
from PIL import ImageTk, Image
import script

img_path = "img2.jpg"
img_temp = "01.jpg"


def show1(img_path="img1.jpg"):
    myimg = ImageTk.PhotoImage(Image.open(img_path).resize((300,200), Image.ANTIALIAS))
    label_view1= tk.Label(image=myimg,highlightthickness=2,relief="sunken")
    label_view1.image = myimg
    label_view1.place(x=30,y=270)

def show2(img_temp="img2.jpg"):
    myimg_op = ImageTk.PhotoImage(Image.open(img_temp).resize((300,200), Image.ANTIALIAS))
    label_view2= tk.Label(image=myimg_op,highlightthickness=2,relief="sunken")
    label_view2.image = myimg_op
    label_view2.place(x=350,y=270)

def func_selector(name):
    func_dict[name]
    show1(img_path)
    show2(img_temp)

    func_dict = {
        "b1":script.blur(img_path),
        "b2":script.edge_detection(img_path),
        "b3":script.Enhance(img_path),
        "b4":script.motion_blur(img_path),
        "b5":script.sharp(img_path),
        "b6":None,
        "b7":None,
    }

class pe():
    master = tk.Tk()
    master.title("Photo Editor")
    master.resizable(width=False, height=False)
    master.geometry('{}x{}'.format(700, 500))
    master.iconbitmap("images/icon.ico")

    top_frame = tk.Frame(master, height=20).grid(column=None, row=0)

    b1 = tk.Button(master, text='Blur', width=25, command=func_selector('b1')).grid(column=0, row=1, padx=20, pady=20)
    b2 = tk.Button(master, text='Edge Detection', width=25, command=func_selector('b2')).grid(column=1, row=1, padx=20,
                                                                                              pady=20)
    b3 = tk.Button(master, text='Enhance', width=25, command=func_selector('b3')).grid(column=2, row=1, padx=20,
                                                                                       pady=20)
    b4 = tk.Button(master, text='Motion Blur', width=25, command=func_selector('b4')).grid(column=0, row=2, padx=20,
                                                                                           pady=20)
    b5 = tk.Button(master, text='Sharp', width=25, command=func_selector('b5')).grid(column=1, row=2, padx=20, pady=20)
    b6 = tk.Button(master, text='b6', width=25, command=func_selector('b6')).grid(column=2, row=2, padx=20, pady=20)
    b7 = tk.Button(master, text='save', width=25, command=func_selector('b7')).grid(column=2, row=3, padx=20, pady=20)

if __name__ == '__main__':

    pic_edit = pe
    pic_edit.master.mainloop()
