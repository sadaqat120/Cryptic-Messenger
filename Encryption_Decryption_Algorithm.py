import random
import string
import tkinter as tk
from tkinter import messagebox

Key=[
    ['Y', ')', 'e', '~', '.', '$', 'O', 6, 'R', '=', 'S', '(', 'J', 0, 'u', 7, '>', 'A', 'z', 'r', 'K', 'H', 'I', 1, 's', '^', 'P', 'g', 'n', 5, 'l', '?', 'W', 'x', '\\', 'Q', 'L', 'M', '*', ':', 'E', 'D', 'f', '@', '|', 'U', '{', 'k', 'b', '+', 2, 'C', 'o', 'V', 'Z', 'N', ']', ';', 'X', 8, ' ', 'v', 'y', '%', '!', 'c', '_', 4, '/', 'w', 'q', '&', '"', 'm', 'i', 'G', '#', '-', 'p', 'T', 'a', 't', 'h', '`', 'd', 'j', 9, 'B', '}', "'", 'F', 3, '<', '[', ','],
    ['<', ']', 'J', 0, 'h', 'O', '>', '(', '[', 'P', '%', 'j', '-', ' ', '"', 'o', 'b', '*', '!', 'l', '|', 'V', 'g', 'E', 6, 'H', ',', '#', '?', ':', 'Z', 'B', ';', "'", 'w', 5, 'z', 'n', 'U', 'G', 'q', 'W', 'F', 'a', 'm', 'v', 3, 4, 'u', 'X', '\\', 'T', 'd', 'L', 'N', 'x', '~', '@', 'K', 'I', 'S', 'y', ')', 't', 'r', 'Y', 'k', 'C', 'f', 'e', 7, '/', '&', 'p', 'Q', 'A', 1, 'R', 's', 'c', 8, '`', 9, '{', '+', '^', '$', 'M', 'D', '=', 'i', '}', '.', 2, '_'],
    ['"', 'B', '@', 'u', 'k', 'S', 3, '!', '_', 'o', 5, 'A', 8, '%', 'U', 0, ':', 'z', 1, 'O', '\\', 't', 'N', '<', 'K', 'p', '-', 7, 'Y', 'm', '`', 'H', 'I', 'g', 'e', "'", '$', 'h', '&', ']', '~', '*', '>', ',', ' ', 'n', 6, ';', '(', 'v', 'w', '^', 'r', 'C', 2, 'W', '|', ')', '{', '}', 'F', 'a', 'j', 'c', 'f', '?', 'P', 'Q', 9, 'D', 'J', 'Z', 'i', 'y', 'X', 'b', '[', 'R', 'G', 'q', 's', 'x', 4, 'V', '=', 'T', 'M', '/', 'd', 'L', 'E', '.', '+', '#', 'l'],
    [')', 'Y', 2, "'", 'B', 'U', '$', 'F', '\\', 'u', 'M', '(', 'a', ']', 's', 8, '+', 'O', 'v', 'z', 'm', '^', 'I', 'k', 5, ' ', ';', '|', 'y', 'n', 'E', '#', 'A', 'r', 'o', 'l', 'V', '.', ':', 7, 'Q', '/', 'S', 'j', '-', 'D', '!', 'h', 'b', 9, 4, 'e', 'H', 'T', '>', 'K', 'P', 'c', 'R', '}', 'J', '%', ',', '*', 'f', 'X', 0, '_', 'q', 'w', '?', 'i', 'C', 'L', '@', 3, 't', 6, 'p', '<', '=', '&', 'N', 'Z', 'd', '`', 'x', '~', '[', 'g', '"', 'W', 'G', '{', 1],
    ['u', '(', '?', '[', '}', 5, '>', 'M', 'c', ';', 'Q', 'I', 'k', 'O', 'v', 'h', '_', 4, 'm', '"', '~', 'w', '#', 'p', 'z', "'", '|', '!', 1, 'd', '+', 't', '%', 'U', '$', '*', '/', 'x', 'G', 'L', 'g', ':', 's', ']', 'Z', 7, 'a', 'e', 'A', 'T', 'F', '-', 'q', 'X', 'V', '`', 'r', 6, 'n', 'o', 9, 'P', 'E', '=', '.', '&', 'y', ',', 'i', 'l', 'W', 'R', '@', ')', '{', 'N', 'B', '\\', 'j', 0, '<', 'K', 'C', 3, 'H', 'J', 'S', 2, 8, 'f', ' ', 'b', '^', 'Y', 'D'],
    [4, '$', 'j', 'V', '_', '%', '{', 'v', 'U', ']', 's', 't', 'B', '/', 'O', 'q', '`', 'I', '>', 'e', '=', '+', 5, '*', 'o', '}', 'H', 'K', ' ', 'k', 0, 'A', ')', "'", '.', 'a', 'E', 'Z', 'C', 'c', 'Q', 'S', ';', 'g', '|', 'R', 2, 'n', 'f', '(', 9, 'u', 'm', 'b', '^', 'y', 'N', '\\', 'G', 'W', 'D', 'M', 1, '!', '-', 'X', ':', 'p', 'w', 'h', 7, '<', 'x', '@', '#', 'i', '?', 'z', 'l', '[', 6, '"', 8, 'd', ',', 'F', 'T', '~', 'J', 'Y', 'P', '&', 'L', 'r', 3],
    ['j', 'C', 5, 'o', 'y', 'n', '!', 3, '*', 7, 'a', ']', '\\', '{', '.', 'k', '}', 'w', 'N', '=', "'", 'M', '_', 'D', 'l', 's', 'r', 'I', 'W', 'g', 'F', 1, 9, 'E', 'd', 'Q', ')', 'B', 'L', 6, 't', 'c', '%', '/', 'R', 'Y', 'A', 8, 'O', '@', 'v', '#', 'm', 'H', 'U', '~', 'T', '|', 'P', 'h', 'S', '`', 'b', '+', 0, 'i', '-', '$', '^', '<', 'G', '>', 'K', ',', 'X', 2, 'f', 'Z', '[', 'p', '(', 4, 'z', ' ', 'e', 'q', '"', 'J', 'V', '&', 'u', ':', ';', '?', 'x'],
    ['`', 'X', 'd', 4, ')', '}', ';', 'C', '$', 'b', 't', 'f', 'z', 'c', 'm', 9, 'i', 'p', '&', '/', 'U', 'F', 0, '*', 'T', 'H', '-', '|', '^', '(', 'a', 'E', '<', '#', '"', 'P', 'q', ' ', '\\', '!', 7, 'I', 'J', 'l', 'k', 'Y', '=', 3, 'h', 'O', 6, 'x', '_', 'r', ':', ',', '@', 'V', '[', 'R', 'j', '.', 'B', '{', 'L', 'G', 'y', 'W', 'S', '~', 'N', 'n', '?', 'w', 'Z', 'Q', 'u', 1, 'A', ']', 'g', 'M', "'", 'v', 'o', 8, 5, '+', '%', 'K', '>', 'D', 's', 2, 'e'],
    ['a', 'm', '[', '+', 'p', ';', 'I', 6, 'f', '~', 'g', 'n', '-', 9, 'l', 'P', 'N', '%', 'X', 'r', '\\', '=', 5, 'L', '*', 'O', 'q', '}', 'V', 'Q', '`', 'o', 'Y', 'k', 4, 2, 'S', ' ', 'A', '"', '<', '|', 'Z', ']', 'M', 'R', '/', ',', 0, '?', ':', ')', "'", 's', 'u', '@', '$', 'i', '{', 'j', '^', 'x', '&', 'B', 3, 1, '#', 'd', 'w', 'K', 8, 'H', 'E', 'c', '_', 'T', '!', '(', 'G', 7, 'b', 'y', 'h', 'v', '>', 'D', '.', 't', 'W', 'J', 'F', 'z', 'e', 'C', 'U'],
    ['\\', 'Z', '*', '$', '+', 'O', ':', 'd', 'E', ']', '}', 'y', ' ', 'c', 'V', 'S', 'D', '{', 'b', 6, ',', 'z', 'P', ';', 'L', '^', 'k', 3, ')', 1, '(', 'l', 'M', 'Y', 'Q', 'R', 'H', '|', 'G', '&', '"', 'X', 'e', 'i', 'g', 8, 'I', "'", 'f', 'w', '<', 7, 'J', 'n', '%', '=', 'h', '!', '@', 'q', 'j', '?', 's', 0, 'U', '>', 'K', 'p', '/', 'v', 'a', 'r', 4, '-', 'N', '_', '[', 'C', 2, 5, 'u', 't', 'F', '#', '~', 9, '.', 'm', '`', 'W', 'x', 'o', 'T', 'A', 'B']
]

def encrypt(message, key):
    
    message_length=len(message)
    key_length=len(key)
    encrypted_message = ""
    
    random_key=random.randrange(key_length)
    key_list_for_keyNumber=key[message_length%key_length]
    find_keyNumber_from_lengthBasedList=key_list_for_keyNumber.index(random_key)
    encrypted_message += str(key_list_for_keyNumber[(find_keyNumber_from_lengthBasedList+message_length)%len(key_list_for_keyNumber)])
    
    characters = string.ascii_letters + string.digits
    encrypted_message += str(''.join(random.choice(characters) for _ in range(2)))
    
    if message_length<10:
        message_number=1
        index_for_messageLength=key[key_length-1].index(message_length)
        encrypted_message += str(key[key_length-1][(index_for_messageLength+5)%len(key[key_length-1])])
    
    else:
        
        if message_length <99:
            message_number=2
        
        elif message_length<999:
            message_number=3
        
        message_length=str(message_length)
        for keyword in message_length:
            try:
                keyword=int(keyword)
            except:
                pass
            index_for_messageLength=key[key_length-1].index(keyword)
            encrypted_message += str(key[key_length-1][(index_for_messageLength+5)%len(key[key_length-1])])
        
    
    key_list_for_encryption=key[random_key]
    for keyword in message:
        try:
            keyword=int(keyword)
        except:
            pass
        message_index=key_list_for_encryption.index(keyword)
        encrypted_message += str(key_list_for_encryption[(message_index+int(message_length))%len(key_list_for_encryption)])
    
    characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    encrypted_message += str(''.join(random.choice(characters) for _ in range(int(message_length))))
        
    index_for_messageNumber=key[0].index(message_number)
    encrypted_message += str(key[0][(index_for_messageNumber+5)%len(key[0])])

    return encrypted_message

def decrypt(encrypted_message, key):
    
    key_length=len(key)
    decrypted_message = ""
    
    splitted_message = encrypted_message.split()
    message_numbers= splitted_message[-1]
    try:
        index_for_messageNumber=key[0].index(message_numbers[-1])
        messageNumber = int(key[0][(index_for_messageNumber-5)%len(key[0])])
    except:
        return "This message is not encrypted from our Cryptic Messenger !"

    flag=True
    count2_for_random=2
    message_length= ""
    for keyword in encrypted_message:
        
        try:
            keyword=int(keyword)
        except:
            pass
        
        if flag is True:
            key_list=keyword
            flag=False
        
        elif count2_for_random>0:
            count2_for_random-=1
        
        elif messageNumber>0:
            index_for_messageLength=key[key_length-1].index(keyword)
            message_length += str(key[key_length-1][(index_for_messageLength-5)%len(key[key_length-1])])
            messageNumber-=1
        
        else:
            
            if flag is False:
                try:
                    message_length=int(message_length)
                except:
                    return "This message is not encrypted from our Cryptic Messenger !"
                key_list_for_keyNumber=key[message_length%key_length]
                find_keyNumber_from_lengthBasedList=key_list_for_keyNumber.index(key_list)
                encrypted_key_listIndex = str(key_list_for_keyNumber[(find_keyNumber_from_lengthBasedList-message_length)
                                                                     %len(key_list_for_keyNumber)])
                encrypted_key_listIndex = int(encrypted_key_listIndex)
                temporary_message_length=message_length
                flag=0    
            
            if temporary_message_length>0:
                key_list_for_encryption=key[encrypted_key_listIndex]
                message_index=key_list_for_encryption.index(keyword)
                decrypted_message += str(key_list_for_encryption[(message_index-message_length)%len(key_list_for_encryption)])
                temporary_message_length-=1     
    return decrypted_message


# Get user input
# original_message = input("Enter your message: ")

# # Print results

# # Encrypt the message
# encrypted_message = encrypt(original_message, Key)
# print("-----------------------------------------------")
# print("Encrypted Message: ", encrypted_message)
# print("-----------------------------------------------")
# # Decrypt the message
# decrypted_message = decrypt(encrypted_message, Key)
# print("Decrypted Message: ", decrypted_message)
# print("-----------------------------------------------")


def main():
    def encrypt_message():
        user_input = input_entry.get()
        if not user_input:
            messagebox.showwarning("Warning", "Please enter a message to encrypt!")
            return
        if len(user_input) > 999:
            messagebox.showerror("Error", "Message too long! Maximum length is 999 characters.")
            return
        
        filtered_input = "".join(c for c in user_input if c.isprintable())  # Remove unsupported characters

        encrypted_text = encrypt(filtered_input, Key)
        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, encrypted_text)
        result_textbox.config(state=tk.DISABLED)

    def decrypt_message():
        user_input = input_entry.get()
        if not user_input:
            messagebox.showwarning("Warning", "Please enter an encrypted message to decrypt!")
            return
        
        if len(user_input) > 999:
            messagebox.showerror("Error", "Message too long! Maximum length is 999 characters.")
            return
        
        filtered_input = "".join(c for c in user_input if c.isprintable())  # Remove unsupported characters
        
        decrypted_text = decrypt(filtered_input, Key)
        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, decrypted_text)
        result_textbox.config(state=tk.DISABLED)

    def copy_to_clipboard():
        result_text = result_textbox.get("1.0", tk.END).strip()
        if result_text:
            root.clipboard_clear()
            root.clipboard_append(result_text)
            root.update()
            messagebox.showinfo("Copied", "Message copied to clipboard!")

    def clear_input():
        input_entry.delete(0, tk.END)
        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete("1.0", tk.END)
        result_textbox.config(state=tk.DISABLED)

    # Create Main Window
    root = tk.Tk()
    root.title("Cryptic Messenger")
    root.geometry("500x450")
    root.configure(bg="#282c34")

    # Heading Label
    title_label = tk.Label(root, text="🔒 Cryptic Messenger 🔒", font=("Arial", 16, "bold"), fg="white", bg="#282c34")
    title_label.pack(pady=10)

    # Input Field
    input_entry = tk.Entry(root, font=("Arial", 14), width=40, bd=2)
    input_entry.pack(pady=10)

    # Encrypt & Decrypt Buttons
    button_frame = tk.Frame(root, bg="#282c34")
    button_frame.pack()

    encrypt_button = tk.Button(button_frame, text="Encrypt", font=("Arial", 12, "bold"), command=encrypt_message, bg="#4CAF50", fg="white", padx=20, pady=5)
    encrypt_button.grid(row=0, column=0, padx=10)

    decrypt_button = tk.Button(button_frame, text="Decrypt", font=("Arial", 12, "bold"), command=decrypt_message, bg="#f44336", fg="white", padx=20, pady=5)
    decrypt_button.grid(row=0, column=1, padx=10)

    # Result Text Box (for copyable text)
    result_textbox = tk.Text(root, font=("Arial", 12), height=4, width=50, wrap="word", state=tk.DISABLED)
    result_textbox.pack(pady=10)

    # Copy to Clipboard Button
    copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), command=copy_to_clipboard, bg="#2196F3", fg="white", padx=10, pady=5)
    copy_button.pack()

    # Exit Button
    exit_button = tk.Button(root, text="Exit", font=("Arial", 12, "bold"), command=root.quit, bg="#ff9800", fg="white", padx=20, pady=5)
    exit_button.pack(side="bottom", pady=10)

    root.mainloop()

# Run the main function
if __name__ == "__main__":
    main()
