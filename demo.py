# -------------------------------
# Quantum Key Generation + Encryption Demo
# -------------------------------
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# -------------------------------
# Step 1: Quantum Key Generator (Hadamard-based)
# -------------------------------
def generate_quantum_key(bits=8):
    """Generate an 8-bit quantum key using Hadamard gates"""
    qc = QuantumCircuit(bits, bits)
    qc.h(range(bits))            # Apply Hadamard gate to each qubit
    qc.measure(range(bits), range(bits))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()

    counts = result.get_counts(qc)
    bitstring = list(counts.keys())[0]
    return [int(b) for b in bitstring[::-1]]  # reverse to match classical order

# -------------------------------
# Step 2: Simple XOR Encryption/Decryption
# -------------------------------
def encrypt_8bit(data: str, key: list):
    key_str = ''.join(map(str, key))
    encrypted = ''.join(chr(ord(c) ^ int(key_str[i % len(key_str)])) for i, c in enumerate(data))
    return encrypted

def decrypt_8bit(encrypted: str, key: list):
    key_str = ''.join(map(str, key))
    decrypted = ''.join(chr(ord(c) ^ int(key_str[i % len(key_str)])) for i, c in enumerate(encrypted))
    return decrypted

# -------------------------------
# Step 3: Example Usage
# -------------------------------
wallet_address = "Varun loves AI"
transaction_id = "Ai is "

# Generate Quantum Key
quantum_key = generate_quantum_key()
print("🔑 Quantum 8-bit Key:", quantum_key)

# Encrypt Data
encrypted_wallet = encrypt_8bit(wallet_address, quantum_key)
encrypted_txn = encrypt_8bit(transaction_id, quantum_key)

# Decrypt Data
decrypted_wallet = decrypt_8bit(encrypted_wallet, quantum_key)
decrypted_txn = decrypt_8bit(encrypted_txn, quantum_key)

# -------------------------------
# Step 4: Display Results
# -------------------------------
print("\n--- Encryption Results ---")
print("Original Wallet Address:", wallet_address)
print("Encrypted Wallet Address:", encrypted_wallet)
print("Decrypted Wallet Address:", decrypted_wallet)

print("\nOriginal Transaction ID:", transaction_id)
print("Encrypted Transaction ID:", encrypted_txn)
print("Decrypted Transaction ID:", decrypted_txn)
