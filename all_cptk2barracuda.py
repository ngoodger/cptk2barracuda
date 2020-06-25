import argparse
import cptk2barracuda
import os

def main():
    ##########################################
    # parse argments
    ##########################################
    parser = argparse.ArgumentParser(prog='all_cptk2barracuda',usage='Converts each checkpoint in results dir to nn.')
    parser.add_argument('-i', '--results_dir', help='Input result dir path.')
    args = parser.parse_args()
    cptk_files = [f[:-5] for f in os.listdir(args.results_dir) if ".ckpt.meta" in f]
    # Call convert for each checkpoint file.
    for cptk_file in cptk_files:
        cptk2barracuda.convert(input_cptk_file=os.path.join(args.results_dir, cptk_file),
                               output_nn_file=os.path.join(args.results_dir, cptk_file + ".nn"))

if __name__ == "__main__":
    main()
