import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a_str", choices=["hello", "goodbye"])
parser.add_argument("--a_bool", action="store_true")
parser.add_argument("--a_list", nargs="+")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    with open("out.txt", "w") as o:
        print(args, file=o)