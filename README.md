# Caesar Cipher Implementation

## Purpose
The purpose of this project is to implement a Caesar cipher for encrypting and decrypting messages. The Caesar cipher is a basic encryption technique that shifts each character in a message by a fixed number of positions in the alphabet.

## Description
This script provides a simple way to encode or decode messages using the Caesar cipher method. The user can input a message, specify a shift value, and choose whether to encrypt or decrypt the message. The script then processes the input and returns the transformed message.

## How It Works
1. **Input:**
   - Message to be encrypted or decrypted.
   - Shift value (integer).
   - Mode (encrypt or decrypt).

2. **Processing:**
   - Iterates through each character in the message.
   - Shifts letters by the specified value while preserving spaces and non-alphabetic characters.
   - Maintains the case of letters (uppercase or lowercase).

3. **Output:**
   - Displays the transformed (encrypted or decrypted) message.

## Dataset
No external dataset is required. The input is provided by the user.

## Installation and Setup
1. **Python Environment:** Ensure you have Python installed on your system.
2. **Script Execution:** Save the script and run it in a Python environment or IDE.

## Input
1. **Message:** The text that you want to encrypt or decrypt.
2. **Shift Value:** An integer that represents the number of positions each character in the message will be shifted.
3. **Mode:**
   - `e` for encryption
   - `d` for decryption

## Usage
1. Run the script.
2. Enter the message you want to encrypt or decrypt.
3. Enter the shift value (an integer, positive for forward shift and negative for backward shift).
4. Enter the mode:
   - `e` for encryption
   - `d` for decryption

## Example

**Encrypting a message:**
- **Input Message:** `HELLO WORLD`
- **Input Shift Value:** `3`
- **Input Mode:** `e`
- **Output:** `KHOOR ZRUOG`

**Decrypting a message:**
- **Input Message:** `KHOOR ZRUOG`
- **Input Shift Value:** `3`
- **Input Mode:** `d`
- **Output:** `HELLO WORLD`

## Notes
- The shift value can be any integer. A positive value shifts characters forward, while a negative value shifts them backward.
- The mode must be either 'e' for encryption or 'd' for decryption.
