import argparse
from typing import List, Tuple


def read_file(path: str) -> List[Tuple[str, str]]:
    with open(path, 'r') as fin:
        text = fin.read()
    text_lines = text.split('\n')
    result = []
    for line in text_lines:
        if "\t" not in line:
            continue
        line = line[line.find("\t") + 1:]
        word = line[:line.find("\t")]
        word = word.lower()
        line = line[line.find("\t_\t") + 3:]
        tag = line[:line.find("\t")]
        result.append((word, tag))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('train_path', help='Path to a file with training data')
    parser.add_argument('test_path', help='Path to a file with test data')
    parser.add_argument('results_path', help='Path to a file with results')

    args = parser.parse_args()

    train = read_file(args.train_path)
    test = read_file(args.test_path)
    results = read_file(args.results_path)

    train_words = set()
    for word, _ in train:
        train_words.add(word)

    correct_lines = 0
    num_lines = 0

    correct_words = set()
    test_words = set()

    correct_unseen_lines = 0
    num_unseen_lines = 0

    correct_unseen_words = set()
    test_unseen_words = set()

    for (word, predicted), (_, target) in zip(results, test):
        num_lines += 1
        test_words.add(word)
        if predicted == target:
            correct_lines += 1
            correct_words.add(word)

            if word not in train_words:
                correct_unseen_lines += 1
                correct_unseen_words.add(word)

        if word not in train_words:
            num_unseen_lines += 1
            test_unseen_words.add(word)

    print("Intersection between test and train by lines", (num_lines-num_unseen_lines)/num_lines)
    print("Intersection between test and train by words", (len(test_words)-len(test_unseen_words))/len(test_words))

    print("Correct lines ratio", correct_lines/num_lines)
    print("Correct words ratio", len(correct_words)/len(test_words))

    print("Correct unseen lines ratio", correct_unseen_lines / num_unseen_lines)
    print("Correct unseen words ratio", len(correct_unseen_words)/ len(test_unseen_words))


if __name__ == '__main__':
    main()
