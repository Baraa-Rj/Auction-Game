import tkinter as tk
from tkinter import simpledialog, messagebox

bidders = {}
highest_bidder = ""


def start_auction():
    global highest_bidder
    while True:
        name = simpledialog.askstring("Bidder Name", "What is your name?")
        if not name:
            break

        bid = simpledialog.askinteger("Bid Amount", "What's your bid?")
        if not bid:
            break

        if name in bidders:
            bidders[name] += bid
        else:
            bidders[name] = bid

        if highest_bidder == "" or bidders[name] > bidders[highest_bidder]:
            highest_bidder = name

        continue_bidding = messagebox.askyesno("More Bidders", "Are there any other bidders?")
        if not continue_bidding:
            break

    if highest_bidder:
        result_message = f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}"
        messagebox.showinfo("Auction Result", result_message)
    else:
        messagebox.showinfo("Auction Result", "No bids were placed.")


app = tk.Tk()
app.title("Secret Auction Program")
app.geometry("400x200")

welcome_label = tk.Label(app, text="Welcome to the Secret Auction Program", font=("Arial", 14))
welcome_label.pack(pady=20)

start_button = tk.Button(app, text="Start Auction", command=start_auction, font=("Arial", 12), bg="#4CAF50", fg="white")
start_button.pack(pady=10)

app.mainloop()
