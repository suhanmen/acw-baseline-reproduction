def Strongest_Extension(class_name, extensions):
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

    # Validate that class_name is a string and not empty
    if not isinstance(class_name, str):
        raise TypeError("class_name must be a string")

    if class_name.strip() == "":
        raise ValueError("class_name cannot be an empty string or whitespace only")

    # Validate that extensions is a list
    if not isinstance(extensions, list):
        raise TypeError("extensions must be a list")

    # Validate that extensions is not empty
    if len(extensions) == 0:
        raise ValueError("extensions list cannot be empty")

    # Helper function to calculate strength of an extension
    def calculate_strength(extension_name):
        """Calculates the strength of an extension based on CAP - SM.

        Args:
            extension_name (str): The name of the extension.

        Returns:
            int: The strength value (CAP - SM).
        """
        cap_count = 0
        sm_count = 0

        # Iterate through each character in the extension name
        for char in extension_name:
            # Check if the character is uppercase
            if char.isupper():
                cap_count += 1
            # Check if the character is lowercase
            elif char.islower():
                sm_count += 1
            # Ignore non-alphabetic characters for counting, 
            # though the problem implies we count letters only

        strength_value = cap_count - sm_count
        return strength_value

    # Helper function to compare two extensions and return the winner index
    def compare_extensions(idx1, ext1, idx2, ext2, max_strength, max_name):
        """Compares two extensions to determine which has stronger strength.

        Args:
            idx1 (int): Index of the first extension.
            ext1 (str): Name of the first extension.
            idx2 (int): Index of the second extension.
            ext2 (str): Name of the second extension.
            max_strength (int): Current maximum strength found.
            max_name (str): Name of the extension with max strength.

        Returns:
            tuple: (new_max_strength, new_max_name)
        """
        strength1 = calculate_strength(ext1)
        strength2 = calculate_strength(ext2)

        # If first extension is stronger, update max
        if strength1 > max_strength:
            return strength1, ext1
        # If second extension is stronger, update max
        elif strength2 > max_strength:
            return strength2, ext2
        # If strengths are equal, we keep the one that appears first (current max)
        else:
            return max_strength, max_name

    # Initialize variables to track the strongest extension
    # Start with the first extension in the list as the initial maximum
    initial_extension = extensions[0]
    current_best_index = 0
    current_best_strength = calculate_strength(initial_extension)
    current_best_name = initial_extension

    # Iterate through the extensions starting from the second one
    for i in range(1, len(extensions)):
        extension_name = extensions[i]
        extension_strength = calculate_strength(extension_name)

        # Compare current extension with the best found so far
        # If this extension is strictly stronger, update the best
        if extension_strength > current_best_strength:
            current_best_strength = extension_strength
            current_best_name = extension_name
            current_best_index = i
        # If strengths are equal, we do nothing (keep the first one encountered)
        # This satisfies the requirement: "choose the one that comes first in the list"

    # Construct the final result string
    result_string = f"{class_name}.{current_best_name}"

    return result_string