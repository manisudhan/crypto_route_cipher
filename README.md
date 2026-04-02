# Route Cipher with Spiral Traversal (Python)

## Description

This project implements a **Route Cipher** using a spiral traversal pattern. The plaintext is arranged in a matrix and then read in a spiral order to generate the encrypted message. The same pattern is reversed during decryption to recover the original text. A custom hash function is also used to generate a numeric hash of the encrypted message.

---

## How It Works (Detailed Explanation)

### 🔐 Encryption Process

Let’s take an example:

```text
Input Text: HELLO WORLD
Step Size (cols): 4
```

### Step 1: Preprocess the text

* Remove spaces
* Convert to continuous text

```text
HELLOWORLD
```

---

### Step 2: Create matrix

Number of rows:

```
rows = ceil(len(text) / cols)
     = ceil(10 / 4)
     = 3
```

Matrix (filled row-wise):

```
H   E   L   L
O   W   O   R
L   D
```

(Last row is partially filled)

---

### Step 3: Spiral traversal (encryption)

We traverse the matrix in this order:

1. Right column ↓
2. Bottom row ←
3. Left column ↑
4. Top row →
   Repeat until all elements are covered

#### Traversal steps:

* Right column ↓ → `L R`
* Bottom row ← → `D L`
* Left column ↑ → `O`
* Top row → → `E L`
* Remaining middle → `O W`

Final encrypted text:

```text
LRDLOELOW
```

---

### 🔓 Decryption Process

We reverse the process using the same spiral pattern.

#### Step 1: Create empty matrix structure

Mark positions with `*`:

```
*   *   *   *
*   *   *   *
*   *
```

---

### Step 2: Fill matrix in spiral order

Insert cipher text (`LRDLOELOW`) in spiral order:

```
H   E   L   L
O   W   O   R
L   D
```

(Original structure reconstructed)

---

### Step 3: Read row-wise

```
HELLOWORLD
```

---

## 🔢 Hash Function Explanation

The `unique_hash` function generates a numeric value from the encrypted text.

### Steps:

1. Start with initial value `h = 17`
2. For each character:

   * Convert character to ASCII using `ord()`
   * Shift bits using `(i % 5)`
   * Combine using XOR (`^`)
   * Multiply and take modulo (`% 100000`)

### Example:

```text
Input: LRDLOELOW
Output: (some numeric value like 48293)
```

👉 This hash can be used to verify integrity or uniqueness of the cipher.

---

## Important Notes

* The number of columns (step size) must be the same for encryption and decryption
* Spaces are removed during processing
* The spiral pattern is the key to both encryption and decryption
* Empty cells are ignored during traversal

---
