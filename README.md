# 🔒 Advanced Random Password Generator

A sleek **password generator app** built using **Python** and **Tkinter**, featuring customization, security, and instant clipboard access.

---

## ✨ Features

* 🔐 **Customizable Length** — Choose any password size
* 🔠 **Character Options** — Uppercase, lowercase, digits & symbols
* 🧩 **Smart Complexity** — Ensures one of each selected type
* ⚡ **One-click Copy** — Instantly copy password to clipboard
* 🌙 **Modern Dark Theme** — Simple and elegant UI

---

## ⚙️ Requirements

* Python 3.7+
* Tkinter (pre-installed with Python)
* Pyperclip

  ```bash
  pip install pyperclip
  ```

---

## 🚀 Run the App

```bash
python Randompasswordgenerator.py
```

---

## 🧠 Password Logic

```
Includes random mix of:
- Uppercase Letters (A–Z)
- Lowercase Letters (a–z)
- Numbers (0–9)
- Symbols (!@#$%^&*)
```

💡 *At least one character from each selected type is guaranteed for stronger security!*

---

## 🖥️ GUI Overview

* Title: “🔒 Random Password Generator”
* Size: 400×400
* Theme: Dark (`#1c1c1c`)
* Buttons:

  * Generate → Blue (`#0078D7`)
  * Copy → Green (`#28A745`)
* Font: Arial / Consolas

---

## 📋 App Interface

```
🔒 Random Password Generator
----------------------------
Enter Password Length: [   12   ]

☑ Include Uppercase (A-Z)
☑ Include Lowercase (a-z)
☑ Include Numbers (0-9)
☐ Include Symbols (!@#...)

[ Generate Password ]
[ Copy to Clipboard ]
```

---

## 🧩 Example Output

```
Generated Password:  T9!aRk3GzP
```

📋 *Password copied to clipboard automatically!*

---

## 🛡️ Validation & Errors

* Invalid or empty length input
* Password length < 4
* No character type selected
* Empty clipboard request

---

## 📂 Project Files

```
Randompasswordgenerator.py   # Main app
README.md                    # Documentation
```

