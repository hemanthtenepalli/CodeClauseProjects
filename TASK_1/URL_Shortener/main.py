import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.title("URL Shortener")
root.configure(bg="#34495e")

url = StringVar()
url_address = StringVar()

def url_shortener():
    url_address_value = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address_value)
    url_address.set(url_short)

def copy_url():
    url_short = url_address.get()
    pyperclip.copy(url_short)

# Define the fonts and colors
title_font = ("Arial", 28, "bold")
label_font = ("Arial", 14)
button_font = ("Arial", 14, "bold")
entry_font = ("Arial", 12)

# Title label
title_label = Label(root, text="URL Shortener", font=title_font, fg="#fff", bg="#34495e", pady=40)
title_label.pack()

# Label for the created URL text
created_url_label = Label(root, text="It is a free tool to shorten URLs. Create short & memorable links in seconds", font=label_font, fg="#fff", bg="#34495e")
created_url_label.pack(pady=(10, 20))


# Entry field for the long URL
url_entry = Entry(root, textvariable=url, width=40, font=entry_font, bd=2, relief="solid")
url_entry.pack(pady=(0, 10))
url_entry.insert(0, "Enter your URL here")  # Placeholder text

# Button to generate short URL
shorten_button = Button(root, text="Generate Short URL", command=url_shortener, font=button_font, fg="#fff", bg="#3498db", padx=10, pady=5, bd=0, relief="solid")
shorten_button.pack(pady=10)

# Entry field to display short URL
short_url_entry = Entry(root, textvariable=url_address, width=40, font=entry_font, bd=2, relief="solid")
short_url_entry.pack(pady=10)

# Button to copy short URL
copy_button = Button(root, text="Copy URL", command=copy_url, font=button_font, fg="#fff", bg="#2ecc71", padx=10, pady=5, bd=0, relief="solid")
copy_button.pack(pady=10)



# Additional text
additional_text = """A FAST AND SIMPLE URL SHORTENER\n\n\nFree URL Shortener for transforming long, ugly links into nice, memorable and trackable \nshort URLs. Use it to shorten links for any social media platforms, blogs,\n SMS, emails, ads, or pretty much anywhere else you want to share them. \n\tTwitter, Facebook, YouTube, Instagram, WhatsApp, emails, SMS, videos.\n this is the best free alternative to generic URL shorteners like bitly and tinyurl."""
additional_label = Label(root, text=additional_text, font=label_font, fg="#fff", bg="#34495e", justify="center")
additional_label.pack(pady=20)


root.mainloop()

