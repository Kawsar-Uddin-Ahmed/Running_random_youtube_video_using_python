import random
import threading
import webbrowser
def running():
    i = int(input("How many links you want : "))
    for j in range(i):
        c = input()
        with open("Links.txt", "a") as f:
                print(c, file=f) #Here file=f is used so that the input can be written in the created file. 
    with open("Links.txt","r") as m:
        d = m.readlines()
        b = random.choice(d)
        webbrowser.open_new(b)
    threading.Timer(10,running).start() #It will recall from inside the function means it is a recursion
if __name__ == '__main__':
    running()

