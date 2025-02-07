# Elevator Simulation using A* Algorithm

This project implements an **elevator control system simulation** using the **A* search algorithm** to optimize elevator movement. The system prioritizes **minimizing wait times** for users and **reducing energy consumption**.

## 📌 Project Overview
Most **multi-elevator systems** operate independently, leading to **inefficiencies**. This project introduces a **centralized decision-making system** that:
- Assigns the **nearest elevator** to each request.
- Reduces **waiting times** for users.
- Minimizes **unnecessary elevator movements** to save energy.

The project consists of a **Python-based simulation** with a simple **graphical user interface (GUI)**.

---

## 🏗️ Project Structure
- `.gitignore` → Specifies ignored files (e.g., cache, logs).
- `requierments.txt` → Dependencies for running the project.
- `State.py` → Defines the **elevator system state** and implements the **A* search algorithm**.
- `UI.py` → Implements a **basic graphical interface** for the simulation.
- `گزارش.pdf` → Project report in **Persian**, detailing the methodology and implementation.
- `گزارش.docx` → Editable version of the project report.
- `__pycache__/` → Compiled Python cache files.

---

## 🔍 How It Works
The system models **elevator movement** in a building using a **state-based approach**:
- **`State.py`**: Defines different states of the system and implements **A* search** to find the optimal elevator movement.
- **`UI.py`**: Allows users to interact with the system, request elevators, and observe their movement.

### **Key Functions in `State.py`**
- **`__init__`** → Initializes the system with the number of floors and elevators.
- **`add_floor()`** → Adds a floor request to the queue.
- **`doit(action)`** → Executes a movement (UP, DOWN, STOP) based on the current state.
- **`transition(actions)`** → Generates a new state after applying actions.
- **`cost()`** → Calculates the cost of a state (based on waiting time and elevator movement).
- **`actions()`** → Determines the possible actions for a given state.
- **`decision()`** → Chooses the best action using A* search.

---

## 🚀 Running the Simulation
### **1️⃣ Run the Python Code**
1. Install dependencies:
   ```bash
   pip install -r requierments.txt
   ```
2. Run the simulation:
   ```bash
   python UI.py
   ```
3. Enter the **number of floors** and **elevators**.
4. Use the **UI buttons** to request an elevator and simulate movement.

### **2️⃣ Running the Executable**
If you don’t have Python installed, you can use the pre-built executable:
1. Open `ElevatorSimulation.exe`.
2. Use the UI to request elevators and observe the simulation.

---

## 📜 Report & Documentation
For a detailed explanation of the project, refer to:
- **`گزارش.pdf`** (Persian) – Complete project report.
- **`گزارش.docx`** – Editable report version.

---

## 🏗️ Future Improvements
- **Implement machine learning** to optimize elevator movement further.
- **Enhance the GUI** with real-time visual feedback.
- **Support multi-building systems** for large-scale simulations.

---

## 📧 Contact
For any questions or contributions, feel free to reach out.

---

📌 **Developed for the Summer 1402 AI Project, University of Tehran**