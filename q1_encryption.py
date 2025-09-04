def shift_within_range(ch, shift, start, end):
    """Shift character within its given ASCII range, wrapping inside the range."""
    range_size = end - start + 1
    return chr((ord(ch) - start + shift) % range_size + start)

def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    result = ""
    for ch in text:
        if 'a' <= ch <= 'm':
            result += shift_within_range(ch, shift1 * shift2, ord('a'), ord('m'))
        elif 'n' <= ch <= 'z':
            result += shift_within_range(ch, -(shift1 + shift2), ord('n'), ord('z'))
        elif 'A' <= ch <= 'M':
            result += shift_within_range(ch, -shift1, ord('A'), ord('M'))
        elif 'N' <= ch <= 'Z':
            result += shift_within_range(ch, shift2 ** 2, ord('N'), ord('Z'))
        else:
            result += ch

    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(result)

def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    result = ""
    for ch in text:
        if 'a' <= ch <= 'm':
            result += shift_within_range(ch, -(shift1 * shift2), ord('a'), ord('m'))
        elif 'n' <= ch <= 'z':
            result += shift_within_range(ch, shift1 + shift2, ord('n'), ord('z'))
        elif 'A' <= ch <= 'M':
            result += shift_within_range(ch, shift1, ord('A'), ord('M'))
        elif 'N' <= ch <= 'Z':
            result += shift_within_range(ch, -(shift2 ** 2), ord('N'), ord('Z'))
        else:
            result += ch

    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(result)

def verify():
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        original = f.read()
    with open("decrypted_text.txt", "r", encoding="utf-8") as f:
        decrypted = f.read()

    if original == decrypted:
        print("Decryption successful")
    else:
        print("Decryption failed")

def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))
    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify()

if __name__ == "__main__":
    main()
