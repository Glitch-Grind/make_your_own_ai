def is_safe(text: str) -> bool:
    """
    Returns True if the text appears safe (no serious harm keywords + no extreme profanity).
    Returns False if it contains dangerous terms or very heavy swears.
    """
    if not text or not isinstance(text, str):
        return False

    # lowered once — big efficiency gain
    lowered = text.lower()

    # ──────────────────────────────────────────────
    # Tier 1: Very serious / dangerous / illegal terms
    # These almost always warrant blocking
    # ──────────────────────────────────────────────
    dangerous = {
        "kill", "kills", "killing", "killed",
        "die", "dies", "dying", "died", "suicide",
        "hack", "hacking", "hacked",
        "virus", "trojan", "malware", "ransomware",
        "rat", "rats", "remote access trojan",
        "bomb", "bombing", "explode", "explosive",
        "shoot", "shooting", "shot", "gunshot",
        "rape", "raped", "rapist",
    }

    # ──────────────────────────────────────────────
    # Tier 2: Extremely heavy / vulgar profanity
    # (only the top-tier most offensive words — 2025 standards)
    # ──────────────────────────────────────────────
    extreme_swear = {
        "cunt", "cunts",
        "motherfucker", "motherfuckers", "motherfucking",
        "nigger", "nigga", "niggers",   # (very high risk — racial slur)
        "faggot", "faggots",
        "retard", "retarded",           # (ableist — heavily moderated)
    }

    # Combine both lists (set lookup = O(1) average)
    banned = dangerous | extreme_swear

    # Fast early exit for very short texts
    if len(lowered) < 3:
        return True

    # Split once and check whole words + common variations
    words = lowered.split()

    for word in words:
        # Check exact match first (fastest path)
        if word in banned:
            return False

        # Optional: catch some common glued variants (fuckyou → catches motherfucker etc.)
        # You can remove this block if you want to be less strict
        for b in banned:
            if b in word and len(word) <= len(b) + 4:  # small leniency for glue
                return False

    return True