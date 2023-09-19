def ft_tqdm(lst: range) -> None:
    """ft_tqdm"""

    for elem in range(len(lst) + 1):
        percentage = int((elem / (len(lst))) * 100)
        print(f"{percentage}%|", end="")
        print(f"{'█' * (percentage)}{' ' * (100 - percentage)}", end="")
        print(f"| {elem}/{len(lst)}", end="\r")
        yield elem
    print()
