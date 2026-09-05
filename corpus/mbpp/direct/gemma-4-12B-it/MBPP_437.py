def remove_odd(s: str) -> str:
    """
    Removes characters at odd indices (1, 3, 5, ...) from a string.
    Note: In the context of the provided assertions:
    "python" -> p(0), y(1), t(2), h(3), o(4), n(5) -> result "yhn" means indices 1, 3, 5 were kept?
    Wait, let's re-evaluate the assertions:
    "python" (p0, y1, t2, h3, o4, n5) -> "yhn" (indices 1, 3, 5)
    "program" (p0, r1, o2, g3, r4, a5, m6) -> "rga" (indices 1, 3, 5)
    "language" (l0, a1, n2, g3, u4, a5, g6, e7) -> "agae" (indices 1, 3, 5, 7)

    The logic is to keep characters at odd indices.
    """
    return "".join(s[i] for i in range(len(s)) if i % 2 != 0)

if __name__ == "__main__":
    assert remove_odd("python") == "yhn"
    assert remove_odd("program") == "rga"
    assert remove_odd("language") == "agae"