from abc import ABC, abstractmethod

import numpy as np
import sympy

class CryptoSystem(ABC):

	@staticmethod
	@abstractmethod
	def key_gen() -> tuple[tuple, tuple]:
		"""Generates the public and private key of the CryptoSystem.

		Returns:
			public_key, private_key (tuple[tuple,tuple]):
				A tuple containing the public key in the first index and
				the private key in the second position
		"""
		...

	@staticmethod
	@abstractmethod
	def encrypt(message: str, public_key: tuple) -> str:
		"""Given a string message and the public key, the message is encrypted into a ciphertext

		Args:
		message (str): the plaintext message to encrypt

		public_key (tuple): the public key used to encrypt the plaintext

		Returns:
			ciphertext (str): A string output of the encrypted message (ciphertext)
		"""
		...

	@staticmethod
	@abstractmethod
	def decrypt(ciphertext: str, private_key: tuple) -> str:
		"""Given an encrypted string ciphertext and the private key, the message is decrypted into the plaintext

		Args:
		ciphertext (str): the plaintext message to encrypt

		private_key (tuple): the private key used to decrypt the ciphertext

		Returns:
			ciphertext (str): A string output of the decrypted message (plaintext)
		"""
		...




# Your implementation starts here
class McEliece(CryptoSystem):

	@staticmethod
	def key_gen() -> tuple[tuple, tuple]:
		# Reminders
		# The public_key contains  (Ĝ, t)
		# The private_key contains (S, P, H)

		# H is a Parity Check matrix of G
		# One benefit of Hamming codes is that
		# the Parity Check matrix is the columns are
		# every binary number excluding 0


		# G is the nullspace of H, sympy may help here


		# Ĝ = S * G * P
		# A Hamming code can correct only 1 error

		# S is any invertible matrix
		# Hint: all upper triangular matrices are invertible


		# P is a permutation matrix
		# Make and identity matrix and shuffle the rows


		raise NotImplementedError

	@staticmethod
	def encrypt(message: str, public_key: tuple) -> str:
		# Reminder, the public_key contains  (Ĝ, t)

		# convert message to binary numoy array
		# may need to make multiple arrays for longer messages


		# m' = m * Ĝ


		# Need to add t errors
		# Can be done by adding a random matrix of weight t to m'


		# Convert array ciphertext to a string, may need to be a hex string

		raise NotImplementedError


	@staticmethod
	def decrypt(ciphertext: str, private_key: tuple) -> str:
		# Reminder, the private_key contains (S, P, H)

		# Start by converting string to binary numpy array


		# Find the inverse of S and P, numpy may have a function for this


		# c' = c * P_inverse
		# This is for c' = m*S*G*P_inverse + z*P_inverse


		# Now we can begin to decode
		# With Hamming codes, c'*H.T lets us know where the error is.
		# Can flip the bit at the location given by c'*H.T by finding
		# what column of H it is


		# With the error gone, reconstruct the message
		# With the error gone, we have m*S*G
		# We can group (m*s)*G
		# Reminder that G is the nullspace of H
		# Sympy may have a function for that
		# Find columns of G that create the identity, and we can reconstruct m


		# convert m into an ascii string

		raise NotImplementedError
