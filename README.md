# Educational Keylogging Demonstration (Controlled Lab)

## ⚠️ IMPORTANT ETHICAL & LEGAL NOTICE

This project is created **strictly for educational purposes** in a **controlled laboratory environment**.

- ✔ All systems involved must be **owned by the user** or used with **explicit written permission**
- ✔ Intended for **cybersecurity education**, malware analysis, and defensive awareness
- ❌ Must NOT be used on personal devices, public networks, or systems without consent
- ❌ Any misuse of this project may be illegal and unethical

The author assumes **no responsibility** for misuse.

---

## 📘 Project Overview

This project demonstrates how **keylogging techniques work at a conceptual level** for cybersecurity education.

The script records keyboard events on a test system and periodically reports collected data to a configured email address.  
Its purpose is to help students understand:

- How input events can be intercepted at the OS level
- Why endpoint security and permissions matter
- How malicious software operates internally
- How such activity can be detected and mitigated

This project is designed for **offline, isolated lab environments only**.

---

## 🧠 Educational Objectives

- Understand keyboard event listeners in operating systems
- Observe background execution using threading
- Study data aggregation and timed reporting
- Analyze risks associated with input interception
- Learn defensive strategies against spyware and keyloggers

---

## 🧩 How It Works (High-Level)

- Uses a keyboard event listener to detect key presses
- Stores captured input in memory
- Resets the buffer at fixed time intervals
- Sends the collected data to a predefined email address
- Runs continuously until manually terminated

> **Note:** This project is for *demonstration*, not stealth or persistence research.

### 1. Running keylogger in victim Kali Linux
<img width="1222" height="578" alt="Screenshot_২০২৬০২০৯_১৪৪১১৩" src="https://github.com/user-attachments/assets/29569884-ccb0-434f-8b14-9010f8d7d4a1" />


 ### 2. Received email after 120 seconds with the log  
<img width="1225" height="413" alt="Screenshot_২০২৬০২০৯_১৪৪১৫১" src="https://github.com/user-attachments/assets/50f88a95-82cd-4edb-984c-1f74eb6abdfe" />
  

---

## 🛠 Environment

- **OS:** Kali Linux (Lab VM)
- **Language:** Python 3
- **Libraries:** `pynput`, `threading`, `smtplib`
- **Network:** Isolated / non-internet-facing lab network

---

## ⚙️ Dependencies

Ensure Python 3 is available on the system:

```bash
sudo apt install python3
