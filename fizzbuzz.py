def fizzbuzz() -> None:
    for i in range(1, 101):
        match magic(i):
            case 1:
                print(f"{i}: ")
            case 6:
                print(f"{i}: fizz")
            case 10:
                print(f"{i}: buzz")
            case 0:
                print(f"{i}: fizzbuzz")

def magic(n: int) -> int:
    return n**4 % 15


if __name__ == "__main__":
    fizzbuzz()
