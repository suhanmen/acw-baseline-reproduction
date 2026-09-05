def Strongest_Extension(class_name, extensions):
    """Determine the strongest extension for a given class and return the formatted string."""

    if not isinstance(class_name, str) or not class_name:
        raise ValueError("class_name must be a non-empty string.")

    if not isinstance(extensions, list) or not extensions:
        raise ValueError("extensions must be a non-empty list.")

    # Helper function to calculate the strength of an extension
    def calculate_strength(extension):
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        return cap - sm

    # Find the extension with the maximum strength
    max_strength = None
    strongest_extension = None
    for ext in extensions:
        if not isinstance(ext, str) or not ext:
            raise ValueError("All extensions must be non-empty strings.")

        strength = calculate_strength(ext)
        # Update if this extension has a higher strength or is the first one
        if max_strength is None or strength > max_strength or (strength == max_strength and ext < strongest_extension):
            max_strength = strength
            strongest_extension = ext

    # Format the result
    return f"{class_name}.{strongest_extension}"