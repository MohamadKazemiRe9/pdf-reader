from tkinter.filedialog import askopenfilename
import PyPDF2
from tkinter import *
import pyttsx3


window = Tk()
window.title("کتابخوان")

window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)


def open_file():
    file= askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    if file:
        pdf_file= PyPDF2.PdfFileReader(file)
        page_numbers = pdf_file.numPages
        for page in range(page_numbers):
            try:
                current_page = pdf_file.getPage(page)
                text = current_page.extractText()
                txt_edit.insert(END, text)
            except:
                pass


def read_file():
    text = txt_edit.get('1.0', END).splitlines()
    for line in text:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(line)
        engine.runAndWait()


txt_edit = Text(window)
frm_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(frm_buttons, text="باز کردن", command=open_file)
btn_read = Button(frm_buttons, text="خواندن فایل", command=read_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_read.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()