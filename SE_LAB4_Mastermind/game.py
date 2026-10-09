import random
from logic import feedback


class Mastermind:
    DIFFICULTIES = {
        "easy": {
            "length": 3,
            "symbols": "1234",
            "turns": 12,
        },
        "medium": {
            "length": 4,
            "symbols": "123456",
            "turns": 10,
        },
        "hard": {
            "length": 5,
            "symbols": "12345678",
            "turns": 8,
        },
    }

    def __init__(self):
        self.history = []
        self.game_over = False
        self.choose_difficulty()

    def choose_difficulty(self):
        print("Choose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choices = {
            "1": "easy",
            "2": "medium",
            "3": "hard",
        }

        while True:
            choice = input("Enter choice (1-3): ").strip()

            if choice in choices:
                self.difficulty = choices[choice]
                config = self.DIFFICULTIES[self.difficulty]

                self.length = config["length"]
                self.symbols = config["symbols"]
                self.turns = config["turns"]

            self.code = [
                    random.choice(self.symbols)
                    for _ in range(self.length)
                ]
            #print("DEBUG SECRET:", "".join(self.code))

            print(
                    f"\nDifficulty: {self.difficulty.capitalize()}"
                )
            print(
                    f"Enter {self.length} digits from "
                    f"{self.symbols[0]} to {self.symbols[-1]}."
                )
            print(f"You have {self.turns} turns.\n")
            return

            print("Invalid choice. Enter 1, 2, or 3.")

    def run(self):
        while self.turns > 0 and not self.game_over:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.game_over = True
                print("Game quit.")
                return

            if (
                len(raw) != self.length
                or any(ch not in self.symbols for ch in raw)
            ):
                print(
                    f"Enter exactly {self.length} digits from "
                    f"{self.symbols[0]} to {self.symbols[-1]}."
                )
                continue

            guess = list(raw)
            exact, partial = feedback(self.code, guess)

            self.history.append((raw, exact, partial))
            self.turns -= 1

            print("Exact:", exact, " Partial:", partial)

            print("Guess history:")
            for turn, (
                previous_guess,
                previous_exact,
                previous_partial
            ) in enumerate(self.history, start=1):
                print(
                    f"{turn}. {previous_guess} -> "
                    f"Exact: {previous_exact}, Partial: {previous_partial}"
                )

            if exact == self.length:
                print("Cracked the code!")
                self.game_over = True
                return

        if not self.game_over:
            print("Out of turns!")
            print("The code was", "".join(self.code))
            self.game_over = True