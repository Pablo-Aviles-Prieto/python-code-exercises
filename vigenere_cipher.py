def vigenere(message: str, key, direction=1):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


if __name__ == "__main__":
    secret_key = "encoder"
    plain_text = "Supah secret message"
    encrypted_message = encrypt(plain_text, secret_key)  # whrok wvgegh pijwnis
    decrypted_message = decrypt(encrypted_message, secret_key)  # supah secret message
    print(
        f"Plain message is: {plain_text}, encrypted message is: {encrypted_message} and decrypted back is: {decrypted_message}"
    )
