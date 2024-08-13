from guitar import Guitar


def main():
    guitars = []

    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    guitars.sort()

    print("Sorted guitars:")
    for guitar in guitars:
        print(guitar)

    # Adding new guitars
    name = input("Enter guitar name: ")
    year = int(input("Enter year made: "))
    cost = float(input("Enter cost: $"))
    guitars.append(Guitar(name, year, cost))

    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
