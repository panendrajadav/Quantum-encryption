# ⚛️ Quantum Encryption for Blockchain Security

This project demonstrates **quantum-based encryption and decryption** designed to enhance **blockchain transaction security**.  
The main implementation is written in **Python using Streamlit and Qiskit**, while a **Q# file** is created separately to represent the **quantum logic only** for educational and logical demonstration purposes.

It generates a **quantum random key** using qubits in superposition and uses it to **encrypt and decrypt wallet addresses and transaction IDs** via a simple **XOR cipher**.


## 🧠 Overview

- **Languages:** Python (Streamlit + Qiskit), Q# (Logic Demonstration)
- **Python Version Required:** 3.9 – 3.11  
- **Purpose:** Secure blockchain wallet and transaction data using quantum-generated keys  
- **Concept:** Quantum randomness ensures each encryption key is unique and unpredictable


## 🔑 Features

- Quantum random key generation using **Hadamard gates**  
- XOR-based **encryption and decryption** for wallet and transaction data  
- Streamlit-based web interface for user interaction  
- Q# file demonstrates the same **quantum logic** in Microsoft QDK  
- Real-world blockchain use case for **wallet data encryption**


## 🧩 How It Works

1. **Quantum Key Generation:**  
   Qubits are initialized, placed in superposition using Hadamard gates, and measured to produce random bits.

2. **Encryption:**  
   Each character of the wallet address or transaction ID is XORed with the generated quantum key bits.

3. **Decryption:**  
   The same quantum key is reused to retrieve the original data (XOR is symmetric).

4. **Integration:**  
   The encrypted values can be stored securely in blockchain systems, ensuring privacy and traceability.


## 🚀 Run the Python (Streamlit) Code

### Prerequisites
- Python **3.9 – 3.11**
- Install required libraries:

# In bash
pip install streamlit qiskit pyperclip

# Clone this repository
git clone https://github.com/panendrajadav/Quantum-encryption
cd Quantum-encryption

# Run the Streamlit app
streamlit run app.py

