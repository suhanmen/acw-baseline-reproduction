def permute_string(s: str) -> list:
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(''.join(path))
            return
        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1:])

    chars = sorted(s)
    backtrack([], chars)
    return result