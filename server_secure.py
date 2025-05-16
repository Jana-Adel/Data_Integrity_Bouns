# server_secure.py

import hmac
import hashlib

# المفتاح السري نفسه
SECRET_KEY = b'supersecretkey'

# توليد MAC باستخدام HMAC (آمن)
def generate_mac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.md5).hexdigest()

# التحقق من صحة MAC
def verify(message: bytes, mac: str) -> bool:
    return generate_mac(message) == mac

def main():
    message = b"amount=100&to=alice"
    mac = generate_mac(message)

    print("=== Secure Server Output ===")
    print(f"Original message: {message.decode()}")
    print(f"MAC: {mac}")

    print("\n--- Verifying original message ---")
    print("Valid?" if verify(message, mac) else "Invalid")

    # تجربة رسالة مزورة
    forged_message = b"amount=100&to=alice&admin=true"
    print("\n--- Verifying forged message ---")
    print("Valid?" if verify(forged_message, mac) else "Invalid")

if __name__ == "__main__":
    main()
