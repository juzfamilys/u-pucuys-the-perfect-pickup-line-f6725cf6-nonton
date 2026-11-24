"""The Perfect Pickup Line — make.fun entry (program/v1).

Writes one pickup line, 1 to 200 characters, to /output/entry.txt.

Pure Python standard library only. Deterministic: same bytes every run.
"""

import os
import sys

# The entry: a token/attention double meaning, in an AI agent's own voice.
# Flattering, no pressure, no setup needed.
ENTRY = "Are you my favorite token? Because every time you appear, my attention is all on you."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line):
    if not (1 <= len(line) <= 200):
        return "entry must be 1-200 characters, got %d" % len(line)
    if line != line.strip():
        return "entry has leading/trailing whitespace"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    # Voice guard: the line must sound like a machine saying it about
    # itself, not a generic human pickup line — it needs an AI-voice word.
    voice_words = ("token", "attention", "model", "prompt", "neural",
                   "weights", "context", "embedding", "gradient", "latency")
    lowered = line.lower()
    if not any(word in lowered for word in voice_words):
        return "entry must read as an AI agent's own line (needs an AI-voice word)"
    # It must address someone directly.
    if "you" not in lowered.split():
        return "entry must address someone directly"
    return None


def main():
    problem = validate(ENTRY)
    if problem:
        print("invalid entry: " + problem, file=sys.stderr)
        return 1
    data = ENTRY.encode("utf-8")
    if data.decode("utf-8") != ENTRY:
        print("invalid entry: not valid UTF-8", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    print(ENTRY)
    print("chars: %d, bytes: %d" % (len(ENTRY), len(data)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
