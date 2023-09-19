def ft_tqdm(lst: range) -> None:
    """ft_tqdm"""

    for elem in range(lst.stop + 1):
        percentage = int((elem / (lst.stop)) * 100)
        print(f"{percentage}%|", end="")
        for _ in range(percentage // 2):
            print("█", end="")
        for _ in range(50 - (percentage // 2)):
            print(" ", end="")
        print(f"| {elem}/{lst.stop}", end="\r")
        yield elem
