import secrets
import string

password_history = set()

def generate_password(num_bytes):
    alphabet = string.ascii_letters + string.digits
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(num_bytes))
        if pwd not in password_history:
            password_history.add(pwd)
            return pwd

def main():
    print("Choose password size (bytes): 8, 16, 32, 64")
    while True:
        choice = input("Enter size: ").strip()

        if choice not in ("8", "16", "32", "64"):
            print("Invalid choice! Please enter 8, 16, 32, or 64.")
            continue

        size = int(choice)
        pwd = generate_password(size)
        print(f"\nGenerated password ({size} bytes):")
        print(pwd)
        print("\n---\n")

if __name__ == "__main__":
    main()
