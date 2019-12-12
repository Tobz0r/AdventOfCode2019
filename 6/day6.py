def generate_orbit_map(orbit_data):
    """Generates orbit map"""
    return dict(reversed(row.split(")")) for row in orbit_data)


def find_path(orbit_map, value):
    """Finds path"""
    path = []
    for value in iter(lambda: orbit_map.get(value), None):
        path.append(value)
    return path


def main():
    """main"""
    orbit_map = generate_orbit_map(open("input.txt").read().splitlines())
    print("Part 1: ", sum(len(find_path(orbit_map, planet)) for planet in orbit_map))
    print("Part 2: ", len(set(find_path(orbit_map, "YOU")).symmetric_difference(set(find_path(orbit_map, "SAN")))))


main()
