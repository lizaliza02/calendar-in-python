def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disc 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disc {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Test the function with n = 3
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
