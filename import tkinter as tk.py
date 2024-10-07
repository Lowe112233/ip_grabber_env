import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests

def get_map():
    ip_address = ip_entry.get()
    if not ip_address:
        messagebox.showerror("Error", "Please enter a valid IP address")
        return
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        lat = data["lat"]
        lon = data["lon"]
        
        url = f"https://www.openstreetmap.org/search?q={lat},{lon}&form=search&show_tiles=true"
        webbrowser.open(url)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_location():
    ip_address = ip_entry.get()
    if not ip_address:
        messagebox.showerror("Error", "Please enter a valid IP address")
        return
    
    try:
        response = requests.get(f"https://api.ipgeolocationfree.com/v1/publicip?apiKey=7b7859cd4ad34e25b76f1a41d1b32f7b")
        data = response.json()
        
        lat = data["latitude"]
        lon = data["longitude"]
        
        url = f"https://www.openstreetmap.org/search?q={lat},{lon}&form=search&show_tiles=true"
        webbrowser.open(url)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("IP Address to OpenStreetMap")

ip_label = tk.Label(root, text="Enter IP Address:")
ip_label.grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root, width=40)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

map_button = tk.Button(root, text="Open OpenStreetMap", command=get_map)
map_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

location_button = tk.Button(root, text="Get Location", command=get_location)
location_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()