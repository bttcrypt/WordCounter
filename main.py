def count_words(text):
    word_count = {}
    words = text.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def main():
    print("Welcome to the Word Counter!")
    text = input("Enter some text: ")

    word_count = count_words(text)
    print("Word count:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
