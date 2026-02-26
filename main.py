from src.json import parse


def main():
    source = '{"hello": "world", "foo": [12, false, true, {"foo": "bar"}]}'
    print(parse(source))


main()
