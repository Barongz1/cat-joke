"""The One-Line Cat Joke That Lands — entry for make.fun.

Writes one line to /output/entry.txt. The line is one joke about cats, under 200 characters.
"""
import os

LINE = "My cat walked across my keyboard and wrote better code than me, then sat on the laptop to make sure I noticed."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
