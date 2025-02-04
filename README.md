# 🐔 Word Classification Game 🎮

A **Tkinter-based educational game** where users drag and drop words into the correct categories (Noun/Adjective). The game supports **multiple levels**, **progress tracking**, and a **login system**.

---

## 📌 Features
✅ **Drag & Drop Interface** – Move words into the correct boxes.  
✅ **6 Levels** – Unlock levels progressively.  
✅ **User Login** – Saves game progress in SQLite.  
✅ **Dynamic Word Lists** – Words change per level.  
✅ **Visual Feedback** – Color-coded word categories.  

---

## 📂 Project Structure
```
WordGameApp/
│── backend/
│   ├── database.py      # Handles user login & progress storage
│   ├── game_logic.py    # Checks word classification logic
│── frontend/
│   ├── main.py          # Main Tkinter GUI application
│   ├── drag_drop.py     # Implements drag-and-drop feature
│   ├── assets/
│   │   ├── hen.png      # Hen image for game
│   │   ├── words.json   # Level-wise word categorization
│── config/
│   ├── settings.py      # Stores UI settings (colors, sizes)
│── docs/
│   ├── uml.puml         # UML Diagram for the game architecture
│── requirements.txt
│── README.md
│── Dockerfile (optional)
```

---

## 🔧 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/WordGameApp.git
cd WordGameApp
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```sh
python frontend/main.py
```

---

## 🛠 Configuration
Modify **`config/settings.py`** to change:
- Background colors (`BG_COLOR`, `ADJ_COLOR`, `NOUN_COLOR`)
- Window size (`WINDOW_WIDTH`, `WINDOW_HEIGHT`)
- Database file (`DATABASE_NAME`)

---

## 🎮 How to Play
1. **Login with a username**.
2. **Select an unlocked level**.
3. **Drag words into the correct box**:
   - **Adjective Box** (🔵 Light Blue)
   - **Noun Box** (🟢 Light Green)
4. **Click "Check Answers"** to validate.
5. **Unlock higher levels** when the previous is completed.

---

## 📦 Word Data (`words.json`)
Example JSON format:
```json
{
    "1": {
        "adjective": ["big", "small"],
        "noun": ["hen", "egg"]
    },
    "2": {
        "adjective": ["red", "soft"],
        "noun": ["apple", "cotton"]
    }
}
```

---

## 📌 UML Diagram
Generated using **PlantUML** (`docs/uml.puml`):  
![UML Diagram](docs/uml.png)

---

## 📝 Future Enhancements
🚀 Add **sound effects** for correct/incorrect answers.  
🎭 Include **animations** for dragging words.  
🏆 Implement **leaderboards** for tracking high scores.  

---

## 📜 License
TBD


