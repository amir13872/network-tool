from tkinter import Tk, Frame, Button, Label, Text, Scrollbar, END, messagebox
import subprocess
import threading

class NetworkToolGUI:
    def __init__(self, master):
        self.master = master
        master.title("Network Tool")

        self.frame = Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.label = Label(self.frame, text="Network Operations")
        self.label.pack()

        self.arp_button = Button(self.frame, text="View ARP Table", command=self.view_arp_table)
        self.arp_button.pack(pady=5)

        self.ping_button = Button(self.frame, text="Ping", command=self.ping)
        self.ping_button.pack(pady=5)

        self.netsh_button = Button(self.frame, text="Show Network Config", command=self.show_network_config)
        self.netsh_button.pack(pady=5)

        self.netbios_button = Button(self.frame, text="Scan NetBIOS", command=self.scan_netbios)
        self.netbios_button.pack(pady=5)

        self.result_text = Text(self.frame, height=15, width=50)
        self.result_text.pack(pady=5)

        self.scrollbar = Scrollbar(self.frame, command=self.result_text.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.result_text.config(yscrollcommand=self.scrollbar.set)

    def view_arp_table(self):
        self.execute_command("arp -a")

    def ping(self):
        ip = "8.8.8.8"  # Example IP
        self.execute_command(f"ping {ip}")

    def show_network_config(self):
        self.execute_command("ipconfig" if self.is_windows() else "ifconfig")

    def scan_netbios(self):
        self.execute_command("nbtstat -n")

    def execute_command(self, command):
        threading.Thread(target=self.run_command, args=(command,)).start()

    def run_command(self, command):
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            self.display_result(result)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Command failed: {e}")

    def display_result(self, result):
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, result)

    def is_windows(self):
        return subprocess.run("uname", shell=True, stdout=subprocess.PIPE).stdout.decode().strip() == "Linux"

if __name__ == "__main__":
    root = Tk()
    gui = NetworkToolGUI(root)
    root.mainloop()