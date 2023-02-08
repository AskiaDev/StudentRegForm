import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



# function section
def dropdown_selected(event):
    print("Selected:", event.widget.get())

def toggle_checkbox(var, checkbox1, checkbox2):
    if var.get() == 1:
        checkbox2.deselect()

def validate_inputs():
    firstName = first_name_entry.get()
    lastName = last_name_entry.get()
    middleName = middle_name_entry.get()
    age = age_spinbox.get()
    course = courses.get()
    yearLevel = year_level.get()
    gender = sex_identity.get()
    units = units_spinbox.get()
    no_of_semester = semester.get()
    widgets = [firstName, lastName, middleName, age, course, yearLevel, gender, units, no_of_semester]

    empty_widgets = [widget for widget in widgets if not widget]

    if empty_widgets:
        messagebox.showwarning("Error", "Please complete the data")


def submit_data():
    firstName = first_name_entry.get()
    lastName = last_name_entry.get()
    middleName = middle_name_entry.get()
    age = age_spinbox.get()
    course = courses.get()
    yearLevel = year_level.get()
    gender = sex_identity.get()
    units = units_spinbox.get()
    no_of_semester = semester.get()


    print("First Name: ", firstName)
    print("Last Name: ", lastName)
    print("Middle Name: ", middleName)
    print("Age: ", age)
    print("----------------------------------")
    print("Course: ", course)
    print("Year Level: ", yearLevel)
    print("Gender: ", gender)
    print("Units: ", units)
    print("No. of Semester: ", no_of_semester)
    student_status()
    validate_inputs()
    validate_checkbox()
    agree_to_terms()




def student_status():
    if var1.get() == 1:
        print("Status: Regular Student")
    elif var2.get() == 1:
        print("Status: Irregular")
    else:
        print("No student status selected")

    
def validate_checkbox():
    if var1.get() == 0 and var2.get() == 0:
        messagebox.showerror("Error", "Please Choose Regular or Irregular")
    return

def agree_to_terms():
    if var3.get() == 0:
        messagebox.showerror("Error", "Please Agree to the Terms and Conditions")



# window section
window = tk.Tk()
window.title("Registration Form")


# frame section

frame = tk.Frame(window)
frame.pack()

# label section
user_info = tk.LabelFrame(frame, text='Student Information', font='Arial 10 bold')
user_info.grid(row=0, column=0, padx=20, pady=20)

# entry section
first_name = tk.Label(user_info, text='First Name: ', font='Arial 10 bold')
first_name.grid(row=0, column=0, pady=0)

last_name = tk.Label(user_info, text='Last Name: ', font='Arial 10 bold')
last_name.grid(row=0, column=1, pady=0)

middle_name = tk.Label(user_info, text='Middle Name: ', font='Arial 10 bold')
middle_name.grid(row=0, column=2)

first_name_entry = tk.Entry(user_info, width=25)
first_name_entry.grid(row=1, column=0,padx=10, pady=10)

last_name_entry = tk.Entry(user_info, width=25)
last_name_entry.grid(row=1, column=1, padx=10, pady=10)

middle_name_entry = tk.Entry(user_info, width=25)
middle_name_entry.grid(row=1, column=2, padx=10, pady=10)

# spinbox section

age = tk.Label(user_info, text='Age: ', font='Arial 10 bold')
age_spinbox = tk.Spinbox(user_info, from_=18, to=100, width=20)
age.grid(row=2, column=0, pady=0)
age_spinbox.grid(row=3, column=0)

# combobox section
courses = tk.Label(user_info, text='Course: ', font='Arial 10 bold')
courses.grid(row=2, column=1, pady=0)
courses = ttk.Combobox(user_info, values=["BSCPE", "BSIT", "BSCS", "BSCE", "BSA", "BSBA"])
courses.grid(row=3, column=1, padx=10, pady=10)
courses.grid(row=3, column=1)

year_level = tk.Label(user_info, text='Year Level: ', font='Arial 10 bold')
year_level.grid(row=2, column=2, pady=0)
year_level = ttk.Combobox(user_info, values=["1st Year", "2nd Year", "3rd Year", "4th Year", "5th Year", "Masteral"])
year_level.grid(row=3, column=2, padx=10, pady=10)
year_level.grid(row=3, column=2)

sex_identity = tk.Label(user_info, text='Gender:', font='Arial 10 bold')
sex_identity.grid(row=4, column=0, pady=0)
sex_identity = ttk.Combobox(user_info, values=["Male", "Female", "Transgender", "Non-Binary"])
sex_identity.grid(row=5, column=0, padx=10, pady=10)

# 2nd frame section

frame2 = tk.LabelFrame(frame)
frame2.grid(row=1, column=0, sticky='news', padx=20, pady=15)

student_label = tk.Label(frame2, text='Student Status', font='Arial 10 bold', padx=10, pady=5)
student_label.grid(row=0, column=0, pady=0)

var1 = tk.IntVar()
var2 = tk.IntVar()

student_check1 = tk.Checkbutton(frame2, text='Regular', variable=var1,  command=lambda: toggle_checkbox(var1, student_check1, student_check2))
student_check1.grid(row=1, column=0, padx=10)


student_check2 = tk.Checkbutton(frame2, text='Irregular', variable=var2,command=lambda: toggle_checkbox(var2, student_check2, student_check1))
student_check2.grid(row=2, column=0, padx=10)


units_label = tk.Label(frame2, text='No. of Units', font='Arial 10 bold', padx=10, pady=5)
units_spinbox = tk.Spinbox(frame2, from_=0, to=40, width=20)
units_label.grid(row=0, column=1, padx=10, pady=0)
units_spinbox.grid(row=1, column=1, padx=10, pady=10)


semester_label = tk.Label(frame2, text='Semester', font='Arial 10 bold', padx=10, pady=5)
semester_label.grid(row=0, column=2, padx=10, pady=0)
semester = ttk.Combobox(frame2, values=["1", "2", "3"])
semester.grid(row=1, column=2, padx=10, pady=10)

# 3rd frame section

frame3 = tk.LabelFrame(frame, text='Terms & Conditions', font='Arial 10 bold')
frame3.grid(row=2, column=0, sticky='news', padx=20, pady=15)

var3 = tk.IntVar()

terms_check = tk.Checkbutton(frame3, text='I agree to the terms and conditions', variable=var3)
terms_check.grid(row=0, column=0, padx=10, pady=10,)


button = tk.Button(frame, text='Submit', font='Arial 10 bold', command=submit_data) 
button.grid(row=3, column=0, sticky='news', padx=20, pady=15)




window.mainloop()

