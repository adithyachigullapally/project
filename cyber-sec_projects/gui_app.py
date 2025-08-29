import tkinter as tk
from malware_detect import check_keywords_file, load_keywords, check_processes

def run_scan():
    check_keywords_file()
    keywords = load_keywords()
    found = check_processes(keywords)
    output_box.delete("1.0", tk.END)
    if found:
        output_box.insert(tk.END, " Suspicious processes detected:\n")
        for pid, name, exe in found:
            output_box.insert(tk.END, f"PID: {pid}, Name: {name}, Path: {exe}\n")
    else:
        output_box.insert(tk.END, " No suspicious keylogger activity found.\n")

root = tk.Tk()
root.title("Keylogger Detector")

btn = tk.Button(root, text="Run Scan", command=run_scan)
btn.pack(pady=10)

output_box = tk.Text(root, height=15, width=60)
output_box.pack()

root.mainloop()
