
def is_cyclic_shift(t, s):
    # Check if s is a cyclic shift of t
    for i in range(len(s)):
        cyclic_shift = s[i:] + s[:i]
        print(cyclic_shift)

        if cyclic_shift in t:
            return "yes"
    return "no"

def main():
    # Input
    t = input().strip()
    s = input().strip()

    # Output
    result = is_cyclic_shift(t, s)
    print(result)

if __name__ == "__main__":
    main()

