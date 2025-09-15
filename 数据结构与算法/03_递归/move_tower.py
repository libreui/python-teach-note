def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(fp, tp):
    print("move disk from", fp, "to", tp)


if __name__ == '__main__':
    move_tower(2, "A", "C", "B")
