import numpy as np
import pandas as pd

# Define the DNA encoding method
ENCODING_METHOD = {
   'A': '00',
   'C': '01',
   'G': '10',
   'T': '11'
}

# Define the function to encode the plaintext message as a DNA sequence
def encode(message):
   binary_message = ''.join([format(ord(char), '08b') for char in message])
   dna_sequence = ''
   for i in range(0, len(binary_message), 2):
       dna_sequence += ENCODING_METHOD[binary_message[i:i+2]]
   return dna_sequence

# Define the function to decode the DNA sequence back to a plaintext message
def decode(dna_sequence):
   binary_message = ''
   for i in range(0, len(dna_sequence), 2):
       for base, code in ENCODING_METHOD.items():
           if dna_sequence[i:i+2] == code:
               binary_message += base
   message = ''.join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])
   return message

# Test the functions with a sample message
message = "Hello, world!"
dna_sequence = encode(message)
decoded_message = decode(dna_sequence)
print("Original message: ", message)
print("Encoded DNA sequence: ", dna_sequence)
print("Decoded message: ", decoded_message)
