# 🔐 Rail Fence Cipher Implementation (Python)

A complete and educational Python implementation of the Rail Fence Cipher encryption algorithm.
This project demonstrates zigzag-based transposition encryption and decryption using structured logic.

It is created as a learning and academic project to understand how classical transposition cryptography works internally, not as a production-ready security system.

---

## 🧱 Project Structure

```bash
rail-fence-cipher-python/
│
├── app.py            # Rail Fence cipher implementation (CLI based)
├── LICENSE           # Project license
└── README.md         # Project documentation
```

---

## ✨ Features

### 🔢 Rail-Based Zigzag Pattern
- Uses a numerical key (number of rails)
- Writes plaintext in a zigzag pattern
- Rearranges characters without substitution
- Demonstrates classical transposition technique

### 🔒 Encryption
- Removes spaces before processing
- Arranges characters across rails
- Reads row by row to produce ciphertext
- Maintains character order logic correctly

### 🔓 Decryption
- Reconstructs zigzag pattern
- Restores original message structure
- Reverses encryption algorithm accurately

### 🧮 Educational Focus
- Clean and readable logic
- Modular encryption & decryption functions
- Ideal for beginners in cryptography
- No external dependencies

---

## 🛠 Technologies Used

| Technology     | Role                           |
| -------------- | ------------------------------ |
| **Python 3**   | Core programming language      |
| **List Logic** | Zigzag rail structure handling |

---

## 📌 Purpose of This Project

This project is built to:
- Understand classical transposition ciphers
- Learn zigzag-based encryption logic
- Explore position-based cryptographic techniques
- Study reversible transformation algorithms

> ⚠️ This project is intended strictly for learning and demonstration purposes.

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShakalBhau0001/rail-fence-cipher-python.git
```

### 2️⃣ Navigate to the project folder
```bash
cd rail-fence-cipher-python
```

### 3️⃣ Run the program
```bash
python app.py
```

### 4️⃣ Follow the prompts
- Choose direction:
  - `E` → Encrypt
  - `D` → Decrypt
- Enter your message
- Enter number of rails
- View the result

---

## 🔎 Example

> Encryption :

```bash
Encrypt or Decrypt (E/D): E
Enter message:  MEET ME TOMORROW
Enter number of rails: 2

Encrypted message: MEMTMROETEOORW
```

> Decryption :

```bash
Encrypt or Decrypt (E/D): D
Enter message: MEMTMROETEOORW
Enter number of rails: 2

Decrypted message: MEETMETOMORROW
```

---

## ⚠️ Limitations

- Not secure for real-world use
- Classical cipher (easily breakable)
- Small key space (limited rails)
- Removes spaces during processing
- CLI-based interaction only

---

## 🌟 Future Improvements

- Preserve spaces and formatting
- Add brute-force rail testing mode
- Add frequency analysis support
- Add input validation for rail values
- Create GUI version
- Combine into a classical cryptography toolkit

---

## ⚠️ Disclaimer

This implementation is created **for educational and learning purposes only.**
The Rail Fence Cipher is historically significant but cryptographically insecure and must not be used to protect real-world sensitive data.

---

## 🪪 Author

> **Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
