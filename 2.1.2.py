def solution(name: str):
    print("Как Вас зовут?")
    print("Привет,", name)


def main():
    name = str(input())
    solution(name)


if __name__ == '__main__':
    main()