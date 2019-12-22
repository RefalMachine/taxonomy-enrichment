import os
import codecs
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_dir')
    args = parser.parse_args()

    test_word = 'КОШКА'
    test_hypernyms = [['4453-N', '144174-N'], ['106553-N', '106554-N']]

    test_true_full_path = os.path.join(args.test_dir, 'test_true_full.tsv')
    test_true_direct_path = os.path.join(args.test_dir, 'test_true_direct.tsv')
    test_pred_full_path = os.path.join(args.test_dir, 'test_pred_full.tsv')
    test_pred_direct_path = os.path.join(args.test_dir, 'test_pred_direct.tsv')
    test_true_mix_path = os.path.join(args.test_dir, 'test_true_mix.tsv')
    test_pred_mix_path = os.path.join(args.test_dir, 'test_pred_mix.tsv')
    test_pred_one_path = os.path.join(args.test_dir, 'test_pred_one.tsv')

    with codecs.open(test_true_full_path, 'w', 'utf-8') as file_descr:
        for parents in test_hypernyms:
            for hypernym in parents:
                file_descr.write(f'{test_word}\t{hypernym}\n')

    with codecs.open(test_true_direct_path, 'w', 'utf-8') as file_descr:
        for parents in test_hypernyms:
            file_descr.write(f'{test_word}\t{parents[0]}\n')

    with codecs.open(test_true_mix_path, 'w', 'utf-8') as file_descr:
        for parents in test_hypernyms:
            p = '\t'.join(parents)
            file_descr.write(f'{test_word}\t{p}\n')

    with codecs.open(test_pred_full_path, 'w', 'utf-8') as file_descr:
        for parents in test_hypernyms:
            for hypernym in parents:
                file_descr.write(f'{test_word}\t{hypernym}\n')

    with codecs.open(test_pred_direct_path, 'w', 'utf-8') as file_descr:
        for parents in test_hypernyms:
            file_descr.write(f'{test_word}\t{parents[0]}\n')

    with codecs.open(test_pred_mix_path, 'w', 'utf-8') as file_descr:
        for i, parents in enumerate(test_hypernyms):
            file_descr.write(f'{test_word}\t{parents[(i + 1) % 2]}\n')

    with codecs.open(test_pred_one_path, 'w', 'utf-8') as file_descr:
        file_descr.write(f'{test_word}\t{test_hypernyms[0][1]}\n')
