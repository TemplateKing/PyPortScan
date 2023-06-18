import socket
import threading
import tkinter as tk
from PIL import Image, ImageTk

results = {}  # Dictionary to store scanning results

def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second

        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))

        # Check if the connection was successful
        if result == 0:
            results[port] = f"Port {port} is open"
        else:
            results[port] = f"Port {port} is closed"

        # Close the socket
        sock.close()
    except socket.error:
        results[port] = f"Could not connect to {host}:{port}"

def port_scan():
    host = entry_host.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())

    # Clear previous output
    text.delete("1.0", tk.END)
    results.clear()

    # Start scanning ports
    text.insert(tk.END, f"Scanning ports on {host}...\n\n")
    for port in range(start_port, end_port + 1):
        # Create a new thread for each port scan
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()

    # Wait for all threads to complete
    for thread in threading.enumerate():
        if thread != threading.main_thread():
            thread.join()

    # Display results in sorted order
    for port, result in sorted(results.items()):
        if "closed" in result.lower():
            text.insert(tk.END, result + "\n", "closed")
        else:
            text.insert(tk.END, result + "\n", "open")

# Create the GUI
root = tk.Tk()
root.title("PyPortScan")

# Calculate window position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 700
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Set window icon
icon_image = Image.open("icon.ico")
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

# Title Label
title_label = tk.Label(root, text="PyPortScan", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Host Input
label_host = tk.Label(root, text="IP Address:")
label_host.pack()
entry_host = tk.Entry(root)
entry_host.pack()

# Port Range Input
label_ports = tk.Label(root, text="Port Range:")
label_ports.pack()
entry_start_port = tk.Entry(root)
entry_start_port.pack()
entry_end_port = tk.Entry(root)
entry_end_port.pack()

# Scan Button
btn_scan = tk.Button(root, text="Scan Ports", command=port_scan)
btn_scan.pack()

# Output Text
text = tk.Text(root)
text.pack()

# Configure text tag colors
text.tag_configure("open", foreground="green")
text.tag_configure("closed", foreground="dark red")

# Run the GUI
root.mainloop()

#########################################
#                                       #
#   Please join my discord community:   #
#    https://discord.gg/QKJPfpaFUk      #
#                                       #
#########################################