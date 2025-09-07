import argparse
from src.task2_income_generator import generator_numbers, sum_profit

def main():
    p = argparse.ArgumentParser(description="Parse income numbers from text and sum them.")
    p.add_argument("text", type=str, help="Вхідний текст у лапках")
    args = p.parse_args()

    total = sum_profit(args.text, generator_numbers)
    print(f"Загальний дохід: {total}")

if __name__ == "__main__":
    main()
