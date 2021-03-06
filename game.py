from tkinter import *
from PIL import Image, ImageTk

def rgbToColour(rgb):			# allows any colour variation to become rgb colour
    return "#%02x%02x%02x" % rgb

def ChoosePlayer():
    playButton.destroy()		# removes the button "play"
    global computerButton, playerButton
    computerButton=Button(root, text = "Against Computer", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[setVs('Computer'), Theme()])# creates a button named "Against Computer"
    computerButton.place(x=660, y=500, height = 100, width =600)			# places the button in a certain position
    playerButton = Button(root, text = "Against Player", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[setVs('Player'), Theme()])	# creates a button named "Against Player"
    playerButton.place(x=660, y=300, height = 100, width =600)				# places the button in a certain position												

def setVs(vsChoice):
    global vs
    vs = vsChoice
    ##print (vs)


def Theme():
    computerButton.destroy()    #removes the previous buttons
    playerButton.destroy()
    global title1, jungleButton, desertButton, volcanicButton    #allows the variables to be used in other functions
    title1 = Label(root, text = "Themes:",  font = ("Calibri", 48)) #creates title
    title1.place(x=810, y=75, height = 100, width = 300)            #places title
    volcanicButton = Button(root, text = "Volcanic", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                            activebackground = rgbToColour((41, 236, 242)), command = lambda:[setTheme('Volcanic'), ColourCounter()]) #creates button for volcanic
    volcanicButton.place(x=735, y=250, height = 100, width =450)                                                                      #places button volcanic                                          
    jungleButton = Button(root, text = "Jungle", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),          
                            activebackground = rgbToColour((41, 236, 242)), command = lambda:[setTheme('Jungle'), ColourCounter()]) #creates button for jungle
    jungleButton.place(x=735, y=400, height = 100, width =450)                                                                      #places button jungle
    desertButton = Button(root, text = "Desert", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                            activebackground = rgbToColour((41, 236, 242)), command = lambda:[setTheme('Desert'), ColourCounter()]) #creates button for desert
    desertButton.place(x=735, y=550, height = 100, width =450)                                                                      #places button desert

def setTheme(themeChoice):
    global theme
    theme = themeChoice 
    ##print(theme)

 # def ColourCounter():  
 #     volcanicButton.destroy()
 #     jungleButton.destroy()      #removes previous buttons
 #     desertButton.destroy()
 #     title1.destroy()
 #     redButton = Button                                          #red
 #     redButton.place(x=, y=, height=, width=)
#     blueButton = Button                                         #blue
 #     blueButton.place(x=, y=, height=, width=)
 #     greenButton = Button                                        #green
 #     greenButton.place(x=, y=, height=, width=)
 #     yellowButton = Button                                       #yellow
 #     yellowButton.place(x=, y=, height=, width=)
 #     purpleButton = Button                                       #purple
 #     purpleButton.place(x=, y=, height=, width=)
 #     blackButton = Button                                        #black
 #     blackButton.place(x=, y=, height=, width=)
    
    



#def setColour(colourChoice)
  #  global colour
  #  colour = colourChoice
  #  ##print(colour)




root = Tk()
root.geometry('1920x1080') 	# creates a window 
root.configure(background="black")

#filename = PhotoImage(file = ".\\background.png")
#background_label = Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open(".\\background.png")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

e = Example(root)
e.pack(fill=BOTH, expand=YES)

playButton = Button(root, text = "Play", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                    activebackground = rgbToColour((41, 236, 242)), command = ChoosePlayer) # creates a button called play that begins the game
playButton.place(x=810, y=300, height = 100, width = 300)	# placement of the button


root.mainloop()
