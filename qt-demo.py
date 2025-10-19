import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import pyperclip

# -------------------------------
# Quantum Key Generation
# -------------------------------
def generate_quantum_key(bits=8):
    """Generate 8-bit key using Hadamard gates and measurement"""
    qc = QuantumCircuit(bits, bits)
    qc.h(range(bits))
    qc.measure(range(bits), range(bits))

    simulator = AerSimulator()
    job = simulator.run(qc)
    result = job.result()
    counts = result.get_counts(qc)

    key_str = list(counts.keys())[0]
    key_bits = [int(b) for b in key_str[::-1]]
    return key_bits

# -------------------------------
# XOR Encryption / Decryption
# -------------------------------
def xor_encrypt(data: str, key: list):
    key_str = ''.join(map(str, key))
    return ''.join(chr(ord(c) ^ int(key_str[i % len(key_str)])) for i, c in enumerate(data))

def xor_decrypt(encrypted: str, key: list):
    key_str = ''.join(map(str, key))
    return ''.join(chr(ord(c) ^ int(key_str[i % len(key_str)])) for i, c in enumerate(encrypted))

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Quantum Encryption Demo", page_icon="⚛️", layout="centered")
st.title("⚛️ Quantum Encryption Demo")
st.caption("Encrypt & Decrypt Wallet/Transaction with Quantum Key (Qiskit)")

# -------------------------------
# Scrollable Sections
# -------------------------------
encrypt_expander = st.expander("🔐 Encryption Section", expanded=True)
decrypt_expander = st.expander("🔓 Decryption Section", expanded=True)

# -------------------------------
# Encryption Section
# -------------------------------
with encrypt_expander:
    st.subheader("Encrypt Wallet & Transaction")
    wallet_address = st.text_input("Enter Wallet Address", key="enc_wallet")
    transaction_id = st.text_input("Enter Transaction ID", key="enc_txn")

    if st.button("Generate Quantum Key & Encrypt", key="encrypt_btn"):
        if wallet_address and transaction_id:
            quantum_key = generate_quantum_key()
            encrypted_wallet = xor_encrypt(wallet_address, quantum_key)
            encrypted_txn = xor_encrypt(transaction_id, quantum_key)

            st.success("✅ Encryption Done")
            st.text("Quantum Key (8-bit): " + str(quantum_key))

            st.text_input("Encrypted Wallet Address", encrypted_wallet, disabled=True, key="enc_wallet_out")
            if st.button("Copy Wallet Encrypted Value", key="copy_wallet_enc"):
                pyperclip.copy(encrypted_wallet)
                st.toast("Copied Wallet Encrypted Value!")

            st.text_input("Encrypted Transaction ID", encrypted_txn, disabled=True, key="enc_txn_out")
            if st.button("Copy Transaction Encrypted Value", key="copy_txn_enc"):
                pyperclip.copy(encrypted_txn)
                st.toast("Copied Transaction Encrypted Value!")

            # Auto-save encrypted values into session so decryption fields are populated
            st.session_state["quantum_key"] = quantum_key
            st.session_state["dec_wallet_input"] = encrypted_wallet
            st.session_state["dec_txn_input"] = encrypted_txn
        else:
            st.warning("Enter both Wallet and Transaction ID")

# -------------------------------
# Decryption Section
# -------------------------------
with decrypt_expander:
    st.subheader("Decrypt Data")

    # Initialize session keys if missing (avoid passing value= when key exists)
    if "dec_wallet_input" not in st.session_state:
        st.session_state["dec_wallet_input"] = ""
    if "dec_txn_input" not in st.session_state:
        st.session_state["dec_txn_input"] = ""

    # Input encrypted values for decryption (auto-filled from session if available)
    encrypted_wallet_input = st.text_area(
        "Paste Encrypted Wallet Value",
        key="dec_wallet_input",
        height=80
    )
    encrypted_txn_input = st.text_area(
        "Paste Encrypted Transaction Value",
        key="dec_txn_input",
        height=80
    )

    # Use quantum key from session or manual entry
    if "quantum_key" in st.session_state:
        key_input = st.session_state["quantum_key"]
        st.text("Quantum Key (auto-used): " + str(key_input))
    else:
        key_input_text = st.text_input(
            "Enter Quantum Key (comma-separated, e.g., 1,0,1,1,0,0,1,0)",
            key="manual_key"
        )
        key_input = [int(k.strip()) for k in key_input_text.split(",")] if key_input_text else []

    if st.button("Decrypt", key="decrypt_btn"):
        try:
            if encrypted_wallet_input and encrypted_txn_input and key_input:
                decrypted_wallet = xor_decrypt(encrypted_wallet_input, key_input)
                decrypted_txn = xor_decrypt(encrypted_txn_input, key_input)

                st.success("✅ Decryption Done")
                st.text("Decrypted Wallet Address: " + decrypted_wallet)
                st.text("Decrypted Transaction ID: " + decrypted_txn)

                # Auto-save decrypted results to session for later use
                st.session_state["dec_wallet_output"] = decrypted_wallet
                st.session_state["dec_txn_output"] = decrypted_txn
            else:
                st.warning("Provide Encrypted values and Quantum Key")
        except Exception as e:
            st.error(f"Error: {e}")
