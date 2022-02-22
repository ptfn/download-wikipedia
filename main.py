import wikipedia as wiki
import sys

def main():
    wiki.set_lang("ru")
    arr = sys.argv[1:]

    for i in range(len(arr)):
        try:
            string = arr[i].title()
            ny = wiki.page(arr[i])
            
            file = open(f"{arr[i]}.txt", "+a")
            file.write(ny.content)
            file.close()
            print(f"{string}\t\033[32mfound\033[0m")
        except:
            print(f"{string}\t\033[31mnot\033[0m")

if __name__ == "__main__":
    main()
