def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    lower_ans = answer.lower().strip()
    if lower_ans == "42" or lower_ans== "forty-two" or lower_ans == "forty two":
        print("Yes")
    else:
        print("No")

main()


