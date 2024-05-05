# application to display data to user

from tkinter import *

# class for each new page
class Page:
    # constructor
    def __init__(self, dataFile: str, name: str | None = 'New Room') -> None:
        # .py file containing appropriate data
        self.dataFile = dataFile
        # name of the room
        self.name = name

# class for main GUI
class GUI(Frame):
    # constructor
    def __init__(self, parent) -> None:
        Frame.__init__(self, master=parent)

        self.pages = []

        # organize the GUI
        self.pack(expand=1, fill=BOTH)

    # init GUI
    def showWelcomePage(self):
        # delete all displayed widgets
        self.clearFrame()
        
        # display welcome message
        GUI.welcomeLabel = Label(self, font=("TkDefaultFont", 15), text="Welcome to Room Traffic Tracker!")
        GUI.welcomeLabel.pack(fill=X, pady=50)

        # make button for user to make a room
        GUI.addRoomBtn = Button(self, bg='white', command=lambda: self.addNewPage(), text="Add Room", width=20)
        # push to bottom of the window
        GUI.addRoomBtn.pack(side=BOTTOM, pady=50)

        # display buttons for each room page from last to first
        for page in reversed(self.pages):
            pageBtn = Button(self, bg='white', command=lambda: self.showPage(page), text=page.name, width=50)
            pageBtn.pack(side=BOTTOM)

    # allow user to make new room page
    def addNewPage(self):
        # delete all displayed widgets
        self.clearFrame()

        # setup user input at the bottom of the GUI
        # prompts user to set name of the room and associated data file
        GUI.roomName = Entry(self, bg='white', width=50)
        GUI.roomData = Entry(self, bg='white', width=50)
        # labels for each entry
        GUI.roomNameLabel = Label(self, text="Room name:")
        GUI.roomDataLabel = Label(self, text="Data file (.py):")

        # user can submit by clicking submit button
        GUI.submitBtn = Button(self, bg='white', command=lambda: self.createPage()  # checks if text entries are empty first
                               if self.roomName.get() != '' and self.roomData.get() != '' else None,
                               text='Submit', width=20)
        # or cancel by clicking cancel button
        GUI.cancelBtn = Button(self, bg='white', command=lambda: self.showWelcomePage(), text='Cancel', width=20)

        # used for spacing in grid manager
        GUI.spacer1 = Label(self, text="")
        GUI.spacer2 = Label(self, text="")

        # add entries to grid manager
        GUI.roomNameLabel.grid(row=0, column=1, sticky=N+E+S+W)
        GUI.roomName.grid(row=1, column=0, columnspan=3, sticky=N+E+S+W)
        GUI.roomDataLabel.grid(row=2, column=1, sticky=N+E+S+W)
        GUI.roomData.grid(row=3, column=0, columnspan=3, sticky=N+E+S+W)
        GUI.spacer1.grid(row=4, column=0, sticky=N+E+S+W)
        
        # add buttons to grid manager
        GUI.submitBtn.grid(row=5, column=1, sticky=N+E+S+W)
        GUI.cancelBtn.grid(row=6, column=1, sticky=N+E+S+W)
        GUI.spacer2.grid(row=7, column=0, sticky=N+E+S+W, pady=15)

        # put grid on bottom of window
        self.grid_anchor(S)

    # create new room page
    def createPage(self):
        # create new Page instance
        newPage = Page(name=GUI.roomName.get(), dataFile=GUI.roomData.get())
        self.pages.append(newPage)

        # go back to welcome page
        # a button for the new room page will be displayed
        self.showWelcomePage()

    # show page
    def showPage(self, page: Page):
        # delete all displayed widgets
        self.clearFrame()

        # make labels for name of room page
        GUI.nameLabel = Label(self, font=("TkDefaultFont", 15), text=f"Average Daily {page.name} Traffic")
        # and data associated with room page
        GUI.dataLabel = Label(self, text="Data placeholder")    ######DATA FROM FILE(may need different widget)######

        # display labels
        GUI.nameLabel.pack(fill=X, pady=50)
        GUI.dataLabel.pack(anchor=W, padx=50, pady=50)

        # make button to go back to welcome page
        GUI.backButton = Button(self, bg='white', command=lambda: self.showWelcomePage(), text='Back', width=20)
        # and display it
        GUI.backButton.pack(side=BOTTOM, pady=50)

    # delete all displayed widgets
    def clearFrame(self):
        for widget in self.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    # the default size of the GUI is 800x600
    WIDTH = 800
    HEIGHT = 600

    # create the window
    window = Tk()
    window.title("Room Traffic Tracker")
    window.geometry(f"{WIDTH}x{HEIGHT}")

    # create the GUI as a Tkinter canvas inside the window
    g = GUI(window)

    # start application on welcome page
    g.showWelcomePage()

    # wait for the window to close
    window.mainloop()