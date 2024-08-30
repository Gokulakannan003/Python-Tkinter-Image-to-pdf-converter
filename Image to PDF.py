from tkinter import *
from tkinter import filedialog
from PIL import Image
from reportlab.pdfgen import canvas


root = Tk()
root.title("Image to PDF Converter")
root.geometry("400x200")
root.configure(borderwidth=5, background="light green")
root.resizable(False, False)


def convert_image_to_pdf(image_path, pdf_path):
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Create a canvas with the size of the image
    c = canvas.Canvas(pdf_path, pagesize=(img_width, img_height))
    c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
    c.save()


def select_file():
    image_path = filedialog.askopenfilename(filetypes=[("Image file", "*.png;*.jpg;*.jpeg")])
    if image_path:
        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            convert_image_to_pdf(image_path, pdf_path)


lab = Label(root, background="light green")
lab.pack()

lab1 = Label(root, text="Image to PDF converter", background="light green", font=("Ariel", 18, "bold"))
lab1.pack()

lab2 = Label(root, background="light green")
lab2.pack()

btn = Button(root, text="Select Image", command=select_file, background="violet", font=("Ariel", 12, "bold"))
btn.pack(pady=20)

root.mainloop()
