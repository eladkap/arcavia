from collect_symbols import collect_symbols, write_symbols_to_file


def main():
    symbols = collect_symbols()
    write_symbols_to_file(symbols)

    for symbol in symbols:
        print(f"{symbol['symbol']}: {symbol['meaning']}")


if __name__ == '__main__':
    main()
