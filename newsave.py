from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

# paths for images in GUI
pathtophoto1 = Image.open("/Users/imanicoleman/Downloads/shelter.gif")
pathtophoto2 = Image.open("/Users/imanicoleman/Downloads/landscape.gif")
pathtophoto3 = Image.open("/Users/imanicoleman/Downloads/food1.gif")
pathtophoto4 = Image.open("/Users/imanicoleman/Downloads/resource.gif")
pathtophoto5 = Image.open("/Users/imanicoleman/Downloads/resource.gif")
pathtophoto6 = Image.open("/Users/imanicoleman/Downloads/hope.gif")
pathtophoto7 = Image.open("/Users/imanicoleman/Downloads/ccvn.gif")
pathtophoto8 = Image.open("/Users/imanicoleman/Downloads/dash.gif")
pathtophoto9 = Image.open("/Users/imanicoleman/Downloads/smaritton.gif")
pathtophoto10 = Image.open("/Users/imanicoleman/Downloads/adams.gif")
pathtophoto11 = Image.open("/Users/imanicoleman/Downloads/coalition.gif")
pathtophoto12 = Image.open("/Users/imanicoleman/Downloads/NCCF.gif")
pathtophoto13 = Image.open("/Users/imanicoleman/Downloads/emeryhouse.gif")
pathtophoto14 = Image.open("/Users/imanicoleman/Downloads/central.gif")
pathtophoto15 = Image.open("/Users/imanicoleman/Downloads/isaiah.gif")
pathtophoto16= Image.open("/Users/imanicoleman/Downloads/georgetown.gif")
pathtophoto17= Image.open("/Users/imanicoleman/Downloads/christ.gif")
pathtophoto18= Image.open("/Users/imanicoleman/Downloads/harriet.gif")
pathtophoto19= Image.open("/Users/imanicoleman/Downloads/801 east.gif")




#what i added !!!
pathtophotodc = Image.open("/Users/imanicoleman/Downloads/alp.gif")
pathtophotobleft = Image.open("/Users/imanicoleman/Downloads/left-border.gif")
pathtophotobright = Image.open("/Users/imanicoleman/Downloads/right-border.gif")
pathtophotothrive = Image.open("/Users/imanicoleman/Downloads/thrivedc.gif")
pathtophotochurch = Image.open("/Users/imanicoleman/Downloads/church.gif")
pathtophotoSOME = Image.open("/Users/imanicoleman/Downloads/SOME.gif")
pathtophotoFTF = Image.open('/Users/imanicoleman/Downloads/FTF.gif')
pathtophotoBeacon = Image.open('/Users/imanicoleman/Downloads/beacon.gif')
pathtophotoCenter = Image.open('/Users/imanicoleman/Downloads/center.gif')
pathtophotoNCC = Image.open('/Users/imanicoleman/Downloads/NCC.gif')

# main page
root = Tk()


# sets screen size
root.geometry("1500x1000")

# Allow Window to be resizable
root.resizable(width = True, height = True)

# title of screen
root.title("HelpTheHomies")

# set window to one solid color
root.configure(bg = '#FFA500')

# main page text
myLabel1 = Label(root, text='Help The Homies', bg = "#FFA500", padx = 100, pady = 50,width = 200)
myLabel1.config(font = ("Courier", 44))
myLabel1.pack()
# Label(root, text = 'Help The Homies', font =('Alex Brush', 25)).pack(side = TOP, padx = 200, pady = 50)
# img= Image.open("/Users/imanicoleman/Downloads/icon.png")
photo = PhotoImage(file = "/Users/imanicoleman/Downloads/icon.gif")
photoimage = photo.subsample(1, 2)
Button(root, image = photoimage).place(x = 450, y= 250)

leftimg = ImageTk.PhotoImage(pathtophotobleft)
panelbl = Label(root, image=leftimg, width=361, height=803, borderwidth = 0)
panelbl.image = leftimg
panelbl.place(x=-10, y=-1)
rightimg = ImageTk.PhotoImage(pathtophotobright)
panelbr = Label(root, image=rightimg, width=361, height=803, borderwidth=0)
panelbr.image = rightimg
panelbr.place(x=1080, y=-10)



def NewWindow():
    newWindow = Toplevel(root)

# sets the title of the
# Toplevel widget
    newWindow.title("Main Screen")

# sets the geometry of toplevel
    newWindow.geometry("1500x1000")
    newWindow.configure(bg = '#FFA500')
    Label(newWindow, text='Welcome to Help the Homies', bg = '#FFA500', font=(
    'Trajan Pro', 25, 'bold')).pack(side=TOP, pady=10)
# setting shelter image within the new window
    image1 = ImageTk.PhotoImage(pathtophoto1)
    panel1 = Label(newWindow, image=image1, width = 150, height = 150,  )
    panel1.image = image1  # keep a reference
    panel1.place(x=100, y=500)
# setting landscape image
    image2 = ImageTk.PhotoImage(pathtophoto2)
    panel2 = Label(newWindow, image = image2, width= 1500, height =300)
    panel2.image = image2
    panel2.place(x=-5, y = 150)
# setting food image
    image3 = ImageTk.PhotoImage(pathtophoto3)
    panel3 = Label(newWindow, image = image3, width = 150 , height =150)
    panel3.image = image3
    panel3.place(x= 500, y = 500)

# bottom text
    hotline_text = Label(newWindow, text = "Service Hotline: (800) 535-7252", bg ='#FFA500', font = ("Courier", 16))
    hotline_text.place(x= 570, y =750)

    # shelter_page = Button(newWindow,text = "Places to stay")
    # shelter_page.place(x=220, y = 650)
    food_page = Button(newWindow, text="Food Resources", font="Courier", command=Foodwindow)
    food_page.place(x=500, y=700)

    phone_page = Button(newWindow, text="Place a call", font="Courier", command=Phonewindow)
    phone_page.place(x=100, y=700)

    shelter_page = Button(newWindow, text="Shelters", font="Courier", command=Shelterwindow)
    shelter_page.place(x=900, y=700)

    resources_page = Button(newWindow, text="Looking for Additional Resources", font="Courier", command=Resourceswindow)
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
    myLabel3 = Label(Shelterwindow,
                     text='We do not directly provide aid ourselves, but provide local resources for you to find.')
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
    panel2.place(x=900, y=500)

    img = ImageTk.PhotoImage(pathtophoto11)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=1100, y=500)

    img = ImageTk.PhotoImage(pathtophoto12)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=1300, y=500)

    img = ImageTk.PhotoImage(pathtophoto13)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=100, y=100)

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
    panel2.place(x=1100, y=100)
    img = ImageTk.PhotoImage(pathtophoto19)
    panel2 = Label(Shelterwindow, image=img, width=150, height=150)
    panel2.image = img
    panel2.place(x=1300, y=100)



# What i added
def Phonewindow():
    Phonewindow = Toplevel(root)
    Phonewindow.title("Phone")
    Phonewindow.geometry("1500x1000")
    Phonewindow.configure(bg='#FFA500')
    Label(Phonewindow, text='Make a Call', bg='#FFA500', font=(
        'Courier', 25)).pack(side=TOP, pady=10)
    input_frame = Frame(Phonewindow, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                        highlightthickness=2, bg='#FFA500')

    input_frame.place(x = 250, y = 42 )
    input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=50, bg="#eee", bd=0,
                        justify=RIGHT)
    input_field.grid(row=0, column=0)
    input_field.pack(ipadx = 200, ipady=40)
# number buttons (non functional so they will be labels for now)
    one = Label(Phonewindow, text = "1", bg = '#FFA500', borderwidth = 3, font=('Courier',50), relief = 'raised',
                padx=70, pady=15)
    one.place(x = 300, y = 200)
    two = Label(Phonewindow, text="2", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                padx=70, pady=15)
    two.place(x=610, y=200)
    twoletters = Label(Phonewindow, text="ABC", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    twoletters.place(x=675, y=260)
    three = Label(Phonewindow, text="3", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                padx=70, pady=15)
    three.place(x=920, y=200)
    threeletters = Label(Phonewindow, text="DEF", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    threeletters.place(x=985, y=260)
    four = Label(Phonewindow, text="4", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                padx=70, pady=15)
    four.place(x=300, y=300)
    fourletters = Label(Phonewindow, text="GHI", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    fourletters.place(x=365, y=360)
    five = Label(Phonewindow, text="5", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                 padx=70, pady=15)
    five.place(x=610, y=300)
    fiveletters = Label(Phonewindow, text="JKL", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    fiveletters.place(x=675, y=360)
    six = Label(Phonewindow, text="6", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                 padx=70, pady=15)
    six.place(x=920, y=300)
    sixletters = Label(Phonewindow, text="MNO", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    sixletters.place(x=985, y=360)
    seven = Label(Phonewindow, text="7", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                padx=70, pady=15)
    seven.place(x=300, y=400)
    sevenletters = Label(Phonewindow, text="PQRS", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    sevenletters.place(x=360, y=460)
    eight = Label(Phonewindow, text="8", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                  padx=70, pady=15)
    eight.place(x=610, y=400)
    eightletters = Label(Phonewindow, text="TUV", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    eightletters.place(x=675, y=460)
    nine = Label(Phonewindow, text="9", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                  padx=70, pady=15)
    nine.place(x=920, y=400)
    nineletters = Label(Phonewindow, text="WXYZ", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    nineletters.place(x=980, y=460)
    star = Label(Phonewindow, text="*", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                  padx=70, pady=15)
    star.place(x=300, y=500)
    zero = Label(Phonewindow, text="0", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                 padx=70, pady=15)
    zero.place(x=610, y=500)
    plussign = Label(Phonewindow, text="+", bg='#FFA500', borderwidth=0, font=('Courier', 15), padx=10, pady=3)
    plussign.place(x=683, y=560)
    pound = Label(Phonewindow, text="#", bg='#FFA500', borderwidth=3, font=('Courier', 50), relief='raised',
                 padx=70, pady=15)
    pound.place(x=920, y=500)
    dial= Label(Phonewindow, text="Dial", bg='#8BCAD0', borderwidth=3, font=('Courier', 50), relief='sunken',
                 padx=90, pady=15)
    dial.place(x=550, y=650)


# what i added
def Foodwindow():
    Foodwindow = Toplevel(root)
    Foodwindow.title("Food")
    Foodwindow.geometry("1500x1000")
    Foodwindow.configure(bg='#FFA500')
    Label(Foodwindow, text='Food Pantries', bg='#FFA500', font=(
        'Iowan Old Style', 35, 'bold') , padx = 90, pady= 15).pack(side=TOP, pady=10)
    leftimg = ImageTk.PhotoImage(pathtophotobleft)
    panelbl = Label(Foodwindow, image=leftimg, width=361, height=803, borderwidth = 0)
    panelbl.image = leftimg
    panelbl.place(x=-10, y=-1)
    rightimg = ImageTk.PhotoImage(pathtophotobright)
    panelbr = Label(Foodwindow, image=rightimg, width=361, height=803, borderwidth=0)
    panelbr.image = rightimg
    panelbr.place(x=1080, y=-10)
# FIRST PANTRY
    first_pantry = Label(Foodwindow, text = "Thrive DC",bg='#FFA500', font=(
        'Iowan Old Style', 20, 'bold'),relief = 'raised', padx = 10, pady= 7)
    first_pantry.place(x = 80, y = 180)
    thrivedc = ImageTk.PhotoImage(pathtophotothrive)
    panelthrive = Label(Foodwindow, image=thrivedc, width=160, height=107, borderwidth=0)
    panelthrive.image = thrivedc
    panelthrive.place(x = 60, y =240)
    first_text = Label(Foodwindow, text= '1525 Newton Street NW\nWashington, DC - 20010\nPhone: 202-737-9311'
                                         '\n\nM-F: 8:30 A.M. - 11:00 P.M.', bg='#FFA500',
                       padx = 20, pady = 7, font=('Iowan Old Style', 12, 'bold'))
    first_text.place(x=35,y =350)
# SECOND PANTRY
    sec_pantry = Label(Foodwindow, text = "Washington City Church \nof the\nBrethren Nutrition Program",bg='#FFA500', font=(
        'Iowan Old Style', 15, 'bold'),relief = 'raised', padx = 10, pady= 7)
    sec_pantry.place(x = 280, y = 80)
    church = ImageTk.PhotoImage(pathtophotochurch)
    panelchurch = Label(Foodwindow, image= church, width=160, height=107, borderwidth=0)
    panelchurch.image = church
    panelchurch.place(x=310, y=175)
    sec_text= Label(Foodwindow, text= '337 North Carolina Avenue SE\nWashington, DC - 20003\nPhone: (202) 547-5924\n\n'
                                      'M-F: 12:00 P.M. - 1:30 P.M.', padx = 20, pady = 7,  bg='#FFA500'
                    ,font=('Iowan Old Style', 12, 'bold'))
    sec_text.place(x=280 , y = 285)
# THIRD PANTRY
    sec_pantry = Label(Foodwindow, text=" SOME (So Others Can Eat)", bg='#FFA500',
                       font=('Iowan Old Style', 17, 'bold'), relief='raised', padx=10, pady=7)
    sec_pantry.place(x=580, y=180)
    SOME = ImageTk.PhotoImage(pathtophotoSOME)
    panelS = Label(Foodwindow, image=SOME, width=170, height=114, borderwidth=0)
    panelS.image = SOME
    panelS.place(x=620, y=240)
    third_text = Label(Foodwindow,text = '710 Street NW\nWashington, DC - 20001\nPhone: (202) 797-8806'
                                         '\n\n Breakfast hours: 7:00 A.M. - 8:00 A.M.'
                                         '\n Lunch hours: 11:00 A.M. - 1:00 P.M.', bg='#FFA500'
                       ,font=('Iowan Old Style', 12, 'bold') )
    third_text.place(x=590, y = 360)
# FOURTH PANTRY
    fourth_pantry = Label(Foodwindow, text = "Feed The Family",bg='#FFA500', font=(
        'Iowan Old Style', 20, 'bold'),relief = 'raised', padx = 10, pady= 7)
    fourth_pantry.place(x = 920, y = 80)
    FTF = ImageTk.PhotoImage(pathtophotoFTF)
    panelFTF = Label(Foodwindow, image=FTF, width=160, height=160, borderwidth=0)
    panelFTF.image = FTF
    panelFTF.place(x=930, y = 140)
    fourth_text = Label(Foodwindow, text = '4225 Connecticut Avenue NW\nWashington, DC - 20008'
                                           '\nPhone: (202) 555-5555\n\nSun: 1:00 P.M. - 4:00 P.M.',  bg='#FFA500'
                        ,font=('Iowan Old Style', 12, 'bold'))
    fourth_text.place(x =915 , y = 310)
# FIFTH PANTRY
    fifth_pantry = Label(Foodwindow, text = 'Emory Beacon of Light', bg='#FFA500', font=(
        'Iowan Old Style', 18, 'bold'),relief = 'raised', padx = 10, pady= 7)
    fifth_pantry.place(x = 1160, y = 180)
    beacon = ImageTk.PhotoImage(pathtophotoBeacon)
    panelb = Label(Foodwindow, image= beacon, width=160, height=160, borderwidth=0)
    panelb.image = beacon
    panelb.place(x = 1190, y = 240)
    fifth_text = Label(Foodwindow, text = '6203 Piney Branch Road NW\nWashington, DC - 20011'
                                          '\nPhone: (202) 829-5732\n\n Tues: 12:00 P.M. - 2:00 P.M.',  bg='#FFA500'
                       ,font=('Iowan Old Style', 12, 'bold'))
    fifth_text.place(x = 1180, y = 410)
# SIXTH PANTRY
    six_pantry = Label(Foodwindow, text = 'Father Mc Kenna Center', bg='#FFA500',
                       font=('Iowan Old Style', 18, 'bold'),relief = 'raised', padx = 10, pady= 7)
    six_pantry.place(x=280, y =450)
    center = ImageTk.PhotoImage(pathtophotoCenter)
    panelc = Label(Foodwindow, image=center, width=160, height=107, borderwidth=0)
    panelc.image = center
    panelc.place(x=320, y=500)
    six_text= Label(Foodwindow, text ='19 I St NW\nWashington, DC - 20001\nPhone: (202) 842-1112'
                                      '\n\nM - F: 12:00 P.M. - UNTIL', bg='#FFA500',font=('Iowan Old Style', 12, 'bold'))
    six_text.place(x=320, y = 620)
# SEVENTH PANTRY
    sev_pantry = Label(Foodwindow, text = 'North Capitol Collaborative',bg='#FFA500',
                       font=('Iowan Old Style', 18, 'bold'),relief = 'raised', padx = 10, pady= 7)
    sev_pantry.place(x=880, y =450 )
    NCC = ImageTk.PhotoImage(pathtophotoNCC)
    paneln = Label(Foodwindow, image=NCC, width=160, height=107, borderwidth=0)
    paneln.image = NCC
    paneln.place(x=930, y = 500)
    sev_text = Label(Foodwindow, text= '2000 Rhode Island Avenue, NW\nWashington, DC - 20018'
                                       '\nPhone: (202) 588-1800\n\n 2nd and fourth Thursday out of the month\n'
                                       '10:00 A.M. - 2:00 P.M.',bg='#FFA500'
                       ,font=('Iowan Old Style', 12, 'bold'))
    sev_text.place(x= 880, y = 620)
# image
    dc = ImageTk.PhotoImage(pathtophotodc)
    paneld = Label(Foodwindow, image = dc, width=150, height=200, borderwidth=0 )
    paneld.image = dc
    paneld.place(x = 630, y = 500)

def Resourceswindow():
    Resourceswindow = Toplevel(root)
    Resourceswindow.title("Resources")
    Resourceswindow.geometry("1500x1000")
    Resourceswindow.configure(bg='#FFA500')
    Label(Resourceswindow, text='Looking for Additional Resources?', bg='#FFA500', font=(
        'Courier', 25)).pack(side=TOP, pady=10)


# a button widget which will open a
# new window on button click
main_page_btn = Button(root,text="Tap to Begin",command=NewWindow, font = ("courier",25))

main_page_btn.place(x=600, y= 600)


# allows program to continue looping
if __name__ == "__main__":
    root.mainloop()
