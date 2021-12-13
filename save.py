from tkinter import *
from PIL import ImageTk, Image

# paths for images in GUI
pathtophoto1 = Image.open("/Users/sweet/Downloads/phone.gif")
pathtophoto2 = Image.open("/Users/sweet/Downloads/landscape.gif")
pathtophoto3 = Image.open("/Users/sweet/Downloads/food1.gif")
pathtophoto4 = Image.open("/Users/sweet/Downloads/resource.gif")
pathtophoto5 = Image.open("/Users/sweet/Downloads/resource.gif")
pathtophoto6 = Image.open("/Users/sweet/OneDrive/Documents/hope and a home.png")
pathtophoto7 = Image.open("/Users/sweet/OneDrive/Documents/ccvn.jpeg")
pathtophoto8 = Image.open("/Users/sweet/OneDrive/Documents/dash.png")
pathtophoto9 = Image.open("/Users/sweet/OneDrive/Documents/Samaritan-Inns-Vaccination-Banner.jpg")
pathtophoto10 = Image.open("/Users/sweet/OneDrive/Documents/Housing-and-Shelter-Landing-Banner.png") #adams emergency shelter
pathtophoto11 = Image.open("/Users/sweet/OneDrive/Documents/coalition.png") #coalition for the homeless
pathtophoto12 = Image.open("/Users/sweet/OneDrive/Documents/NCCF.jpeg") #new begging famliy shelter
pathtophoto13 = Image.open("/Users/sweet/OneDrive/Documents/emeryhouse_program_large.jpg") #Emery Work Bay
pathtophoto14 = Image.open("/Users/sweet/OneDrive/Documents/central misson union.jpeg")#Central Union Mission
pathtophoto15 = Image.open("/Users/sweet/OneDrive/Documents/isaiah.png")#saiah House Day Program
pathtophoto16= Image.open("/Users/sweet/OneDrive/Documents/georgetown-ministry-center.png") #Georgetown Ministry Center
pathtophoto17= Image.open("/Users/sweet/OneDrive/Documents/christ housee.png") #Christ House
pathtophoto18= Image.open("/Users/sweet/OneDrive/Documents/harriet tubman.png")#harriet tubman for women
pathtophoto19= Image.open("/Users/sweet/OneDrive/Documents/801 east.jpg")#801 East Men's Shelter
 #main page
root = Tk()

# sets screen size
root.geometry("1500x1000")

# Allow Window to be resizable
root.resizable(width=True, height=True)

# title of screen
root.title("HelpTheHomies")

# set window to one solid color
root.configure(bg='#8BCAD0')

# main page text
myLabel1 = Label(root, text='Help The Homies', bg="#8BCAD0", padx=100, pady=50, width=200)
myLabel1.config(font=("Courier", 44))
myLabel1.pack()
# Label(root, text = 'Help The Homies', font =('Alex Brush', 25)).pack(side = TOP, padx = 200, pady = 50)
# img= Image.open("/Users/imanicoleman/Downloads/icon.png")
photo = PhotoImage(file="/Users/sweet/Downloads/icon.png")
photoimage = photo.subsample(1, 2)
Button(root, image=photoimage, ).place(x=450, y=250)


def NewWindow():
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Main Screen")

    # sets the geometry of toplevel
    newWindow.geometry("1500x1000")
    newWindow.configure(bg='#FFA500')
    Label(newWindow, text='Welcome to Help the Homies', bg='#FFA500', font=(
        'Trajan Pro', 25)).pack(side=TOP, pady=10)
    # setting shelter image within the new window
    image1 = ImageTk.PhotoImage(pathtophoto1)
    panel1 = Label(newWindow, image=image1, width=150, height=150, )
    panel1.image = image1  # keep a reference
    panel1.place(x=100, y=500)
    # setting landscape image
    image2 = ImageTk.PhotoImage(pathtophoto2)
    panel2 = Label(newWindow, image=image2, width=1500, height=300)
    panel2.image = image2
    panel2.place(x=-5, y=150)
    # setting food image
    image3 = ImageTk.PhotoImage(pathtophoto3)
    panel3 = Label(newWindow, image=image3, width=150, height=150)
    panel3.image = image3
    panel3.place(x=500, y=500)
    # setting Resource image
    # image4 = ImageTk.PhotoImage(pathtophoto4)
    # panel4 = Label(newWindow, image=image4, width=150, height=150)
    # panel4.image = image4
    # image4.place(x=500, y = 200)
    # setting phone image
    #     image5 = ImageTk.PhotoImage(image = pathtophoto5)
    #     panel5 = Label(newWindow, image = image5, width = 150, height = 150)
    #     panel5.image = image5
    #     image5.place(x = 500, y = 200)

    # bottom text
    hotline_text = Label(newWindow, text="Service Hotline: (800) 535-7252", bg='#FFA500', font=("Courier", 16))
    hotline_text.place(x=570, y=750)


    food_page = Button(newWindow, text="Food Resources",font="Courier",command=Foodwindow)
    food_page.place(x=500, y=700)

    phone_page = Button(newWindow, text="Place a call",font="Courier",command=Phonewindow)
    phone_page.place(x=100, y=700)

    shelter_page = Button(newWindow, text="Shelters",font="Courier",command=Shelterwindow)
    shelter_page.place(x=900, y=700)

    resources_page = Button(newWindow, text="Looking for Additional Resources",font="Courier",command=Resourceswindow)
    resources_page.place(x=1100, y=700)

    # a button widget which will open a
    # new window on button click



def Shelterwindow():
    Shelterwindow = Toplevel(root)
    Shelterwindow.title("Shelter")
    Shelterwindow.geometry("1500x1000")
    Shelterwindow.configure(bg='#FFA500')
    Label(Shelterwindow, text='List of shelters', bg='#FFA500', font=(
        'Courier', 25)).pack(side=TOP, pady=10)
    myLabel2 = Label(Shelterwindow, text='We provide a directory of shelters that provide assistance to the homeless.')
    myLabel3 = Label(Shelterwindow, text='We do not directly provide aid ourselves, but provide local resources for you to find.')
    myLabel2.config(font=("Courier", 14))
    myLabel3.config(font=("Courier", 14))
    myLabel2.pack()
    myLabel3.pack()
    Shelterwindow.title("Shelter")
    # using image.open function and PhotoImage function to open the spcified image and display on the screen
    img = ImageTk.PhotoImage(pathtophoto6)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=100, y=500)

    img = ImageTk.PhotoImage(pathtophoto7)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=300, y=500)

    img = ImageTk.PhotoImage(pathtophoto8)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=500, y=500)

    img = ImageTk.PhotoImage(pathtophoto9)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=700, y=500)

    img = ImageTk.PhotoImage(pathtophoto10)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=900,y=500)

    img = ImageTk.PhotoImage(pathtophoto11)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=1100,y=500)

    img = ImageTk.PhotoImage(pathtophoto12)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=1300,y=500)

    img = ImageTk.PhotoImage(pathtophoto13)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=100,y=100)

    img = ImageTk.PhotoImage(pathtophoto14)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=300, y=100)

    img = ImageTk.PhotoImage(pathtophoto15)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=500, y=100)

    img = ImageTk.PhotoImage(pathtophoto16)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=700, y=100)

    img = ImageTk.PhotoImage(pathtophoto17)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=900, y=100)

    img = ImageTk.PhotoImage(pathtophoto18)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=1100,y=100)
    img = ImageTk.PhotoImage(pathtophoto19)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=1300,y=100)


def Phonewindow():
    Phonewindow = Toplevel(root)
    Phonewindow.title("Phone")
    Phonewindow.geometry("1500x1000")
    Phonewindow.configure(bg='#FFA500')
    Label(Phonewindow, text='Make a Call', bg='#FFA500', font=(
        'Courier', 25)).pack(side=TOP, pady=10)

def Foodwindow():
    Foodwindow = Toplevel(root)
    Foodwindow.title("Food")
    Foodwindow.geometry("1500x1000")
    Foodwindow.configure(bg='#FFA500')
    Label(Foodwindow, text='Food Pantries', bg='#FFA500', font=(
        'Courier', 25)).pack(side=TOP, pady=10)
def Resourceswindow():
    Resourceswindow = Toplevel(root)
    Resourceswindow.title("Resources")
    Resourceswindow.geometry("1500x1000")
    Resourceswindow.configure(bg='#FFA500')
    Label(Resourceswindow, text='Looking for Additional Resources?', bg='#FFA500', font=(
        'Courier', 25)).pack(side=TOP, pady=10)


# a button widget which will open a
# new window on button click
main_page_btn = Button(root, text="Tap to Begin",font= ("Courier",25) ,command=NewWindow)

main_page_btn.place(x=600, y=600)

# figure out how to change color of background and text of button on mac
# myButton = Button(root, text="click", command=myClick, fg="blue",bg="blue")

# allows program to continue looping
if __name__ == "__main__":
    root.mainloop()
