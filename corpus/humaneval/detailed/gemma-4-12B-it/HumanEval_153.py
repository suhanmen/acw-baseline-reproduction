import typing

def calculate_extension_strength(extension: str) -> int:
    """
    Calculates the strength of an extension based on the count of
    uppercase letters (CAP) and lowercase letters (SM).
    Strength is defined as CAP - SM.
    """
    cap_count: int = 0
    sm_count: int = 0

    # Iterate through each character to identify casing
    for char in extension:
        if char.isupper():
            cap_count += 1
        elif char.islower():
            sm_count += 1

    return cap_count - sm_count

def Strongest_Extension(class_name: str, extensions: list[str]) -> str:
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    # Input Validation: Ensure class_name is a non-empty string
    if not isinstance(class_name, str) or not class_name:
        raise ValueError("class_name must be a non-empty string.")

    # Input Validation: Ensure extensions is a list of strings
    if not isinstance(extensions, list):
        raise ValueError("extensions must be a list.")

    # Edge Case: If the list of extensions is empty, return the class name 
    # or handle as per requirement. Based on instructions, we assume 
    # at least one extension exists to have a 'strongest'.
    if not extensions:
        return class_name

    # Variable to track the strongest extension found so far
    strongest_extension_name: str = ""
    # Variable to track the maximum strength value encountered
    # Initialize with negative infinity to ensure any real number is larger
    max_strength: float = float('-inf')

    # Iterate through extensions and calculate strengths
    for extension in extensions:
        # Validate that the current extension is a string
        if not isinstance(extension, str):
            continue

        # Calculate strength for the current extension
        current_strength: int = calculate_extension_strength(extension)

        # If current strength is strictly greater than max_strength, update.
        # By using strictly greater (>), we preserve the first occurrence
        # in the case of ties, satisfying the requirement.
        if current_strength > max_strength:
            max_strength = current_strength
            strongest_extension_name = extension

    # Handle the case where no valid string extensions were found in the list
    if strongest_extension_name == "":
        # This handles lists containing non-strings or empty list logic
        return class_name

    # Construct the final output string
    result: str = f"{class_name}.{strongest_extension_name}"

    return result