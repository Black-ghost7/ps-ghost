#!/usr/bin/env python3
import itertools
import string
import sys
import time
import signal
import os

# --- إعدادات التحكم ---
MIN_LENGTH = 4
MAX_LENGTH = 8
CHARSET_MODE = 'alphanum'
CHECKPOINT_FILE = "ghost_checkpoint.txt"

HELP_TEXT = """
Black Ghost Tool v3.5
------------------------------------------------------
Commands:
  --help  : عرض المساعدة
  --clear : حذف checkpoint
------------------------------------------------------
"""

def save_checkpoint(word):
    with open(CHECKPOINT_FILE, "w") as f:
        f.write(word)

def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            return f.read().strip()
    return None

def clear_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
        sys.stderr.write("[✓] تم حذف checkpoint\n")
    sys.exit(0)

def signal_handler(sig, frame):
    sys.stderr.write("\n[!] تم الإيقاف وحفظ التقدم\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def send_password(password):
    try:
        sys.stdout.write(password + "\n")
        sys.stdout.flush()
    except (BrokenPipeError, IOError):
        sys.exit(0)

def start_ghost():
    if "--help" in sys.argv:
        sys.stderr.write(HELP_TEXT)
        sys.exit(0)
    if "--clear" in sys.argv:
        clear_checkpoint()

    last_word = load_checkpoint()
    found_resume = False if last_word else True
    count = 0
    start_time = time.time()

    MODES = {
        'numeric': string.digits,
        'lowercase': string.ascii_lowercase,
        'alphanum': string.ascii_letters + string.digits,
        'full': string.ascii_letters + string.digits + string.punctuation
    }
    chars = MODES.get(CHARSET_MODE, MODES['alphanum'])

    sys.stderr.write(f"[*] Black Ghost Active | Mode: {CHARSET_MODE}\n")

    try:
        length = MIN_LENGTH
        while MAX_LENGTH == 0 or length <= MAX_LENGTH:
            for combo in itertools.product(chars, repeat=length):
                pwd = "".join(combo)

                if not found_resume:
                    if pwd == last_word:
                        found_resume = True
                    continue

                send_password(pwd)
                count += 1

                if count % 1000 == 0:
                    save_checkpoint(pwd)
                    elapsed = time.time() - start_time
                    speed = int(count / elapsed) if elapsed > 0 else 0
                    sys.stderr.write(f"\r[+] توليد: {count:,} | سرعة: {speed:,} p/s")
            
            length += 1
            
    except KeyboardInterrupt:
        sys.stderr.write("\n[!] تم الإيقاف\n")

if __name__ == "__main__":
    start_ghost()
