import pygame


class ThreeFailedPayments(Exception):
    pass


menu = {
    "Classic Hotdog": 3,
    "Spicy Hawtdog": 4,
    "Fries": 2,
    "Fizzy Juice": 1,
    "Golden Caviar Truffle Wurst": 150
}

available_money = 100


class Shop:

    def run_game(self):
        pass

    def __init__(self):
        self.screen = pygame.display.set_mode((1259, 859))
        pygame.display.set_caption("Hotdog shop")

    def buy_item(item, balance, prices):
        return item in prices and balance >= prices[item]

    def here_is_item_and_goodbye_message(item):
        print(f"Here's your {item}!\n")
        print("Thanks for visiting the Hotdog Shop! Have a Nice Day!")

    def retry_payment(item, balance, prices):
        attempts = 1
        while attempts <= 3:
            ask_for_more_money = input(
                "It looks like you're out of money on your card. Can you add any more money? (Y/N) ")
            if ask_for_more_money == "Y":
                # Try for validating additional_money is a float
                try:
                    additional_money = float(input("How much? (please enter numbers ONLY) "))
                    balance += additional_money
                # Exception is raised, print error for wrong value type
                except ValueError:
                    print("Invalid input. Please try again.")

                if item.buy_item(item, balance, prices):
                    item.here_is_item_and_goodbye_message(item)
                    return
                attempts += 1
            else:
                print("Invalid input. Please try again.")

        raise ThreeFailedPayments()

    def hot_dog_shop(self):
        print("\nWelcome to The Hotdog Shop!")
        print("We have many tasty items available. Here's our menu:")
        for item in menu:
            print(f"{item} - £{menu.get(item)}")

        user_selection = input(
            "\nAnything looking tasty? If so, please enter the name of the item you'd like.\nIf not, enter 'exit' to exit the Hotdog Shop.\n")

        try:
            if user_selection == "exit":
                print("Thanks for visiting the Hotdog Shop! Have a Nice Day!")
                return
            elif user_selection in menu.keys():
                if self.buy_item(user_selection, available_money, menu):
                    self.here_is_item_and_goodbye_message(user_selection)
                else:
                    self.retry_payment(user_selection, available_money, menu)
            else:
                raise ValueError("Not a valid answer. Please try again.\n")
        except ValueError as e:
            print(e)
            self.hot_dog_shop()
        except ThreeFailedPayments as e:
            print(e)
            print("Your payment has failed 3 times...please exit the Hotdog Shop. Have a nice day!")


# hot_dog_shop()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    hds = Shop()
    hds.run_game()
