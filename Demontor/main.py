import yfinance as yf
from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Dementor Stock Trader")
root.configure(background="black")
root.geometry("600x400")
ticker_Name = tk.StringVar()


def submit():

    tickername = ticker_Name.get()
    label = tk.Label(text=""+tickername)
    label.pack()
    ticker = yf.Ticker(tickername)
    ticker.history(period="1d", interval="1m")
    tk.Label(text=ticker.info.get('currentPrice')).pack()
    ticker_Name.set("")


ticker_entry = tk.Entry(root, textvariable=ticker_Name)
sub_btn = tk.Button(root, text="Submit", command=submit)
ticker_entry.pack()
sub_btn.pack()
root.mainloop()


