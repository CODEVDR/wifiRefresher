import time
from tkinter import *
from selenium import webdriver


class App(Tk):
    def __init__(self):
        self.root = Tk()

        self.fontHead = ("Cascadia Code", 30, "bold")
        self.fontBody = ("Cascadia Code", 15, "bold")

        self.root.geometry("500x300")
        self.root.title("PageRefresher By CodeWithVdr")
        self.root.minsize(500, 300)
        self.root.maxsize(500, 300)
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass

        self.head = Label(
            self.root, text="WIFI REFRESHER", font=self.fontHead, relief=SOLID
        )
        self.head.pack()

        self.frameBody = Frame(self.root)
        self.URL = StringVar()
        Label(self.frameBody, font=self.fontBody, text="Enter URL : ").pack(
            anchor=W, pady=5
        )
        Entry(
            self.frameBody,
            font=self.fontBody,
            relief=SOLID,
            textvariable=self.URL,
            width=40,
        ).pack()
        Button(
            self.frameBody,
            font=self.fontBody,
            text="Submit",
            relief=SOLID,
            cursor="hand2",
            command=self.pageRefresher,
        ).pack(pady=10, anchor=E)
        self.status = Label(self.frameBody, font=self.fontBody, fg="green")
        self.status.pack(anchor=W, pady=2)
        self.frameBody.pack(pady=35)

        self.root.mainloop()

    def pageRefresher(self):
        self.browser = webdriver.Edge()
        brk = 0
        while True:
            print("Refreshing...")
            self.root.update()
            try:
                self.status["fg"] = f"green"
                self.browser.get(self.URL.get())  # Getting The URL
                for i in range(30):
                    self.root.update()
                    if i != 0:
                        time.sleep(1)  # Waiting For 1 Seconds
                        self.status["text"] = f"Status : Refreshing in {30-i}"
                        self.root.update()
                self.browser.refresh()  # Function For Refreshing Page
            except:
                for i in range(30):
                    self.root.update()
                    if i != 0:
                        time.sleep(1)  # Waiting For 1 Seconds
                        self.status["text"] = f"Status : Error Wifi Disconnected"
                        self.status["fg"] = f"red"
                        self.root.update()
                brk += 1
                if brk > 3:
                    self.status["text"] = f"Please Restart App"
                    self.status["fg"] = f"red"
                    break
            self.root.update()


if __name__ == "__main__":
    App()
