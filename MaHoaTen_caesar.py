#Cách 1
import string

def caesar_cipher(text: str, k: int) -> str:
    """Trả về chuỗi đã mã hóa bằng Caesar cipher với shift k (k có thể >26 hoặc âm)."""
    k = k % 26
    result_chars = []
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase

    for ch in text:
        if ch in upper:
            idx = upper.index(ch)
            result_chars.append(upper[(idx + k) % 26])
        elif ch in lower:
            idx = lower.index(ch)
            result_chars.append(lower[(idx + k) % 26])
        else:
            result_chars.append(ch)
    return ''.join(result_chars)

if __name__ == "__main__":
    plaintext = "HOANGTHIKIMDUNG"
    k = 22

    ciphertext = caesar_cipher(plaintext, k)
    print(f"Plaintext: {plaintext}")
    print(f"k = {k}")
    print(f"Ciphertext: {ciphertext}")

#Cách 2
plaintext = "HOANGTHIKIMDUNG"
A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
k = 22  # số dịch

ciphertext = ""
for i in plaintext:
    if i in A:
        x = A.index(i)   # tìm vị trí chữ trong A
        new_char = A[(x + k) % 26]   # dịch k vị trí, quay vòng bằng mod 26
        ciphertext += new_char
print("Ciphertext:", ciphertext)
