class Pifagor:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self.generator()

    def generator(self):
        for a in range(1, self.limit):
            for b in range(a, self.limit):
                try:
                    c = (a**2 + b**2) ** 0.5
                    if c.is_integer() and c <= self.limit:
                        yield (a, b, int(c))
                except OverflowError:
                    continue
                except Exception as e:
                    print(f"Error!: {e}")

def main():
    try:
        limit = int(input("Raqam kiriting: "))
        if limit < 1:
            raise ValueError("Chegara 1 dan katta bo'lishi kerak")
        pifagor = Pifagor(limit)
        print("Pifagor sonlari:")
        for i in pifagor:
            print(f"pifagor sonlar {i}")
    except ValueError as error:
        print(f"Error!: {error}")

if __name__ == "__main__":
    main()
