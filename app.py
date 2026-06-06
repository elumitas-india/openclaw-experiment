import os
import subprocess

prompt = input("Enter Message Content: ")
 
result = subprocess.run(
    [os.getenv("OLLAMA", "ollama"), "run", os.getenv("OLLAMA_MODEL", "llama3:latest"), prompt],
    capture_output=True,
    text=True
)

reply = result.stdout.strip()

print("\nGenerated Message:")
print(reply)
numbers = [
    "+919600519263",
    "+919791373971"
]

for number in numbers:
    subprocess.run([
        os.getenv("OPENCLAW", "openclaw"),
        "message",
        "send",
        "--channel", os.getenv("CHANNEL", "whatsapp"),
        "--account", os.getenv("WHATSAPP_ACCOUNT", "default"),
        "--target", number,
        "--message", reply
    ])

print("\nSent to all recipients.")