xs: str = "123"
ys: str = "45"

x_idx: int = 0
while x_idx < len(xs):
    y_idx: int = 0
    while y_idx < len(ys):
        print(f"({xs[x_idx]},{ys[y_idx]})")
        y_idx = y_idx + 1
    x_idx = x_idx + 1
