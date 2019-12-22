import argparse
import codecs
from collections import defaultdict


# Consistent with Python 2


def read_dataset(data_path, sep='\t', mixed=False):
    vocab = defaultdict(list)
    with codecs.open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_split = line.replace("\n", '').split(sep)
            word = line_split[0]
            hypernyms = line_split[1] if mixed is False else set(line_split[1:])
            vocab[word].append(hypernyms)
    return vocab


def get_score(full, direct, predicted, k=10, mixed=False):
    ap_sum = 0
    rr_sum = 0

    for neologism in full:
        full_hypernyms = set(full.get(neologism, [])) if mixed is False else full.get(neologism, [])
        direct_hypernyms = set(direct.get(neologism, []))
        predicted_hypernyms = predicted.get(neologism, [])

        if mixed is True:
            ap_sum += compute_ap_mixed(full_hypernyms, predicted_hypernyms, k)
            full_hypernyms = set.union(*full_hypernyms)
        else:
            ap_sum += max(compute_ap(full_hypernyms, predicted_hypernyms, k),
                          compute_ap(direct_hypernyms, predicted_hypernyms, k))

        rr_sum += compute_rr(full_hypernyms, predicted_hypernyms, k)

    return ap_sum / len(full), rr_sum / len(full)

def compute_ap_mixed(actual, predicted, k=10, skip_already_predicted=True):
    if not actual:
        return 0.0

    predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0
    already_predicted = set()
    skipped = 0
    for i, p in enumerate(predicted):
        if p in already_predicted:
            if skip_already_predicted is True:
                skipped += 1
            continue
        for parents in actual:
            if p in parents:
                num_hits += 1.0
                score += num_hits / (i + 1.0 - skipped)
                already_predicted.update(parents)
                break

    return score / min(len(actual), k)

def compute_ap(actual, predicted, k=10):
    if not actual:
        return 0.0

    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0

    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)

    return score / min(len(actual), k)


def compute_rr(true, predicted, k=10):
    for i, synset in enumerate(predicted[:k]):
        if synset in true:
            return 1.0 / (i + 1.0)
    return 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('full')
    parser.add_argument('direct')
    parser.add_argument('predicted')
    parser.add_argument('--mixed', action='store_true')
    args = parser.parse_args()

    full = read_dataset(args.full, mixed=args.mixed)
    direct = read_dataset(args.direct)
    submitted = read_dataset(args.predicted)
    if set(full) != set(submitted):
        print("Not all words are presented in your file")
    mean_ap, mean_rr = get_score(full, direct, submitted, mixed=args.mixed)
    print("map: {0}\nmrr: {1}\n".format(mean_ap, mean_rr))


if __name__ == '__main__':
    main()
