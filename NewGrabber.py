import tkinter as tk
from tkinter import messagebox
import requests
import folium
import os
from ipwhois import IPWhois

# Function to get ISP and ASN information
def get_isp_and_asn(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_whois()
        isp = result.get('asn_description', 'Unknown ISP')
        asn = result.get('asn', 'Unknown ASN')
        return isp, asn
    except Exception as e:
        return "Error retrieving ISP/ASN", str(e)

# Function to get the IP location (existing function)
def get_ip_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        return response.json()
    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve data: {e}")
        return None

# Function to show map and display ISP/ASN information
def show_map():
    ip = entry.get()
    location_data = get_ip_location(ip)
    
    # Get ISP and ASN details
    isp, asn = get_isp_and_asn(ip)

    if location_data and location_data['status'] == 'success':
        lat = location_data['lat']
        lon = location_data['lon']
        location_name = location_data['city'] + ', ' + location_data['country']

        # Display ISP and ASN information
        messagebox.showinfo("IP Information", f"IP: {ip}\nLocation: {location_name}\nISP: {isp}\nASN: {asn}")

        # Create a map centered around the IP's location
        map_ = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], tooltip=location_name).add_to(map_)
        
        # Save the map to an HTML file
        map_file = 'ip_location_map.html'
        map_.save(map_file)

        # Open the map in the default web browser
        os.startfile(map_file)
    else:
        messagebox.showerror("Error", "Invalid IP address or unable to retrieve location.")

# Create the main window
root = tk.Tk()
root.title("IP Address Locator")

# Create and place the entry widget
label = tk.Label(root, text="Enter IP Address:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create and place the button
button = tk.Button(root, text="Show Location on Map", command=show_map)
button.pack(pady=20)

# Run the application
root.mainloop()