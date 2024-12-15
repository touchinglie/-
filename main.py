import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from functionpack import *
from logincheck import *


# 方法函数
def login(username1="none", password1="none"):
    username1 = str(username.get())
    password1 = str(password.get())
    if checkUserKey.checking(username1, password1):
        txt = "正在加载"
        messagebox.showinfo(title="登录成功", message=txt)
        window.destroy()
        open_child_window()
    else:
        txt = "账号密码有误"
        messagebox.showinfo(title="登录失败", message=txt)


def importing():
    global fileaddress
    global importingwindow
    fileaddress = tk.StringVar()
    importingwindow = tk.Toplevel()
    importingwindow.geometry("250x100")
    importingwindow.title("importing")
    importingwindow.iconbitmap("icon.ico")

    text = "导入sqlite数据库地址:"
    label_username = tk.Label(
        importingwindow,
        text=text,
        font=("宋体", 10, "bold"),
        padx=5,
        pady=5,
        borderwidth=1,
    )
    label_username.place(x=7, y=20)

    entryfile = ttk.Entry(importingwindow, textvariable=fileaddress)
    entryfile.place(x=30, y=40)
    sure_button = tk.Button(importingwindow, text="确定", command=startimport)
    sure_button.place(x=200, y=40)


def startimport():
    delivery.listin(fileaddress.get())
    importingwindow.destroy()


def exporting():
    try:
        databackup.backup()
        txt = "已导出"
        messagebox.showinfo(title="成功", message=txt)
    except:
        txt = "导出出现错误"
        messagebox.showinfo(title="失败", message=txt)
        raise


def InsertNewKey():
    global NewKey
    global Insertwindow
    NewKey = tk.StringVar()
    Insertwindow = tk.Toplevel()
    Insertwindow.geometry("250x100")
    Insertwindow.title("Inserting")
    Insertwindow.iconbitmap("icon.ico")

    text = "请输入插入属性（用,分割）:"
    label_username = tk.Label(
        Insertwindow,
        text=text,
        font=("宋体", 10, "bold"),
        padx=5,
        pady=5,
        borderwidth=1,
    )
    label_username.place(x=7, y=20)

    entryfile = ttk.Entry(Insertwindow, textvariable=NewKey)
    entryfile.place(x=30, y=40)
    sure_button = tk.Button(Insertwindow, text="确定", command=InsertKey)
    sure_button.place(x=200, y=40)


def InsertKey():
    NewKey1 = NewKey.get().split(",")
    try:
        changer1.InsertNewKey(NewKey1[0], NewKey1[1], NewKey1[2], NewKey1[3])
        txt = "已插入"
        messagebox.showinfo(title="成功", message=txt)
        Insertwindow.destroy()
        child_window.destroy()
        open_child_window()
    except:
        txt = "插入值时出现错误"
        messagebox.showinfo(title="失败", message=txt)
        raise


def DeleteKey():
    global Deletekey
    global Deletewindow
    Deletekey = tk.StringVar()
    Deletewindow = tk.Toplevel()
    Deletewindow.geometry("250x100")
    Deletewindow.title("Deleteing")
    Deletewindow.iconbitmap("icon.ico")

    text = "请输入要删除属性的ID:"
    label_username = tk.Label(
        Deletewindow,
        text=text,
        font=("宋体", 10, "bold"),
        padx=5,
        pady=5,
        borderwidth=1,
    )
    label_username.place(x=7, y=20)

    entryfile = ttk.Entry(Deletewindow, textvariable=Deletekey)
    entryfile.place(x=30, y=40)
    sure_button = tk.Button(Deletewindow, text="确定", command=Delete)
    sure_button.place(x=200, y=40)


def Delete():
    DeleteKey1 = Deletekey.get()
    try:
        changer1.DeleteKey(DeleteKey1)
        txt = "已删除"
        messagebox.showinfo(title="成功", message=txt)
        Deletewindow.destroy()
        child_window.destroy()
        open_child_window()
    except:
        txt = "删除值时出现错误"
        messagebox.showinfo(title="失败", message=txt)
        raise


def UpdateKey():
    global Updatekey
    global Updatewindow
    Updatekey = tk.StringVar()
    Updatewindow = tk.Toplevel()
    Updatewindow.geometry("300x100")
    Updatewindow.title("Updating")
    Updatewindow.iconbitmap("icon.ico")

    text = "请输入更新对象的ID，名，值（用，分割）:"
    label_username = tk.Label(
        Updatewindow,
        text=text,
        font=("宋体", 10, "bold"),
        padx=5,
        pady=5,
        borderwidth=1,
    )
    label_username.place(x=7, y=20)

    entryfile = ttk.Entry(Updatewindow, textvariable=Updatekey)
    entryfile.place(x=30, y=40)
    sure_button = tk.Button(Updatewindow, text="确定", command=Update)
    sure_button.place(x=200, y=40)


def Update():
    Updatekey1 = Updatekey.get().split(",")
    try:
        changer1.UpdateKey(Updatekey1[0], Updatekey1[1], Updatekey1[2])
        txt = "已更新"
        messagebox.showinfo(title="成功", message=txt)
        Updatewindow.destroy()
        child_window.destroy()
        open_child_window()
    except:
        txt = "更新值时出现错误"
        messagebox.showinfo(title="失败", message=txt)
        raise


def CheckKey():
    global Checkkey
    global Checkwindow
    Checkkey = tk.StringVar()
    Checkwindow = tk.Toplevel()
    Checkwindow.geometry("300x100")
    Checkwindow.title("Checking")
    Checkwindow.iconbitmap("icon.ico")

    text = "请输入查找对象的ID:"
    label_username = tk.Label(
        Checkwindow,
        text=text,
        font=("宋体", 10, "bold"),
        padx=5,
        pady=5,
        borderwidth=1,
    )
    label_username.place(x=7, y=20)

    entryfile = ttk.Entry(Checkwindow, textvariable=Checkkey)
    entryfile.place(x=30, y=40)
    sure_button = tk.Button(Checkwindow, text="确定", command=Check)
    sure_button.place(x=200, y=40)


def Check():
    CheckKey1 = Checkkey.get()
    try:
        checkanswer = changer1.CheckKey(CheckKey1)
        txt = f"{checkanswer}"
        messagebox.showinfo(title="成功", message=txt)
        Checkwindow.destroy()
    except:
        txt = "查找值时出现错误"
        messagebox.showinfo(title="失败", message=txt)
        raise


def average():
    try:
        averageanswer = changer1.average()
        txt = f"{averageanswer}"
        messagebox.showinfo(title="平均结果", message=txt)
    except:
        txt = "查找值时出现错误"
        messagebox.showinfo(title="失败", message=txt)
        raise


def Excellence():
    try:
        Excellenceanswer = changer1.Excellence()
        txt = f"{Excellenceanswer}"
        messagebox.showinfo(title="平均结果", message=txt)
    except:
        txt = "查找值时出现错误"
        messagebox.showinfo(title="失败", message=txt)
        raise


def authorraise():
    global anthorwindow
    anthorwindow = tk.Toplevel()
    anthorwindow.geometry("300x300")
    anthorwindow.title("关于作者！")
    anthorwindow.iconbitmap("icon.ico")

    text = "© 2024 software by dow"
    label_anthor = tk.Label(
        anthorwindow,
        text=text,
        font=("宋体", 10, "bold"),
        padx=5,
        pady=5,
        borderwidth=1,
    )
    label_anthor.place(x=40, y=20)

    text1 = "License Released under MIT License, \n please note that the software should not be used for any commercial activities. \n This project used to be a secondary development based on https://dowblog.rr.nu/."
    label_about = tk.Label(
        anthorwindow,
        text=text1,
        font=("宋体", 10, "bold"),
        padx=5,
        pady=5,
        borderwidth=1,
        wraplength=300,
    )
    label_about.place(x=0, y=40)

    sure_button = tk.Button(anthorwindow, text="确定", command=exit)
    sure_button.place(x=250, y=260)


def exit():
    anthorwindow.destroy()


# 打开子窗口
def open_child_window():
    # 创建新的tk窗口对象实例
    global child_window
    Datafile = delivery.listdisplay()
    print(Datafile)
    child_window = tk.Tk()
    child_window.geometry("840x480")
    child_window.title("学生管理系统")
    child_window.iconbitmap("icon.ico")

    # 菜单部分
    mainmenu = tk.Menu(child_window)

    filemenu = tk.Menu(mainmenu, tearoff=False)
    editmenu = tk.Menu(mainmenu, tearoff=False)
    aboutmenu = tk.Menu(mainmenu, tearoff=False)
    filemenu.add_command(label="导入", command=importing)
    filemenu.add_command(label="导出", command=exporting)

    editmenu.add_command(label="插入", command=InsertNewKey)
    editmenu.add_command(label="删除", command=DeleteKey)
    editmenu.add_command(label="更新", command=UpdateKey)
    editmenu.add_command(label="查找", command=CheckKey)
    editmenu.add_separator()
    editmenu.add_command(label="求平均", command=average)
    editmenu.add_command(label="取优", command=Excellence)

    aboutmenu.add_command(label="关于作者", command=authorraise)

    mainmenu.add_cascade(label="文件", menu=filemenu)
    mainmenu.add_cascade(label="操作", menu=editmenu)
    mainmenu.add_cascade(label="关于", menu=aboutmenu)
    child_window.config(menu=mainmenu)

    # 窗口数据显示
    columns = ("ID", "Name", "Mark", "Gender")
    tree = ttk.Treeview(
        child_window, columns=columns, height=20, show="headings", displaycolumns="#all"
    )

    tree.heading("#0", text="")
    tree.heading("#1", text="ID")
    tree.heading("#2", text="姓名")
    tree.heading("#3", text="成绩")
    tree.heading("#4", text="性别")

    for index, data in enumerate(Datafile):
        tree.insert("", tk.END, text=index, value=data)
    tree.pack()

    child_window.mainloop()


# 创建独立登录窗口
window = tk.Tk()
window.title("学生管理系统登录界面")
window.iconbitmap = "icon.ico"
# 设置窗口大小
window.geometry("320x200")
username = tk.StringVar()
password = tk.StringVar()

text = "用户名"
label_username = tk.Label(
    window,
    text=text,
    font=("宋体", 10, "bold"),
    padx=5,
    pady=5,
    borderwidth=1,
)
label_username.place(x=30, y=40)

text = "密码"
label_key = tk.Label(
    window,
    text=text,
    font=("宋体", 10, "bold"),
    padx=5,
    pady=5,
    borderwidth=1,
)
label_key.place(x=35, y=90)

entryusername = ttk.Entry(window, textvariable=username)
entryusername.place(x=115, y=40)
entrypassword = ttk.Entry(window, textvariable=password, show="*")
entrypassword.place(x=115, y=90)
# 登录验证按钮触发方法函数
open_child_button = tk.Button(window, text="登录", command=login)
open_child_button.place(x=260, y=140)
window.mainloop()
