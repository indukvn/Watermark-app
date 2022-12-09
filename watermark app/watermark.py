import tkinter
# filedialog to select the file/directory of image
from tkinter import Button, Entry, Label, filedialog
from PIL import Image, ImageDraw, ImageFont


def load_files():
    img = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=[('Jpg Files', '*.jpg')])

    # RGBA (red, green, blue, alpha)
    with Image.open(img).convert("RGBA") as bg_img:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", bg_img.size, (255, 255, 255, 0))

        # select font type and size
        font = ImageFont.truetype("arial.ttf", 128, encoding="unic")
        # get a drawing context/object
        d = ImageDraw.Draw(txt)

        water_mark = input_dta.get()
        # draw text, half opacity
        d.text((bg_img.size[0] // 10, bg_img.size[1] // 10), water_mark, font=font, fill=(255, 255, 255, 128))

        outpt = Image.alpha_composite(bg_img, txt)
        outpt.show()


window = tkinter.Tk()
window.title("Add watermark Application")
window.minsize(width=600, height=200)
window.config(padx=10, pady=10, background="white")


#label
my_label = Label(text="Add text Watermark to your images using Python", font=("Arial", 24, "bold"), bg="white")
my_label.grid(row=0, column=0, columnspan=4)

text_label = Label(text="Enter the text you want to watermark: ", pady=10)
text_label.grid(row=1, column=0)

#text input
input_dta = Entry(width=60)
input_dta.grid(row=1, column=1, columnspan=2)

#button
button = Button(text="Upload Jpg images", command=load_files)
button.grid(rowspan=2, column=1, columnspan=2)


window.mainloop()