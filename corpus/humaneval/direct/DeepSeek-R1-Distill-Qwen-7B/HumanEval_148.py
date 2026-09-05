def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Check if either planet is not in the list
    if planet1 not in planets or planet2 not in planets:
        return ()

    # Get the indices of the two planets
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    # Determine the start and end indices
    if index1 > index2:
        start, end = index2, index1
    else:
        start, end = index1, index2

    # Extract the planets between the two positions
    result = planets[start+1:end]

    return tuple(result)