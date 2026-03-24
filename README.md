# 🎹 Synthesia Unlocker 1.0

A simple bypassing tool built for Synthesia  with Python that interacts with local Synthesia files and provides a quick one-click unlock action through a very simple UI.

---

## 📸 Preview

Minimal interface with:

* Title text
* One button
* Lightweight window
* Real-time geometry logging

---

## ⚙️ Features

* ✔️ Unlocks the full paid version synthesia just with one click.
* ✔️ Performs automated file operations inside the Synthesia directory
* ✔️ Fast operation and delivery.
* ✔️ Real-time window geometry logging (debugging purpose)

---

## 📁 Project Structure

```
synthesia-unlocker/
│
├── main.py        # App entry point
├── ui.py               # UI layout and widgets
├── core.py         # Main logic (check, inject, etc.)
├── utils.py          # Shared variables and effects
└── requirements.txt , README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/randornc0der/synthesia-tooler.git
cd synthesia-unlocker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

Then:

1. Click the **"Unlock Synthesia"** button
2. Wait for the Success message 
3. Restart  Synthesia
4. Enjoy using the paid features

     

---

## ⚠️ Requirements

* Python (3.9 or higher) 
* Windows OS (uses Windows shell commands)
* Have any Synthesia version (recommended 10.9)
* Synthesia installed in:

```
%APPDATA%\Roaming\Synthesia
```

---

## ❗ Notes

* The app will exit if Synthesia is not detected
* Make sure you have proper permissions to modify files in the directory

---

## 🛠 Built With

* PySide6 (Qt for Python)
* Python standard libraries
* pymsgbox

##
