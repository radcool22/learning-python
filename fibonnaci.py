def main():
    n_terms = int(input("Enter the number of terms you want to print: "))

    n1 = 0
    n2 = 1

    print(n1)
    print(n2)

    for i in range(n_terms - 2):
        next_term = n1 + n2
        print(next_term)
        n1 = n2
        n2 = next_term

if __name__ == "__main__":
    main()