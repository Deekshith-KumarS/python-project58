import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# Function to count the number of lines in a text file
def count_lines_in_file():
    # Open file dialog to choose a file
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    
    if file_path:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                num_lines = len(lines)
                
                # Display the result in a message box
                messagebox.showinfo("Line Count", f"The file contains {num_lines} lines.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create main window
root = tk.Tk()
root.title("NUMBER OF LINES IN A TEXT FILE")
root.configure(background='#0096DC')
text_label= tk.Label(root,text='HELLO DEEKSHITH')
text_label.pack()
text_label.config(font=('verdana',24))
text_label.pack(pady=(10,10))



# Set window size
root.geometry("1000x1000")

# Create a button to select a file and count lines
count_button = tk.Button(root, text="CLICK THIS BUTTON TO FIND NUMBER OF LINES IN A TEXT", command=count_lines_in_file)
count_button.pack(pady=200)

# Run the Tkinter event loop
root.mainloop()