from python.runfiles import runfiles


def main():
  path = runfiles.Create().Rlocation("pyzip/data.txt")
  with open(path, "r") as fin:
    print(fin.read())


if __name__ == "__main__":
  main()
