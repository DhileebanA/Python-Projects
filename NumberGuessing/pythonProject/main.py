import random


class GuessGame:
    def __init__(self, lower_limit, upper_limit, max_attempts, difficulty):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.target_number = random.randint(lower_limit, upper_limit)
        self.max_attempts = max_attempts
        self.guesses = 0
        self.score = 0
        self.difficulty = difficulty

    def get_user_guess(self):
        # Task: Complete this function to ask the user to input their guess (within valid range).
        # Hint: Use input() to take user input and handle ValueError for invalid inputs.
        pass

    def calculate_score(self):
        # Task: Implement this function to calculate score based on attempts left.
        # Hint: Base score on remaining attempts, with fewer attempts used leading to a higher score.
        pass

    def provide_hint(self, guess):
        # Task: Add logic to provide hints if the guess is close to the target number.
        # Hint: Check if the guess is within a certain range of the target number.
        pass

    def play(self):
        print(f"Welcome to the Guessing Game! You have {self.max_attempts} attempts.")

        while self.guesses < self.max_attempts:
            user_guess = self.get_user_guess()
            self.guesses += 1

            if user_guess < self.target_number:
                print("Too low! Try again.")
                self.provide_hint(user_guess)
            elif user_guess > self.target_number:
                print("Too high! Try again.")
                self.provide_hint(user_guess)
            else:
                print(
                    f"Congratulations! You've guessed the correct number {self.target_number} in {self.guesses} attempts.")
                self.calculate_score()
                print(f"Your score is {self.score}!")
                return self.score

        print(f"Sorry, you've run out of attempts! The correct number was {self.target_number}.")
        return 0  # Player failed to guess


class GameRunner:
    def __init__(self):
        self.leaderboard = {}

    def select_difficulty(self):
        print("Select a difficulty level:")
        print("1. Easy (1-10, 5 attempts)")
        print("2. Medium (1-100, 10 attempts)")
        print("3. Hard (1-1000, 15 attempts)")

        # Task: Implement difficulty selection logic that returns the appropriate limits and attempts.
        # Hint: Use input() to take the user’s choice and return appropriate values.
        pass

    def update_leaderboard(self, player_name, score, won, difficulty):
        # Task: Complete this function to track wins, losses, and best scores for players.
        # Hint: If the player is new, initialize their record. Update best score if necessary.
        pass

    def display_leaderboard(self):
        # Task: Implement logic to display the leaderboard with player scores, wins, and difficulty level.
        pass

    def start_game(self):
        while True:
            player_name = input("Enter your name: ")
            lower_limit, upper_limit, max_attempts, difficulty = self.select_difficulty()

            print(f"\n{player_name}'s turn!")
            game = GuessGame(lower_limit, upper_limit, max_attempts, difficulty)
            score = game.play()

            won = score > 0
            self.update_leaderboard(player_name, score, won, difficulty)
            self.display_leaderboard()

            if not self.play_again():
                print("Thank you for playing! Goodbye!")
                break

    def play_again(self):
        # Task: Complete this function to ask the player if they want to play again.
        pass


# To run the game (this part remains intact)
if __name__ == "__main__":
    runner = GameRunner()
    runner.start_game()
