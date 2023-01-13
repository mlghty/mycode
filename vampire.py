#!/usr/bin/python3

def main():
    count = 0
    temp_vamp_book = open("vampytimes.txt","a")

    with open("dracula.txt") as vamps:
        dracula = vamps.readlines()
        for line in dracula:
            temp_line = line.lower()
            if "vampire" in temp_line:
                print(line)
                temp_vamp_book.write(line)
                count += 1

    temp_vamp_book.close()
    print("Vampires appears ",str(count)+"!")

if __name__ == "__main__":
    main()
