# Steganography-Python

**Disclaimer: This project is not a proper utilization of steganography and is meant purely for experimental and entertainment purposes.**

## Description

This repository contains a simple Python script that demonstrates a basic form of steganography, a technique used to hide information within an image. Please note that this implementation is not secure and should not be used for any serious or sensitive applications. It was created for educational and recreational purposes only.

## Motivation

Ever wondered how steganography works? This project is a result of curiosity and the desire to create a simple yet functional example of steganography without modifying the actual image. It's meant to showcase the concept, even though it doesn't adhere to proper steganographic practices.

## How It Works

The script allows you to "encrypt" a secret message using a base64-encoded key that is derived from the provided image. The secret message is transformed into a sequence of positions within the image's base64 encoding. Spaces within the message are replaced with a special value. This encrypted message is then base64-encoded to create the final key.

During "decryption," the key is decoded and converted back to the sequence of positions. The original message is reconstructed by looking up characters in the base64-encoded image data using these positions.

**Please note that this implementation has limitations and edge cases where it may not work correctly. It is intended purely as a demo and should not be used for any serious purpose.**

## Usage

1. Run the Python script and provide the path to an image file when prompted.
2. Choose whether to encrypt or decrypt.
3. If encrypting, enter the secret message.
4. If decrypting, enter the provided key.

Please note that this implementation is not secure and is purely intended for demonstration purposes.

## Disclaimer

This project is not intended for real-world steganography applications. It does not provide any form of security or confidentiality. If you are interested in secure steganography, it is recommended to use established libraries and techniques that have been thoroughly reviewed and tested.

## Contributing

Contributions to enhance, modify, or expand upon this project are welcome. However, keep in mind the experimental and recreational nature of this project.

