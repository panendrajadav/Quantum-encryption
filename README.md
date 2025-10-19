# ⚛️ Quantum Encryption for Blockchain Security

This project demonstrates **quantum-based encryption and decryption** using **Q#**, designed to enhance **blockchain transaction security**.  
It generates a **quantum random key** using qubits in superposition and uses it to **encrypt and decrypt wallet addresses and transaction IDs** via a simple **XOR cipher**.


## 🧠 Overview

- **Language:** Q# (Microsoft Quantum Development Kit)  
- **Purpose:** Secure blockchain wallet and transaction data using quantum-generated keys  
- **Concept:** Quantum randomness ensures each encryption key is unique and unpredictable


## 🔑 Features

- Quantum random key generation using **Hadamard gates**  
- XOR-based **encryption and decryption** of text data  
- Demonstrates how **quantum security** can be applied to blockchain systems  
- Simple and easy-to-understand example for learning Q#


## 🧩 How It Works

1. **Quantum Key Generation:**  
   Qubits are initialized, placed in superposition using the Hadamard gate, and then measured to produce random bits.

2. **Encryption:**  
   Each character of the wallet or transaction string is XORed with the generated quantum key bits.

3. **Decryption:**  
   The same quantum key is reused to recover the original data (since XOR is symmetric).



## 🚀 Run the Code

### Prerequisites
- [Microsoft Quantum Development Kit](https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk)
- Visual Studio Code or Visual Studio with Q# extension

### Steps
# Clone this repository
git clone https://github.com/yourusername/QuantumEncryption-QSharp.git
cd QuantumEncryption-QSharp

# Run the Q# program
dotnet run
