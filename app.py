from tkinter import *

import database
from database import *
import tkinter.font as TkFont
from tkinter.filedialog import *

# create database
create_database()

# establish main window for UI
root = Tk()
root.geometry('530x700+530+700')
medium_font = TkFont.Font(size=20)
root.title('Ecryption Questioner')

Label(root, text="Encryption Questioner:", font=("Ariel", 35)).pack(side=TOP)
Label(root, text="My Files:", font=("Ariel", 25)).place(x=5, y=45)

# listbox will be the list of files on the left side
listbox = Listbox(root, height=26, width=12, font=medium_font, selectmode=SINGLE)

# Fill side menu with names of stored files
myFiles = get_all_filenames()

# list all stored files in listbox
for i, file in enumerate(myFiles):
    listbox.insert(i, file)

# customize listbox for storing links to files
listbox.place(x=0, y=85)
text = Text(root, height=40, width=45, bg='#D3D3D3')
scroll = Scrollbar(root)
text.configure(yscrollcommand=scroll.set)
text.place(x=180, y=85)
scroll.config(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
if listbox.size() != 0:
    listbox.selection_set(first=0)
file_path = None


# Rerenders the screen
def update_screen():
    # Fill side menu with names of stored files.
    myFiles = get_all_filenames()

    listbox.delete(0, 'end')

    for i, file in enumerate(myFiles):
        listbox.insert(i, file)

    listbox.selection_set(first=listbox.size()-1)
    selection = listbox.get(listbox.curselection())[0]
    if selection:
        insert_text = get_text_from_file_by_name(selection)
    else:
        insert_text = ""

    listbox.place(x=0, y=85)
    text.delete("1.0", "end")
    text.insert(END, insert_text)


# deletes the file from the database and the listbox.
def file_removal():
    filename = listbox.get(listbox.curselection())[0]
    database.delete_file(filename, True)
    update_screen()


# Logic for determining if question prompt is answered correctly or if file has been uploaded. 
def check_and_upload(question, answer, error1, uploadWindow):
    question = question.get('1.0', END).strip()
    answer = answer.get('1.0', END).strip()

    if file_path is None:
        error1.config(text="No file selected")
        return
    if len(question) == 1:
        error1.config(text="No question inputted")
        return
    if len(answer) == 1:
        error1.config(text="No answer inputted")
        return
    upload_file_to_db(file_path, question, answer)
    uploadWindow.destroy()
    update_screen()


def check_and_encrypt(file_data, answer, error1, encryptWindow):
    if file_data[3] == 1:
        error1.config(text="Error: File is already encrypted")
    answer = answer.get('1.0', END).strip()
    if file_data[2] != answer:
        error1.config(text="Error: Incorrect Answer")
        return
    database.update_file(file_data)
    encryptWindow.destroy()
    update_screen()


def check_and_decrypt(file_data, answer, error1, decryptWindow):
    if file_data[3] == 0:
        error1.config(text="Error: File is already decrypted")
    answer = answer.get('1.0', END).strip()
    if file_data[2].strip() != answer:
        error1.config(text="Error: Incorrect Answer")
        return
    database.update_file(file_data)
    decryptWindow.destroy()
    update_screen()


def open_file():
    global file_path
    file_path = askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
    if file_path is not None:
        pass

# handles file link being clicked inside of the listbox
def onSelect(event):
    selection = listbox.get(listbox.curselection())[0]
    if selection:
        insert_text = get_text_from_file_by_name(selection)
    else:
        insert_text = ""
    text.delete("1.0", "end")
    text.insert(END, insert_text)

def openEncryptWindow():
    encryptWindow = Toplevel(root)
    encryptWindow.title("Encrypt File")
    encryptWindow.geometry("300x300")
    encryptWindow.transient(root)
    Label(encryptWindow, text="Encrypt File:", font=("Ariel", 20)).pack(side=TOP)

    # Get selected file
    selection = listbox.get(listbox.curselection())[0]
    file_data = get_file_question_answer(selection)

    Label(encryptWindow, text="Question:", font=("Ariel", 15)).place(x=5, y=40)
    Label(encryptWindow, text="Answer:", font=("Ariel", 15)).place(x=5, y=110)
    text1 = Text(encryptWindow, height=3, width=25, bd=1, bg='#D3D3D3')
    text2 = Text(encryptWindow, height=3, width=25, bd=1, bg='#D3D3D3')
    text1.delete("1.0", "end")
    text1.insert(END, file_data[1])
    error1 = Label(encryptWindow, text="", font=("Ariel", 15), fg='red', bg='white')

    encryptButton2 = Button(
        encryptWindow,
        text="Encrypt/Decrypt",
        highlightbackground='#3E4149',
        pady=4,
        command=lambda:check_and_encrypt(file_data, text2, error1, encryptWindow)
    )

    encryptButton2.pack(side=BOTTOM)
    text1.place(x=105, y=40)
    text2.place(x=105, y=110)
    error1.place(x=20, y=220)


def openDecryptWindow():
    decryptWindow = Toplevel(root)
    decryptWindow.title("Decrypt File")
    decryptWindow.geometry("300x300")
    decryptWindow.transient(root)
    Label(decryptWindow, text="Decrypt File:", font=("Ariel", 20)).pack(side=TOP)

    # Get selected file
    selection = listbox.get(listbox.curselection())[0]
    file_data = get_file_question_answer(selection)

    Label(decryptWindow, text="Question:", font=("Ariel", 15)).place(x=5, y=40)
    Label(decryptWindow, text="Answer:", font=("Ariel", 15)).place(x=5, y=110)
    text1 = Text(decryptWindow, height=3, width=25, bd=1, bg='#D3D3D3')
    text2 = Text(decryptWindow, height=3, width=25, bd=1, bg='#D3D3D3')
    text1.delete("1.0", "end")
    text1.insert(END, file_data[1])
    error1 = Label(decryptWindow, text="", font=("Ariel", 15), fg='red', bg='white')

    decryptButton2 = Button(
        decryptWindow,
        text="Decrypt",
        highlightbackground='#3E4149',
        pady=4,
        command=lambda:check_and_decrypt(file_data, text2, error1, decryptWindow)
    )

    decryptButton2.pack(side=BOTTOM)
    text1.place(x=105, y=40)
    text2.place(x=105, y=110)
    error1.place(x=20, y=220)

def openUploadWindow():
    uploadWindow = Toplevel(root)
    uploadWindow.title("Upload File")
    uploadWindow.geometry("300x300")
    uploadWindow.transient(root)
    Label(uploadWindow, text="Upload File:", font=("Ariel", 20)).pack(side=TOP)
    msbtn = Button(
        uploadWindow,
        text='Choose File',
        command=lambda:open_file(),
        highlightbackground='#3E4149'
    )

    msbtn.place(x=5, y=190)

    Label(uploadWindow, text="Question:", font=("Ariel", 15)).place(x=5, y=40)
    Label(uploadWindow, text="Answer:", font=("Ariel", 15)).place(x=5, y=110)
    text1 = Text(uploadWindow, height=3, width=20, bd=1, bg='#D3D3D3')
    text2 = Text(uploadWindow, height=3, width=20, bd=1, bg='#D3D3D3')
    error1 = Label(uploadWindow, text="", font=("Ariel", 15), fg='red', bg='white')

    uploadButton2 = Button(
        uploadWindow,
        text="Upload",
        highlightbackground='#3E4149',
        pady=4,
        command=lambda:check_and_upload(text1, text2, error1, uploadWindow)
    )

    uploadButton2.pack(side=BOTTOM)

    text1.place(x=140, y=40)
    text2.place(x=140, y=110)
    error1.place(x=20, y=220)

listbox.bind("<<ListboxSelect>>", onSelect)

upload1 = Button(root, text="Upload", highlightbackground='#3E4149', command=openUploadWindow)
encrypt1 = Button(root, text="Encrypt/Decrypt", highlightbackground='#3E4149', command=openEncryptWindow)
delete1 = Button(root, text="Delete", highlightbackground='#3E4149', command=file_removal)
upload1.place(x=150, y=655)
encrypt1.place(x=275, y=655)
delete1.place(x=450, y=655)

root.mainloop()
