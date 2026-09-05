def start_withp(words):
    candidates = [w for w in words if w.startswith('p') or w.startswith('P')]
    if len(candidates) < 2:
        return None
    words.sort(key=lambda w: (w.lower() == w, w.lower()))
    return candidates[0], candidates[1]