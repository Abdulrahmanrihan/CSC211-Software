import tkinter
import time
from databases import books
from tkinter import messagebox

def home_page():
    root = tkinter.Tk()

    root.geometry("500x400")
    root.title("Home Page")

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(6, weight=1)

    tkinter.Label(root, text="Search here for the category of the reference you need").grid(row=1, column=1, columnspan=2, ipadx=10, ipady=10)
    tkinter.Label(root, text="Here are the available categories").grid(row=2, column=1, columnspan=2, ipadx=10, ipady=10)
    tkinter.Label(root, text=[category + ',' for category in books.keys()], wraplength=350).grid(row=3, column=1, columnspan=2, ipady=10)
    search_entry = tkinter.Entry(root)
    search_entry.grid(row=4, column=1, columnspan=2)

    def search_book(root):
        search_page = tkinter.Toplevel(root)
        category = search_entry.get()

        search_page.geometry("500x400")
        search_page.grid_rowconfigure(0, weight=1)
        search_page.grid_rowconfigure(7, weight=1)
        search_page.grid_columnconfigure(0, weight=1)
        search_page.grid_columnconfigure(7, weight=1)

        search_page.title(category)

        tkinter.Label(search_page, text="These are the available books of this category").grid(row=1, column=1, columnspan=2)

        def payment(prev, book_name):
            payment = tkinter.Toplevel(prev)

            payment.title(book_name)
            
            payment.geometry("500x400")
            payment.grid_rowconfigure(0, weight=1)
            payment.grid_rowconfigure(7, weight=1)
            payment.grid_columnconfigure(0, weight=1)
            payment.grid_columnconfigure(7, weight=1)
            
            tkinter.Label(payment, text=book_name).grid(row=1, column=1, columnspan=2)
            card_name = tkinter.Label(payment, text="Name on card").grid(row=2, column=1, sticky="W", ipadx=10, ipady=10)
            card_name_entry = tkinter.Entry(payment)
            card_name_entry.grid(row=2, column=2)

            card_number = tkinter.Label(payment, text="Card number").grid(row=3, column=1, sticky="W", ipadx=10, ipady=10)
            card_number_entry = tkinter.Entry(payment)
            card_number_entry.grid(row=3, column=2)

            tkinter.Button(payment, text="Pay now", command=lambda:messagebox.showinfo("Success!", "Payment Succeeded")).grid(row=4, column=1, columnspan=2)

            payment.mainloop()

        if (category in books):
            row = 2
            column = 1
            for book in books[category]:
                tkinter.Button(search_page, text = book, command=lambda:payment(search_page, book)).grid(row = row, column = column, ipady=10, ipadx=10, sticky="W")
                column+=1
                if(column == 3):
                    column = 1
                    row +=1

            search_page.mainloop()
    
    
    search_button = tkinter.Button(root, text="Search", command=lambda: search_book(root)).grid(row=5, column=1, columnspan=2)
    root.mainloop()
