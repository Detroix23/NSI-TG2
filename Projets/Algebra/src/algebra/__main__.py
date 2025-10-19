"""
ALGEBRA
__main__.py
"""


def pascal_triangle(n: int) -> None:
    triangle: list[list[int]] = [
        [1],
        [1, 1],
    ]
    
    for y in range(2, n):
        line: list[int] = list()
        for x in range(y + 1):
            if x == 0 or x == y:
                line.append(1)
            else: 
                try:
                    line.append(triangle[y - 1][x - 1] + triangle[y - 1][x])
                except IndexError:
                    raise IndexError(f"""
Tr {triangle}
x - 1: ({y - 1} {x - 1}),
x: ({y - 1} {x}), 
""")
                
        triangle.append(line)
        
    return triangle


def print_triangle(triangle: list[list[int]]) -> None:
    last = triangle[-1]
    max_length: int = len(str(last[len(last) // 2])) + 1
    print(f"max {max_length}")
    
    for line in triangle:
        for number in line:
            formatted = "".join((str(number), " " * (max_length - len(str(number)))))
            print(formatted, end="")
        print()

def main() -> None:
    t = pascal_triangle(10)
    print_triangle(t)


if __name__ == "__main__":
    main()