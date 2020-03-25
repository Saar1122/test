
minutes = [2, 3, 5]
def convert(minutes):
    for saar in range(0, 3):
        minutes[saar] = minutes[saar] * 60
    print(minutes)
if __name__ == "__main__":
    convert(minutes)
