import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests

def get_map():
    ip_address = ip_entry.get()
    if not ip_address:
        messagebox.showerror("Error", "Please enter a valid IP address")
        return
    
    api_url = f"https://nominatim.openstreetmap.org/search?q={ip_address}&format=json"
    
    response = requests.get(api_url)
    data = response.json()[0]
    
    map_url = f"http://maps.google.com/maps?api=s2&center={data['lat']},{data['lon']}&zoom=12&output=embed"
    
    webbrowser.open(map_url)

def get_location():
    ip_address = ip_entry.get()
    if not ip_address:
        messagebox.showerror("Error", "Please enter a valid IP address")
        return
    
    api_url = f"https://api.ipgeolocationfree.com/v1/publicip?apiKey=YOUR_API_KEY"
    
    response = requests.get(api_url)
    data = response.json()
    location = data["latitude"] + "," + data["longitude"]
    
    map_url = f"http://maps.google.com/maps?api=s2&center={location}&zoom=12&output=embed"
    
    webbrowser.open(map_url)

root = tk.Tk()
root.title("IP Address to Google Maps")

ip_label = tk.Label(root, text="Enter IP Address:")
ip_label.grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root, width=40)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

map_button = tk.Button(root, text="Open Google Maps", command=get_map)
map_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

location_button = tk.Button(root, text="Get Location", command=get_location)
location_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()