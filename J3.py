def find_smallest_frame(drops):
    min_x = min(drops, key=lambda x: x[0])[0]
    max_x = max(drops, key=lambda x: x[0])[0]
    min_y = min(drops, key=lambda x: x[1])[1]
    max_y = max(drops, key=lambda x: x[1])[1]

    bottom_left = (min_x - 1, min_y - 1)
    top_right = (max_x + 1, max_y + 1)

    return bottom_left, top_right

def main():
    n = int(input().strip())

    drops = []
    for _ in range(n):
        coordinates = input().strip().split(',')
        coordinates = tuple(map(int, coordinates))
        drops.append(coordinates)

    bottom_left, top_right = find_smallest_frame(drops)
    print(f"{bottom_left[0]},{bottom_left[1]}")
    print(f"{top_right[0]},{top_right[1]}")

if __name__ == "__main__":
    main()