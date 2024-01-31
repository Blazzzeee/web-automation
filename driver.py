from fox import fox
import customtkinter
from PIL import Image, ImageTk, ImageDraw

window = fox()

def create_gui():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    app = customtkinter.CTk()
    app.geometry("420x260")
    label=customtkinter.CTkLabel(master=app, text='')
    original_image = Image.open("C:\\Users\\GEET KHURANA\\My-Python-Packages\\web-automation\\bg.jpeg")
    
    resized_image = original_image.resize((int(400 * 1.2), int(240 * 1.2)), Image.LANCZOS)

    background_image = resized_image.convert("RGBA")

    label_image = Image.new("RGBA", (int(400 * 1.2), int(240 * 1.2)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(label_image)
    label_text = "Server Status: Online" if window.instance else "Server Status: Offline"
    text_width, text_height = draw.textsize(label_text)
    draw.text((305,40), label_text, fill=(255, 255, 255, 255))
    
    
    combined_image = Image.alpha_composite(background_image, label_image)
    combined_photo_image = ImageTk.PhotoImage(combined_image)

    background_label = customtkinter.CTkLabel(app, image=combined_photo_image,text=' ')
    background_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    
    
    button = customtkinter.CTkButton(master=app, text="Login", command=lambda: window.login())
    button.place(x=15,y=120 )



    button2 = customtkinter.CTkButton(master=app, text="Connect to server", command=lambda: window.launch() )
    button2.place(x=15,y=15)
    
    
    label.pack()
    app.mainloop()
    window.launch() 

create_gui()