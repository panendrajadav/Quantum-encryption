namespace QuantumEncryption {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Arrays;

    operation GenerateQuantumKey(bits : Int) : Result[] {
        using (qubits = Qubit[bits]) {
            // Apply Hadamard to each qubit to create superposition
            for (i in 0..bits - 1) {
                H(qubits[i]);
            }
            // Measure each qubit to get random bits
            mutable results = new Result[bits];
            for (i in 0..bits - 1) {
                set results w/= i <- M(qubits[i]);
            }
            ResetAll(qubits);
            return results;
        }
    }

    function XOREncrypt(data : String, key : Result[]) : String {
        // Convert Result[] -> Int[]
        let keyBits = [for k in key -> (if k == One then 1 else 0)];
        let keyLen = Length(keyBits);
        mutable encrypted = "";

        for (i in 0..Length(data) - 1) {
            let charVal = Microsoft.Quantum.Convert.StringAsInt(String([data[i]]));
            let xorVal = charVal ^ keyBits[i % keyLen];
            set encrypted += IntAsString(xorVal);
        }
        return encrypted;
    }

    function XORDecrypt(encrypted : String, key : Result[]) : String {
        // Same logic as XOREncrypt (symmetric)
        return XOREncrypt(encrypted, key);
    }

    @EntryPoint()
    operation Main() : Unit {
        let wallet = "MyWallet123";
        let txn = "Txn987ABC";

        Message("⚛ Generating Quantum Key...");
        let qKey = GenerateQuantumKey(8);
        Message($"Quantum Key: {qKey}");

        let encryptedWallet = XOREncrypt(wallet, qKey);
        let encryptedTxn = XOREncrypt(txn, qKey);

        Message($"🔐 Encrypted Wallet: {encryptedWallet}");
        Message($"🔐 Encrypted Transaction: {encryptedTxn}");

        let decryptedWallet = XORDecrypt(encryptedWallet, qKey);
        let decryptedTxn = XORDecrypt(encryptedTxn, qKey);

        Message($"🔓 Decrypted Wallet: {decryptedWallet}");
        Message($"🔓 Decrypted Transaction: {decryptedTxn}");
    }
}
