import tkinter.messagebox as tmsg
import tkinter as tk
import random

gamenumber = 0

#ボタンがクリックされた時の処理
def ButtonClick():
    global gamenumber
    b = editbox1.get()

    #入力されたデータが4桁の数字かどうかを判定する
    import re

    isok = False
    while isok == False:
        if not re.match(r"^\d\d\d\d$", b):
            tmsg.showerror("Error!", "Enter a 4 digit number")
            break
        else:
            isok = True

            hit = 0
            for i in range(4):
                if a[i] == int(b[i]):
                    hit += 1

            blow = 0
            for j in range(4):
                for i in range(4):
                    if int(b[j]) == a[i] and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                        blow += 1
                        break

            gamenumber += 1

            #ヒットが４なら当たりで終了
            if hit == 4:
                tmsg.showinfo("Right", "You got it right!")
                tmsg.showinfo("Complete", "You tried " +
                              str(gamenumber) + " time(s)!")
                root.destroy()
            else:
                #ヒット数とブロー数を表示
                rirekibox.insert(tk.END, b + "/Hit" +
                                 str(hit) + "/"+"Blow" + str(blow) + "\n")


a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]

print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))


#ウィンドウを作る、入力履歴を表示する
root = tk.Tk()
root.geometry("600x400")
root.title("Hit and Blow game")
rirekibox = tk.Text(root, font=("Arial, 14"))
rirekibox.place(x=400, y=0, width=200, height=400)

#ラベルを作る
label1 = tk.Label(root, text="Enter a number", font=("Arial", 14))
label1.place(x=20, y=20)

#テキストボックスを作る
editbox1 = tk.Entry(width=4, font=("Arial, 28"))
editbox1.place(x=120, y=65)

#ボタンを作る
button1 = tk.Button(root, text="Check", font=(
    "Arial", 14), command=ButtonClick)
button1.place(x=220, y=65)

#ウィンドウを表示する
root.mainloop()
