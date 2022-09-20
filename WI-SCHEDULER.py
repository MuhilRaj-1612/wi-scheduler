# Project WI (WhatsApp (or) Instagram Scheduler)
try:
    # Time module is used for scheduling
    import time
    # OS module is used for inputting commands
    import os
    # pyautogui is used for Automation
    import pyautogui
    # Selenium is used for web automation
    from selenium import webdriver
    # Datetime is used for advanced timer
    from datetime import datetime, timedelta
    # tkinter is used for GUI (Graphical User Interface)
    from tkinter import *
    # tkinter message is used to show Information, Error, Warnings, ETC..
    from tkinter import messagebox
    # Python Imaging library is used for ICON, LOGO, ETC...
    from PIL import Image, ImageTk
    # Win10toast module is used for windows notification after automation is done
    import win10toast
    # Request module is used for requesting web links
    import requests
# Try or Exception is used to check and clean the module not found errors
except ModuleNotFoundError:
    # Message box
    messagebox.showerror('Error', "You don't have python installed. Click OK to install it")
    # OS
    os.system('start PYTHON-WI-SCHEDULER.exe')


# Whatsapp Scheduler


def whatsapp():
    try:
        # Destroying First window
        start_window.destroy()
        # creating Whatsapp main window
        win_1 = Tk()
        # Focusing it
        win_1.focus_force()
        # Background Image
        bg = PhotoImage(file="requests//back_wh.png")
        # Label
        Label(image=bg, width=1000, height=500).place(x=-3, y=0)
        # Title
        win_1.title('WhatsApp Automation')
        # Width
        window_width = 1000
        # height
        window_height = 500
        # screen width
        screen_width = win_1.winfo_screenwidth()
        # screen height
        screen_height = win_1.winfo_screenheight()
        # coordinate x
        center_x = int(screen_width / 2 - window_width / 2)
        # coordinate y
        center_y = int(screen_height / 2 - window_height / 2)
        # window geometry
        win_1.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        # resize = False
        win_1.resizable(False, False)
        # creating canvas
        canvas = Canvas(win_1, bg='ghost white', height=450, width=700, highlightbackground="black")
        # placing it
        canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        canvas_2 = Canvas(win_1, bg='black', height=50, width=700, highlightbackground="black")
        canvas_2.place(x=500, y=50, anchor=CENTER)
        # Creating label
        l_head = Label(text='WHATSAPP AUTOMATION', bg='black', fg='springgreen1', font=('Arial', 25, 'bold'))
        l_head.place(x=500, y=50, anchor=CENTER)
        l_1 = Label(text='Hour: ', bg='ghost white', fg='black', font=('Apple LiSung', 16, 'bold'))
        l_1.place(x=298, y=120, anchor=CENTER)
        l_2 = Label(text='Minutes: ', bg='ghost white', fg='black', font=('Apple LiSung', 15, 'bold'))
        l_2.place(x=284, y=180, anchor=CENTER)
        l_3 = Label(text='AM or PM: ', bg='ghost white', fg='black', font=('Apple LiSung', 14, 'bold'))
        l_3.place(x=278, y=240, anchor=CENTER)
        # Creating labels
        e_1 = Entry(bg="black", fg='springgreen1', insertbackground='ghost white', font=('Arial', 15))
        e_1.place(x=453, y=120, anchor=CENTER, width=250, height=34)

        def e1_focus(focus1):
            # focusing 1st entry
            e_1.focus_set()

        e_2 = Entry(bg="black", fg='springgreen1', insertbackground='ghost white', font=('Arial', 15))
        e_2.place(x=453, y=180, anchor=CENTER, width=250, height=34)

        def e2_focus(focus2):
            # focusing second entry
            e_2.focus_set()

        e_3 = Entry(bg="black", fg='springgreen1', insertbackground='ghost white', font=('Arial', 15))
        e_3.place(x=453, y=240, anchor=CENTER, width=250, height=34)

        def e3_focus(focus3):
            # focusing third entry
            e_3.focus_set()

        # Binding keyboard key with entry
        e_1.bind("<Down>", e2_focus)
        e_2.bind("<Down>", e3_focus)
        e_2.bind("<Up>", e1_focus)
        e_3.bind("<Up>", e2_focus)

        def check(event):
            # Getting the input from the entry in which user gave some input
            a = e_1.get()
            b = e_2.get()
            amorpm_whatsapp = e_3.get()
            # opens and write a file "Time.txt"
            file_time = open('requests//Time.txt', 'w')
            # Concatenating everything
            file_time.write((str(a) + ':' + str(b) + ':' + str('00') + ' ' + str(amorpm_whatsapp).upper()))
            file_time.close()

            if len(a) != 2:
                chk1 = str(0) + str(e_1.get())
                # Removes the file "Time.txt"
                os.remove('requests//Time.txt')
                chk_read_time = open('requests//Time.txt', 'w')
                chk_read_time.write((str(chk1) + ':' + str(b) + ':' + str('00') + ' ' + str(amorpm_whatsapp).upper()))
                chk_read_time.close()

            if len(b) != 2:
                chk2 = str(0) + str(e_2.get())
                os.remove('requests//Time.txt')
                chk2_read_time = open('requests//Time.txt', 'w')
                chk2_read_time.write((str(a) + ':' + str(chk2) + ':' + str('00') + ' ' + str(amorpm_whatsapp).upper()))
                chk2_read_time.close()

            if len(a) != 2 and len(b) != 2:
                chk_both = str(0) + str(e_1.get())
                chk_both_2 = str(0) + str(e_2.get())
                os.remove('requests//Time.txt')
                chk_both_read_time = open('requests//Time.txt', 'w')
                chk_both_read_time.write(
                    (str(chk_both) + ':' + str(chk_both_2) + ':' + str('00') + ' ' + str(amorpm_whatsapp).upper()))
                chk_both_read_time.close()

            if not a or not b or not amorpm_whatsapp:
                messagebox.showerror('Error', "All fields are required")

            if len(a) >= 3 or len(b) >= 3:
                messagebox.showerror('Error', 'Unexpected input. Exceeding Two digits. Proper timing needed')
                # clear the entry
                e_1.delete(0, END)
                e_2.delete(0, END)

            if str(amorpm_whatsapp).upper() != "AM" and str(amorpm_whatsapp).upper() != 'PM':
                messagebox.showerror('Error', 'Proper timing needed')
                e_3.delete(0, END)

            if len(a) < 3 and len(b) < 3 and a and b and amorpm_whatsapp and str(amorpm_whatsapp).upper() == 'AM' or str(
                    amorpm_whatsapp).upper() == 'PM':
                # Disabling the buttons and entry after the button is clicked
                e_1.config(state=DISABLED)
                e_2.config(state=DISABLED)
                e_3.config(state=DISABLED)
                btn_for_wh.config(state=DISABLED)
                l_4 = Label(text='Phone number: ', bg='ghost white', fg='black', font=('Apple LiSung', 16, 'bold'))
                l_4.place(x=160, y=360)
                l_5 = Label(text='Message: ', bg='ghost white', fg='black', font=('Apple LiSung', 16, 'bold'))
                l_5.place(x=218, y=410)
                e_4 = Entry(bg="black", fg='springgreen2', insertbackground='ghost white', font=('Arial', 15))
                e_4.place(x=453, y=375, anchor=CENTER, width=250, height=34)

                def e4_focus(focus4):
                    e_4.focus_set()

                e_5 = Entry(bg="black", fg='springgreen2', insertbackground='ghost white', font=('Arial', 15))
                e_5.place(x=453, y=423, anchor=CENTER, width=250, height=34)

                def e5_focus(focus5):
                    e_5.focus_set()

                e_4.bind("<Down>", e5_focus)
                e_5.bind("<Up>", e4_focus)

                def check_2(event1):
                    phone = e_4.get()
                    message = e_5.get()
                    file_message = open('requests//message.txt', 'w')
                    file_message.write(message)
                    file_message.close()
                    if len(phone) > 10:
                        messagebox.showwarning('Not Allowed', 'Exceeding 10 digit')
                        e_4.delete(0, END)

                    elif len(phone) < 10:
                        messagebox.showwarning('Not Allowed', 'Number incorrect')
                        e_4.delete(0, END)

                    if len(phone) == 10:
                        file_phone = open('requests//phone.txt', 'w')
                        file_phone.write(phone)
                        file_phone.close()
                        temp_time = open('requests//Time.txt', 'r')
                        temp_phone = open('requests//phone.txt', 'r')
                        win_1.destroy()
                        root = Tk()
                        root.overrideredirect(1)

                        root.withdraw()
                        ask_ok_cancel = messagebox.askokcancel('Time Scheduled',
                                                               'Your message will reach ' + temp_phone.read() + ' in ' + temp_time.read() + '. Click OK to continue',
                                                               icon='info')
                        temp_time.close()
                        temp_phone.close()

                        def bg_wh():
                            while True:
                                date = datetime.today() + timedelta(hours=0, minutes=2)
                                adv = date.strftime('%I:%M:%S %p')
                                read_time = open('requests//Time.txt', 'r')
                                combine = read_time.read()
                                time.sleep(0.50)
                                # print('2 minutes advanced timer: ', adv)
                                # print('Scheduled timing -------: ', combine)
                                if adv != combine:
                                    pass
                                    # print('Did not match', '\n')
                                if adv == combine:
                                    read_phone = open('requests//phone.txt', 'r')
                                    read_message = open('requests//message.txt', 'r')
                                    phone_number = read_phone.read()
                                    messages_getting = read_message.read()
                                    # print('Matches')
                                    os.system('start microsoft-edge:')
                                    time.sleep(2)
                                    pyautogui.typewrite(
                                        'https://web.whatsapp.com/send?phone=+91' + str(phone_number) + '&text=' + str(
                                            messages_getting))
                                    time.sleep(1)
                                    pyautogui.press('enter')
                                    while adv == combine:
                                        original = time.strftime('%I:%M:%S %p')
                                        time.sleep(0.50)
                                        # print('True time----------: ', original)
                                        # print('Your scheduled time: ', combine)
                                        if original != combine:
                                            # print('Did not match')
                                            pass
                                        if original == combine:
                                            # print('Matches')
                                            pyautogui.click(x=924, y=725)
                                            pyautogui.press('enter')
                                            time.sleep(5)
                                            read_phone.close()
                                            read_message.close()
                                            read_time.close()
                                            time.sleep(5)
                                            pyautogui.hotkey('alt', 'f4')
                                            notification1 = win10toast.ToastNotifier()
                                            notification1.show_toast('WI-Scheduler',
                                                                     'Your messages reached ' + phone_number + ' successfully',
                                                                     duration=15,
                                                                     icon_path="requests//favicon.ico")
                                            break

                                    break

                            exit()

                        if ask_ok_cancel:
                            bg_wh()
                        if not ask_ok_cancel:
                            exit()

                Button(text='DONE', height=1, width=12, borderwidth=0, bg='black', fg='springgreen1',
                       font=('Arial', 15),
                       activebackground='springgreen2', activeforeground='black', command=lambda: check_2(event1=None),
                       cursor='hand2').place(
                    x=710,
                    y=395,
                    anchor=CENTER)
                e_4.focus()
                e_5.bind("<Return>", check_2)

        btn_for_wh = Button(text='VERIFY', height=1, width=12, borderwidth=0, bg='black', fg='springgreen1',
                            font=('Arial', 15),
                            activebackground='springgreen1', activeforeground='black', command=lambda: check(event=None),
                            cursor='hand2',
                            state=NORMAL)
        btn_for_wh.place(x=450, y=307, anchor=CENTER)
        e_3.bind("<Return>", check)

        icon = PhotoImage(file="requests//favicon.png")
        image = Image.open("requests//favicon.png")
        crop_wa = image.resize((200, 200))
        final_wa = ImageTk.PhotoImage(crop_wa)
        Label(image=final_wa, bd=0, bg='ghost white').place(x=600, y=80)
        win_1.iconphoto(False, icon)
        win_1.mainloop()
    finally:
        try:
            os.remove('requests//Time.txt')
        except Exception:
            pass
        try:
            os.remove('requests//phone.txt')
        except Exception:
            pass
        try:
            os.remove('requests//message.txt')
        except Exception:
            pass


def instagram():
    try:
        start_window.destroy()
        win_2 = Tk()
        win_2.focus_force()
        win_2.config(bg='ghost white')
        window_width____ = 1000
        window_height____ = 500
        # get the screen dimension
        screen_width____ = win_2.winfo_screenwidth()
        screen_height____ = win_2.winfo_screenheight()
        # find the center point
        center_x____ = int(screen_width____ / 2 - window_width____ / 2)
        center_y____ = int(screen_height____ / 2 - window_height____ / 2)
        win_2.geometry(f'{window_width____}x{window_height____}+{center_x____}+{center_y____}')
        win_2.geometry('1000x500')
        win_2.title('Instagram Automation')
        bg_insta_2 = PhotoImage(file="requests//insta_back.png")
        Label(image=bg_insta_2, height=1920, width=1080).pack()
        win_2.resizable(False, False)
        canvas_insta = Canvas(win_2, bg='ghost white', height=250, width=500, highlightbackground="black")
        canvas_insta.place(relx=0.5, rely=0.5, anchor=CENTER)
        canvas_2_insta = Canvas(win_2, bg='black', height=50, width=500, highlightbackground="black")
        canvas_2_insta.place(x=500, y=130, anchor=CENTER)
        l_head_insta = Label(win_2, text='INSTAGRAM AUTOMATION', bg='black', fg='darkorchid1', font=('Arial', 25, 'bold'))
        l_head_insta.place(x=500, y=130, anchor=CENTER)
        l_1_insta = Label(win_2, text='Hour: ', bg='ghost white', fg='black', font=('Apple LiSung', 16, 'bold'))
        l_1_insta.place(x=330, y=200, anchor=CENTER)
        l_2_insta = Label(win_2, text='Minutes: ', bg='ghost white', fg='black', font=('Apple LiSung', 15, 'bold'))
        l_2_insta.place(x=317, y=250, anchor=CENTER)
        l_3_insta = Label(win_2, text='AM or PM: ', bg='ghost white', fg='black', font=('Apple LiSung', 14, 'bold'))
        l_3_insta.place(x=310, y=300, anchor=CENTER)
        e_1_insta = Entry(win_2, bg="black", fg='darkorchid1', insertbackground='ghost white', font=('Arial', 15), bd=0)
        e_1_insta.place(x=490, y=200, anchor=CENTER, width=250, height=34)

        def insta1(focus6):
            e_1_insta.focus_set()

        e_2_insta = Entry(win_2, bg="black", fg='darkorchid1', insertbackground='ghost white', font=('Arial', 15), bd=0)
        e_2_insta.place(x=490, y=250, anchor=CENTER, width=250, height=34)

        def insta2(focus7):
            e_2_insta.focus_set()

        e_3_insta = Entry(win_2, bg="black", fg='darkorchid1', insertbackground='ghost white', font=('Arial', 15), bd=0)
        e_3_insta.place(x=490, y=300, anchor=CENTER, width=250, height=34)

        def insta3(focus8):
            e_3_insta.focus_set()

        e_1_insta.bind("<Down>", insta2)
        e_2_insta.bind("<Down>", insta3)
        e_3_insta.bind("<Up>", insta2)
        e_2_insta.bind("<Up>", insta1)

        def check(event2):
            a_insta = e_1_insta.get()
            b_insta = e_2_insta.get()
            ampm = e_3_insta.get()
            file_time = open('requests//Time.txt', 'w')
            file_time.write((str(a_insta) + ':' + str(b_insta) + ':' + str('00') + ' ' + str(ampm).upper()))
            file_time.close()
            if len(a_insta) != 2:
                chk1 = str(0) + str(e_1_insta.get())
                os.remove('requests//Time.txt')
                chk_read_time = open('requests//Time.txt', 'w')
                chk_read_time.write((str(chk1) + ':' + str(b_insta) + ':' + str('00') + ' ' + str(ampm).upper()))
                chk_read_time.close()
            if len(b_insta) != 2:
                chk2 = str(0) + str(e_2_insta.get())
                os.remove('requests//Time.txt')
                chk2_read_time = open('requests//Time.txt', 'w')
                chk2_read_time.write((str(a_insta) + ':' + str(chk2) + ':' + str('00') + ' ' + str(ampm).upper()))
                chk2_read_time.close()
            if len(a_insta) != 2 and len(b_insta) != 2:
                chk_both = str(0) + str(e_1_insta.get())
                chk_both_2 = str(0) + str(e_2_insta.get())
                os.remove('requests//Time.txt')
                chk_both_read_time = open('requests//Time.txt', 'w')
                chk_both_read_time.write(
                    (str(chk_both) + ':' + str(chk_both_2) + ':' + str('00') + ' ' + str(ampm).upper()))
                chk_both_read_time.close()
            if not a_insta or not b_insta or not ampm:
                messagebox.showerror('Error', "All fields are required")
            if len(a_insta) >= 3 or len(b_insta) >= 3:
                messagebox.showerror('Error', 'Unexpected input. Exceeding Two digits. Proper timing needed')
                e_1_insta.delete(0, END)
                e_2_insta.delete(0, END)
            if len(ampm) != 2 or str(ampm).upper() != "AM" and str(ampm).upper() != 'PM':
                messagebox.showerror('Error', 'AM or PM ?')
                e_3_insta.delete(0, END)
            if len(a_insta) < 3 and len(b_insta) < 3 and a_insta and b_insta and str(ampm).upper() == 'AM' or str(
                    ampm).upper() == 'PM':
                win_2.destroy()
                win_3 = Tk()
                win_3.focus_force()
                bg_insta = PhotoImage(file="requests//insta_back_two.png")
                Label(image=bg_insta, height=1920, width=1080).pack()
                window_width___ = 1000
                window_height___ = 500
                # get the screen dimension
                screen_width___ = win_3.winfo_screenwidth()
                screen_height___ = win_3.winfo_screenheight()
                # find the center point
                center_x___ = int(screen_width___ / 2 - window_width___ / 2)
                center_y___ = int(screen_height___ / 2 - window_height___ / 2)
                win_3.geometry(f'{window_width___}x{window_height___}+{center_x___}+{center_y___}')
                win_3.title('Instagram Automation')
                win_3.resizable(False, False)
                canvas_insta_1 = Canvas(win_3, bg='ghost white', height=250, width=500, highlightbackground="black")
                canvas_insta_1.place(relx=0.5, rely=0.5, anchor=CENTER)
                canvas_2_insta_2 = Canvas(win_3, bg='black', height=50, width=500, highlightbackground="black")
                canvas_2_insta_2.place(x=500, y=130, anchor=CENTER)
                l_head_insta_1 = Label(win_3, text='INSTAGRAM AUTOMATION', bg='black', fg='darkorchid1',
                                       font=('Arial', 25, 'bold'))
                l_head_insta_1.place(x=500, y=130, anchor=CENTER)
                l_1_insta_2 = Label(win_3, text='YOUR USERNAME: ', bg='ghost white', fg='black',
                                    font=('Apple LiSung', 16, 'bold'))
                l_1_insta_2.place(x=360, y=211, anchor=CENTER)
                l_2_insta_3 = Label(win_3, text='YOUR PASSWORD: ', bg='ghost white', fg='black',
                                    font=('Apple LiSung', 15, 'bold'))
                l_2_insta_3.place(x=360, y=270, anchor=CENTER)
                e_4_insta_4 = Entry(win_3, bg="black", fg='darkorchid1', insertbackground='ghost white', font=('Arial', 15))
                e_4_insta_4.place(x=580, y=210, anchor=CENTER, width=250, height=34)

                def insta4(focus9):
                    e_4_insta_4.focus_force()

                def show():
                    e_5_insta_5.config(show="")
                    e_5_button.config(text='HIDE PASSWORD', command=hide)
                    e_5_button.place(x=614, y=235)

                def hide():
                    e_5_insta_5.config(show='•')
                    e_5_button.config(text='SHOW PASSWORD', command=show)
                    e_5_button.place(x=605, y=235)

                e_5_button = Button(text="SHOW PASSWORD", font=('Apple LiSung', 8, 'bold'), borderwidth=0, fg='blue',
                                    cursor='hand2', command=show)
                e_5_button.place(x=605, y=235)

                e_5_insta_5 = Entry(win_3, bg="black", fg='darkorchid1', insertbackground='ghost white', show='•',
                                    font=('Arial', 15))
                e_5_insta_5.place(x=580, y=270, anchor=CENTER, width=250, height=34)

                def insta5(focus10):
                    e_5_insta_5.focus_force()

                e_4_insta_4.bind("<Down>", insta5)
                e_5_insta_5.bind("<Up>", insta4)

                def check_2(event3):
                    l_1_insta_2_get = e_4_insta_4.get()
                    l_2_insta_3_get = e_5_insta_5.get()
                    if not l_1_insta_2_get or not l_2_insta_3_get:
                        messagebox.showerror('WI-Scheduler', 'All fields are required')
                    if l_1_insta_2_get and l_2_insta_3_get:
                        user_save = open('requests//username.txt', 'w')
                        user_save.write(str(l_1_insta_2_get).lower())
                        user_save.close()
                        pass_save = open('requests//password.txt', 'w')
                        pass_save.write(str(l_2_insta_3_get))
                        pass_save.close()
                        win_3.destroy()
                        win_4 = Tk()
                        win_4.focus_force()
                        bg_insta_3 = PhotoImage(
                            file="requests//insta_back_three.png")
                        Label(image=bg_insta_3, height=1920, width=1080).pack()
                        window_width__ = 1000
                        window_height__ = 500
                        # get the screen dimension
                        screen_width__ = win_4.winfo_screenwidth()
                        screen_height__ = win_4.winfo_screenheight()
                        # find the center point
                        center_x__ = int(screen_width__ / 2 - window_width__ / 2)
                        center_y__ = int(screen_height__ / 2 - window_height__ / 2)
                        win_4.geometry(f'{window_width__}x{window_height__}+{center_x__}+{center_y__}')
                        win_4.title('Instagram Automation')
                        win_4.resizable(False, False)
                        canvas_insta_3_1 = Canvas(win_4, bg='ghost white', height=250, width=500,
                                                  highlightbackground="black")
                        canvas_insta_3_1.place(relx=0.5, rely=0.5, anchor=CENTER)
                        canvas_2_insta_3_2 = Canvas(win_4, bg='black', height=50, width=500, highlightbackground="black")
                        canvas_2_insta_3_2.place(x=500, y=130, anchor=CENTER)
                        l_head_insta_3_1 = Label(win_4, text='INSTAGRAM AUTOMATION', bg='black', fg='darkorchid1',
                                                 font=('Arial', 25, 'bold'))
                        l_head_insta_3_1.place(x=500, y=130, anchor=CENTER)
                        l_4_in_3 = Label(win_4, text="Receiver's Username: ", bg='ghost white', fg='black',
                                         font=('Apple LiSung', 16, 'bold'))
                        l_4_in_3.place(x=250, y=190)
                        l_5_in_3 = Label(win_4, text='Message to send: ', bg='ghost white', fg='black',
                                         font=('Apple LiSung', 16, 'bold'))
                        l_5_in_3.place(x=291, y=245)
                        e_4_in_3 = Entry(win_4, bg="black", fg='darkorchid1', insertbackground='ghost white',
                                         font=('Arial', 15))
                        e_4_in_3.place(x=610, y=205, anchor=CENTER, width=250, height=34)

                        def insta6(focus11):
                            e_4_in_3.focus_set()

                        e_5_in_3 = Entry(win_4, bg="black", fg='darkorchid1', insertbackground='ghost white',
                                         font=('Arial', 15))
                        e_5_in_3.place(x=610, y=260, anchor=CENTER, width=250, height=34)

                        def insta7(focus12):
                            e_5_in_3.focus_set()

                        e_4_in_3.bind("<Down>", insta7)
                        e_5_in_3.bind("<Up>", insta6)

                        def timeready(event4):
                            re_user = e_4_in_3.get()
                            re_msg = e_5_in_3.get()
                            if not re_user or not re_msg:
                                messagebox.showerror('ERROR', 'All fields are required')
                            if re_msg and re_user:
                                res_user = open('requests//receiveruser.txt', 'w')
                                res_user.write(re_user.lower())
                                res_user.close()
                                res_msg = open('requests//receivermsg.txt', 'w')
                                res_msg.write(re_msg)
                                res_msg.close()
                                win_4.destroy()
                                user_read = open('requests//username.txt', 'r')
                                user_of_in = user_read.read()
                                pass_read = open('requests//password.txt', 'r')
                                pass_of_in = pass_read.read()
                                op_time_insta = open('requests//Time.txt', 'r')
                                combine_insta = op_time_insta.read()
                                read_res_user = open('requests//receiveruser.txt', 'r')
                                o = read_res_user.read()
                                read_res_msg = open('requests//receivermsg.txt', 'r')
                                root = Tk()
                                root.overrideredirect(1)
                                root.withdraw()
                                ask_ok_cancel = messagebox.askokcancel('Time Scheduled',
                                                                       'Your message will reach ' + o + ' in ' + combine_insta + '. Click OK to continue',
                                                                       icon='info')

                                def bg():
                                    while True:
                                        date_insta = datetime.today() + timedelta(hours=0, minutes=2)
                                        adv_insta = date_insta.strftime('%I:%M:%S %p')
                                        time.sleep(0.50)
                                        # print('2 minutes advanced timer: ', adv_insta)
                                        # print('Scheduled timing -------: ', combine_insta)
                                        if adv_insta != combine_insta:
                                            pass
                                            # print('Did not match', '\n')
                                        if combine_insta == adv_insta:
                                            p = read_res_msg.read()
                                            # print('Matches')
                                            browser = webdriver.Chrome(
                                                "requests//chromedriver.exe")
                                            browser.get('https://www.instagram.com/')
                                            pyautogui.hotkey('win', 'up')
                                            time.sleep(10)
                                            # Using selenium to automate web browser
                                            username_element = browser.find_element_by_name('username')
                                            username_element.send_keys(str(user_of_in))
                                            time.sleep(1)
                                            password_element = browser.find_element_by_name('password')
                                            password_element.send_keys(str(pass_of_in))
                                            time.sleep(1)
                                            pyautogui.press('enter')
                                            time.sleep(8)
                                            search_box = browser.find_element_by_class_name('TqC_a')
                                            search_box.click()
                                            time.sleep(2)
                                            pyautogui.typewrite(o)
                                            time.sleep(3)
                                            pyautogui.press('enter')
                                            time.sleep(1)
                                            pyautogui.press('enter')
                                            time.sleep(5)
                                            browser.find_element_by_class_name('_8A5w5 ').click()
                                            time.sleep(5)
                                            browser.find_element_by_class_name('HoLwm').click()
                                            time.sleep(4)
                                            browser.find_element_by_class_name('Igw0E.IwRSH.eGOV_.vwCYk.ItkAi').click()
                                            pyautogui.typewrite(p)
                                            while adv_insta == combine_insta:
                                                original_insta = time.strftime('%I:%M:%S %p')
                                                time.sleep(0.50)
                                                # print('True time----------: ', original_insta)
                                                # print('Your scheduled time: ', combine_insta)
                                                if original_insta != combine_insta:
                                                    pass
                                                    # print('Did not match', '\n')
                                                if original_insta == combine_insta:
                                                    # print('Matches')
                                                    pyautogui.press('enter')
                                                    time.sleep(3)
                                                    browser.close()
                                                    user_read.close()
                                                    pass_read.close()
                                                    op_time_insta.close()
                                                    read_res_msg.close()
                                                    read_res_user.close()
                                                    os.remove('requests//username.txt')
                                                    os.remove('requests//password.txt')
                                                    os.remove('requests//Time.txt')
                                                    os.remove('requests//receiveruser.txt')
                                                    os.remove('requests//receivermsg.txt')
                                                    notification2 = win10toast.ToastNotifier()
                                                    notification2.show_toast('WI-Scheduler',
                                                                             'Your messages reached ' + o + ' successfully',
                                                                             duration=10,
                                                                             icon_path="requests//favicon.ico")
                                                    break

                                            break
                                    exit()
                                    # Closing and breaking everything

                                if ask_ok_cancel:
                                    try:
                                        bg()
                                    except Exception:
                                        unknown_error = Tk()
                                        unknown_error.withdraw()
                                        unknown_error.wm_iconbitmap("requests//favicon.ico")
                                        messagebox.showerror('Error',
                                                             'Unknown Error Occurred. Check your Internet connection / quality')
                                        user_read.close()
                                        pass_read.close()
                                        op_time_insta.close()
                                        read_res_msg.close()
                                        read_res_user.close()
                                        exit()

                                if not ask_ok_cancel:
                                    notification4 = win10toast.ToastNotifier()
                                    notification4.show_toast('WI-Scheduler', 'Instagram automation cancelled', duration=10,
                                                             icon_path="requests//favicon.ico")
                                    user_read.close()
                                    pass_read.close()
                                    op_time_insta.close()
                                    read_res_msg.close()
                                    read_res_user.close()
                                    exit()

                        Button(win_4, text='DONE', height=0, width=12, borderwidth=0, bg='black', fg='darkorchid',
                               font=('Arial', 15, 'bold'),
                               activebackground='darkorchid1', activeforeground='black',
                               command=lambda: timeready(event4=None), cursor='hand2',
                               state=NORMAL).place(x=609,
                                                   y=325,
                                                   anchor=CENTER)
                        win_4.wm_iconbitmap("requests//favicon.ico")
                        e_5_in_3.bind("<Return>", timeready)
                        win_4.mainloop()

                Button(win_3, text='GO', height=0, width=12, borderwidth=0, bg='black', fg='darkorchid',
                       font=('Arial', 15, 'bold'),
                       activebackground='darkorchid1', activeforeground='black', command=lambda: check_2(event3=None),
                       cursor='hand2',
                       state=NORMAL).place(x=580,
                                           y=327,
                                           anchor=CENTER)
                win_3.wm_iconbitmap("requests//favicon.ico")
                e_5_insta_5.bind("<Return>", check_2)
                win_3.mainloop()

        Button(win_2, text='DONE', height=1, width=12, borderwidth=0, bg='black', fg='darkorchid1',
               font=('Arial', 15),
               activebackground='darkorchid1', activeforeground='black', command=lambda: check(event2=None), cursor='hand2',
               state=NORMAL).place(x=492,
                                   y=345,
                                   anchor=CENTER)
        e_3_insta.bind("<Return>", check)

        image = Image.open("requests//favicon.png")
        crop_in = image.resize((120, 120))
        final_in = ImageTk.PhotoImage(crop_in)
        Label(win_2, image=final_in, bd=0, bg='ghost white').place(x=620, y=180)
        win_2.wm_iconbitmap("requests//favicon.ico")
        win_2.mainloop()

    finally:
        try:
            os.remove('requests//username.txt')
        except Exception:
            pass
        try:
            os.remove('requests//password.txt')
        except Exception:
            pass
        try:
            os.remove('requests//Time.txt')
        except Exception:
            pass
        try:
            os.remove('requests//receiveruser.txt')
        except Exception:
            pass
        try:
            os.remove('requests//receivermsg.txt')
        except Exception:
            pass


try:
    admin = open('requests//administrator.txt', 'w')
    admin.write('Access granted')
    admin.close()
    os.remove("requests//administrator.txt")
except PermissionError:
    ad = Tk()
    ad.withdraw()
    messagebox.showerror('Access Denied', 'Please run this app as administrator')
    exit()

try:
    chk = requests.get('https://www.google.com')
    start_window = Tk()
    start_window.title('WI-SCHEDULER')
    window_width_ = 1000
    window_height_ = 500
    # get the screen dimension
    screen_width_ = start_window.winfo_screenwidth()
    screen_height_ = start_window.winfo_screenheight()
    # find the center point
    center_x_ = int(screen_width_ / 2 - window_width_ / 2)
    center_y_ = int(screen_height_ / 2 - window_height_ / 2)
    start_window.geometry(f'{window_width_}x{window_height_}+{center_x_}+{center_y_}')
    start_window.resizable(False, False)
    bgm = PhotoImage(file="requests//questionbackground.png")
    Label(image=bgm, height=1920, width=1080).pack()
    canvas_main = Canvas(start_window, bg='ghost white', height=450, width=700, highlightbackground="black")
    canvas_main.place(relx=0.5, rely=0.5, anchor=CENTER)
    canvas_2_main = Canvas(start_window, bg='black', height=50, width=700, highlightbackground="black")
    canvas_2_main.place(x=500, y=50, anchor=CENTER)
    l_head_main = Label(text='WI-SCHEDULER', bg='black', fg='cyan', font=('Arial', 25, 'bold'))
    l_head_main.place(x=500, y=50, anchor=CENTER)
    Button(text='WHATSAPP AUTOMATION', height=1, width=30, borderwidth=0, bg='black', fg='springgreen1',
           font=('Arial', 15),
           activebackground='springgreen1', activeforeground='black', command=whatsapp, cursor='hand2',
           state=NORMAL).place(x=500,
                               y=200,
                               anchor=CENTER)
    Button(text='INSTAGRAM AUTOMATION', height=1, width=30, borderwidth=0, bg='black', fg='darkorchid1',
           font=('Arial', 15),
           activebackground='darkorchid1', activeforeground='black', command=instagram, cursor='hand2',
           state=NORMAL).place(x=500,
                               y=300,
                               anchor=CENTER)
    Label(text='(OR)', font=('Arial', 15, 'bold'), bg='ghost white').place(x=469, y=240)
    icon_main = PhotoImage(file="requests//favicon.png")
    image_main = Image.open("requests//favicon.png")
    crop = image_main.resize((150, 150))
    final_main = ImageTk.PhotoImage(crop)
    Label(text='WI', font=('Arial', 25, 'bold'), fg='red', bg='ghost white').place(x=470, y=110)
    Label(image=final_main, bd=0, bg='ghost white').place(x=420, y=320)
    start_window.wm_iconbitmap("requests//favicon.ico")
    start_window.mainloop()
except requests.exceptions.ConnectionError:
    root2 = Tk()
    root2.overrideredirect(1)
    root2.wm_iconbitmap("requests//favicon.ico")
    root2.withdraw()
    messagebox.showerror('Disconnected', 'You are not connected to the Internet')

# Completely done by Muhil Raj
