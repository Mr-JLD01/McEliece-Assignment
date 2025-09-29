import unittest

import json

import numpy as np

from Cryptosystem import McEliece

with open('example_key.json') as f:
   keys = json.load(f)
   public_key = (np.array(keys["G"]).astype(int), keys["t"])
   private_key = (np.array(keys["S"]).astype(int), np.array(keys["P"]).astype(int), np.array(keys["H"]).astype(int))

class TestMcEliece(unittest.TestCase):

    def test_key_gen(self):
        (public, private) = McEliece.key_gen()

        G_hat: np.ndarray = public[0]

        # S - substitution matrix tests
        S: np.ndarray = private[0]
        S_inverse = np.linalg.inv(S)

        self.assertEqual(S.shape[0], S.shape[1])
        self.assertEqual(S.shape[0], G_hat.shape[0])

        self.assertTrue(np.equal(S@S_inverse%2, np.eye(S.shape[0])).all())

        # P - Permutation matrix tests
        P: np.ndarray = private[1]
        P_inverse = np.linalg.inv(P)

        self.assertEqual(P.shape[0], P.shape[1])
        self.assertEqual(P.shape[0], G_hat.shape[1])

        self.assertTrue(np.equal(P@P_inverse%2, np.eye(P.shape[0])).all())

        # t-error tests
        t = public[1]
        self.assertEqual(type(t), int)
        self.assertTrue(t > 0)

        # Ĝ and H tests
        H: np.ndarray = private[2]

        G_prime = G_hat @ P_inverse % 2

        self.assertEqual(G_hat.shape[1], H.shape[1])

        self.assertTrue(np.equal(G_prime@H.T%2, np.zeros(shape=(G_prime.shape[0], H.shape[0]))).all())

        (public2, private2) = McEliece.key_gen()

        S2 = private2[0]
        P2 = private2[1]

        self.assertFalse(np.equal(S, S2).all())
        self.assertFalse(np.equal(P, P2).all())


    def test_encrypt(self):
        test_messages = ["Hi", "To" "Coding is fun?"]

        for message in test_messages:
            ciphertext = McEliece.encrypt(message, public_key)
            self.assertGreaterEqual(len(ciphertext.encode("ascii", "replace")), len(message)*1.3)
            ciphertext2 = McEliece.encrypt(message, public_key)
            self.assertNotEqual(ciphertext, ciphertext2)

    def test_full_without_key_gen(self):
        test_messages = ["Ey", "Po" "Arbitrarily long message."]

        for message in range(test_messages):
            self.assertEqual(message, McEliece.decrypt(McEliece.encrypt(message, public_key), private_key))

    def test_full_with_key_gen(self):
        test_messages = ["Pi", "Be" "My system fully works!"]

        for message in range(test_messages):
            (public, private) = McEliece.key_gen()

            self.assertEqual(message, McEliece.decrypt(McEliece.encrypt(message, public), private))



if __name__ == '__main__':
    unittest.main(verbosity=2)