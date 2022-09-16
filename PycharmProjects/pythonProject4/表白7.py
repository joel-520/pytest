def closeWindow():
    messagebox.showinfo(title="警告", message="关不掉吧，气不气")


    return

#点击不喜欢的事件


def noLove():
    no_love = Toplevel(window)

    no_love.geometry("300x100+610+260")

    no_love.title("我好喜欢你")

    label = Label(no_love, text="再考虑考虑呗", font=("华文行楷", 25))

    label.pack()

    btn = Button(

        no_love,

        text="好吧",

        width=10,

        height=2,

        command=no_love.destroy)

    btn.pack()

    no_love.protocol("WM_DELETE_WINDOW", closeNoLove)


def closeNoLove():
    # messagebox.showinfo("不喜欢我，你就关不掉")

    messagebox.showinfo(title="警告", message="不喜欢我，你就关不掉")

    noLove()


# 点击喜欢 然后关闭窗体的事件

def closelove():
    messagebox.showinfo(title="好怂啊你", message="喜欢我直说就行")


    return

#喜欢的事件


def love():
    love = Toplevel(window)

    love.geometry("300x150+610+260")

    love.title("好巧啊，我也喜欢你")

    label = Label(love, text="如家酒店A350等你", font=("华文行楷", 20))

    label.pack()

    label = Label(love, text="电话给我，美滋滋", font=("华文行楷", 25))

    label.pack()

    entry = Entry(love, font=("楷体", 15))

    entry.pack()

    btn = Button(love, text="嗯嗯", width=10, height=2, command=closeallwindow)

    btn.pack()

    love.protocol("WM_DELETE_WINDOW", closelove)