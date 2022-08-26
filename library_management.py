from tkinter import *
import tkinter.messagebox as tmsg
import datetime as dt
import os

window=Tk()
window.wm_iconbitmap('lib.ico')
window.title("LIBRARY MANAGEMENT")
def Show_Books():
    if books==[]:
        text.delete(1.0, END)
        text.insert(END,'There are no books available')
        tmsg.showinfo("Details","There is no books in Library Yet")
        
    else:
        text.delete(1.0, END)
        text.insert(END,'The books are-:')
        for book in books:
            text.insert(END, book + ' , ')
def cleararea():
    text.delete(1.0,END)

def Add_books():
    global books
    # addbook=input("Add Book-:")
    
    book=add_book_value.get()
    addbooks=book.title()
    if add_book_value.get()=='':
            tmsg.showinfo('Details','Kindly Enter Valid Book Name :)')
            return
        
    elif addbooks in books:
        tmsg.showinfo('Details',f"{add_book_value.get()} is already with us ,kindly add another book :)")
        return
    else:
        
        tmsg.showinfo('Details',f'{add_book_value.get()} Book Has been Added.')
        with open('Total_books.txt','a') as f:
            f.write(f"At {dt.datetime.now()} {add_book_value.get()} Book has been ADDED .")
            f.write('\n')
        books.append(addbooks)
        
        return f" {addbooks} Book Added. Thank for donating :) "

def lend_bookss():
    global books
    global dicts
    names=lend_book_name_person_value.get()
    name=names.title()
    book_name=lend_book_name_value.get()
    book_names=book_name.title()
    if book_names =='':
        tmsg.showinfo("Details","Kindly Enter Something :)")
        return
    if book_names not in books :
        tmsg.showinfo('details',"This Book is Not Available , Kindly choose Some another Book :)")
        return
    if book_names in dicts:
        tmsg.showerror("Cannot Lend",f"Sorry {name} , {book_names} is already been lended . Kindly try after some Days.")
        return 
    else:
        tmsg.showinfo('lending details',f"{book_names} book is now lended to {name}.")
        dicts[book_names]=name

        with open('Lended_books_Details.txt','a') as f:
            f.write(f"At {dt.datetime.now()} {book_names} Book has been lended to {name} .")
            f.write('\n')

def return_bookss():
    global books
    global dicts
    a=return_book_value.get()
    aa=a.title()
    if aa=='':
        tmsg.showinfo("details","Kindly Enter Something :)")
        return
    if dicts=={} :
        tmsg.showinfo("details","NO Book Has Been Lended Yet:)")
        return
    if aa not in dicts :
        tmsg.showinfo("details","This Book is Not Been Lended :)")
        
    else:

        if aa in dicts:
            tmsg.showinfo('Return Details',f'{aa} Book has been returned by {dicts[aa]}')
            with open(f'Return_books_Details.txt','a') as f:
                f.write(f"At {dt.datetime.now()} {aa} Book has been returned by {dicts[aa]} .")
                f.write('\n')
            
            dicts.pop(aa)
        
def show_lended_bookss():
    global dicts
    if dicts =={}:
        tmsg.showinfo("Details","NO BOOK has been Lended Yet :)")
    else:
        for i in dicts:
            text.delete(1.0, END)
        text.insert(END,'')
        for book in dicts:
            text.insert(END, f'{book} book is lended to {dicts[book]}' + ' , ')

def deletefiles():
            if os.path.exists("Lended_books_Details.txt"):
                os.remove(f'Total_books.txt')
                os.remove(f"Lended_books_Details.txt")
                os.remove(f'Return_books_Details.txt')
                text.insert(END,"Files Deleted")
            else:
                text.delete(1.0, END)
                text.insert(END,"Files Does not exist or has been already deleted.")
                tmsg.showerror('Error',"File Does Not Exist .")


# Set the geometry
window.geometry("1000x500")
Label(text="Welcome to RVC Library",font="algerian 30 bold",fg='grey').grid(row=0,column=2)
# Add the list of items
books= []
dicts={}



add_book=Label(text="ADD BOOK").grid(row=1,column=2)
lend_book=Label(text="LEND BOOK  (Book Name ,Name)").grid(row=2,column=2)
return_book=Label(text="RETURN LENDED BOOK").grid(row=3,column=2)
# show_lended_book=Label(text="SHOW LENDED BOOKS").grid(row=4,column=2)
# show_book=Label(text="SHOW TOTAL BOOKS").grid(row=5,column=2)
##tkinter vairable for storing entries
window.maxsize(1000,500)
window.minsize(1000,500)
add_book_value=StringVar()
lend_book_name_value=StringVar()
lend_book_name_person_value=StringVar()
return_book_value=StringVar()
show_lended_book_value=StringVar()
show_book_value=StringVar()
# foodservicevalue=StringVar()
#enrties for our form
add_book_entry=Entry(window,textvariable=add_book_value)
lend_book_name_entry=Entry(window,textvariable=lend_book_name_value)
lend_book_name_person_entry=Entry(window,textvariable=lend_book_name_person_value)

return_book_entry=Entry(window,textvariable=return_book_value)
show_lended_book_entry=Entry(window,textvariable=show_lended_book_value)
show_book_entry=Entry(window,textvariable=show_book_value)

#packing our entries
add_book_entry.grid(row=1,column=3)
lend_book_name_entry.grid(row=2,column=3)
lend_book_name_person_entry.grid(row=2,column=4)

return_book_entry.grid(row=3,column=3)
# show_lended_book_entry.grid(row=4,column=3)
# show_book_entry.grid(row=5,column=3)

Button(text="ADD THIS BOOK",command=Add_books).grid(row=1,column=4,padx=11,pady=5)
Button(text="LEND",command=lend_bookss).grid(row=2,column=5,padx=11,pady=5)
Button(text="RETURN THIS BOOK",command=return_bookss).grid(row=3,column=4,padx=11,pady=5)
Button(text="SHOW LENDED BOOK",command=show_lended_bookss).grid(row=4,column=4,padx=11,pady=5)
Button(text="SHOW TOTAL BOOKS",command=Show_Books).grid(row=5,column=4,padx=11,pady=5)
Button(text="CLEAR",command=cleararea).grid(row=6,column=4,padx=11,pady=5)
Button(text="DELETE DETAILS",command=deletefiles).grid(row=7,column=4,padx=11,pady=5)

Button(text="Exit",command=quit).grid(row=8,column=4,padx=11,pady=5)

text=Text(window, width=80, height=10)
text.grid(row=8,column=2)
# Scroll = Scrollbar(text)


# Scroll.config(command=text.yview)
# text.config(yscrollcommand=Scroll.set)
# Scroll.pack()
window.mainloop()
