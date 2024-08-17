# Password Generator: Generate a random and secure password.

import secrets
token = secrets.token_hex(16)  # Generates 16 random bytes
print(token)