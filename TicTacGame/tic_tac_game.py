import random

from curses.ascii import isalnum

class TicTacGame:
    board = []
    leaderboard = {}
    player = "X"
    playerName1 = ""
    playerName2 = ""
    robotName = "robot"
    robotGenious = "genious"
    currentPlayer = ""
    tie = False

    def __init__(self):
        for i in range(9):
            self.board.append(i)


    def validate_num(self, val: str) -> None:
        while True:
            try:
                val = int(val)
                break
            except ValueError:
                print("It's not a number")  
                val = input()
                continue
        return val


    def show_menu(self) -> None:
        print("1) start game\n2) leaderboard\n3) instruction\n4) exit")
        val = 0
        while True:
            val = input()
            val = self.validate_num(val)
            if 1 <= val <= 4:
                break
            print("Enter a number from 1 to 4")
        match val:
            case 1:
                self.start_game()
            case 2:
                self.show_leadreboard()
                self.show_menu()
            case 3:
                self.show_instruction()
                self.show_menu()
            case 4:
                self.exit()


    def show_leadreboard(self) -> None:
        print("---leaderboard---")
        for key, value in self.leaderboard.items():
            print(str(key) + ": ", value)


    def show_instruction(self) -> None:
        print("There are no instructions xD")

    def exit(self) -> None:
        print("Waiting for your return :)")


    def start_game(self) -> None:
        print("1) play vs person\n2) play vs computer")
        val = 0
        while True:
            val = input()
            val = self.validate_num(val)
            if 1 <= val <= 2:
                break
            print("Enter a number from 1 to 2")
        match val:
            case 1:
                self.start_game_vs_person()
            case 2:
                self.start_game_vs_computer()


    def _add_person(self, name: str) -> None:
        while True:
            if name == "vsRobot":
                playerName = input("Enter your name: ")
            else:
                playerName = input(f"Enter the name of the {name} player: ")
            if playerName == self.robotName:
                print("This name is used by the computer, choose another :)")
            elif playerName == '':
                print("emptyname :)")
            else:
                break

        playerName.strip()
        if playerName not in self.leaderboard:
            self.leaderboard[playerName] = 0
        if name in ["first", "vsRobot"]:
            self.playerName1 = playerName
        if name == "second":
            self.playerName2 = playerName


    def _choose_first_started(self) -> None:
        print(f"Who goes first? ({self.playerName1}/{self.playerName2})")
        while True:
            ans = input()
            if ans == self.playerName1:
                self.currentPlayer = self.playerName1
                break
            elif ans == self.playerName2:
                self.currentPlayer = self.playerName2
                break
            else:
                print("Incorrect input")


    def _choose_sign(self) -> None:
        while True:
            sign = input(f"{self.currentPlayer} choose your sign (X or O): ")
            if sign.upper() == "X":
                self.player = "X"
                break
            elif sign.upper() == "O":
                self.player = "O"
                break
            else:
                print("This is not correct sign")


    def _validate_players_info(self) -> None:
        self._add_person("first")
        self._add_person("second")
        self._choose_first_started()
        self._choose_sign()


    def _change_player(self) -> None:
        if self.player == "O":
            self.player = "X"
        else:
            self.player = "O"
        if self.currentPlayer == self.playerName1:
            self.currentPlayer = self.playerName2
        else:
            self.currentPlayer = self.playerName1


    def _reset(self) -> None:
        for i in range(9):
            self.board[i] = i
        self.tie = False

    def _rescore(self) -> None:
        if not self.tie:
            self.leaderboard[self.currentPlayer] += 1


    def _next_game(self) -> bool:
        print("Do u wanna play one more game or back to menu? (play/menu)")
        self._reset()
        while True:
            ans = input()
            if ans == "play":
                return True
            elif ans == "menu":
                return False
            else:
                print("Incorrect input")


    def _check_tie(self) -> bool:
        checker = 0
        for i in range(9):
            if isalnum(self.board[i]):
                checker += 1
        if checker == 9:
            self.tie = True
        return self.tie


    def __game_process(self) -> None:
        while True:
            if self._check_tie():
                break
            self.show_board()
            if self.currentPlayer == self.robotName:
                self._robot_move()
            else:
                self._validate_input()
            if (self.check_winner()):
                break
            self._change_player()
        self.show_board()
        if not self.tie:
            print(f"{self.currentPlayer} win this round!")
        else:
            print("It's tie")


    def start_game_vs_person(self) -> None:
        self._validate_players_info()
        self.__game_process()
        self._rescore()
        while self._next_game():
            self._choose_first_started()
            self._choose_sign()
            self.__game_process()
            self._rescore()
        self._reset()
        self.show_menu()


    def __add_computer(self) -> None:
        self.playerName2 = self.robotName
        if self.robotName not in self.leaderboard:
            self.leaderboard[self.robotName] = 0


    def _choose_sign_with_robot(self) -> None:
        while True:
            name = self.playerName2 if self.currentPlayer == self.robotName == self.playerName1 else self.playerName1
            sign = input(f"{name} choose your sign (X or O): ")
            if sign.upper() == "X":
                if self.currentPlayer == self.robotName:
                    self.player = "O"
                else:
                    self.player = "X"
                break
            elif sign.upper() == "O":
                if self.currentPlayer == self.robotName:
                    self.player = "X"
                else:
                    self.player = "O"
                break
            else:
                print("This is not correct sign")


    def _validate_player_info_vs_pc(self) -> None:
        self._add_person("vsRobot")
        self.__add_computer()
        self._choose_first_started()
        self._choose_sign_with_robot()


    def _robot_move(self) -> None:
        while True:
            num = random.randint(0, 8)
            if not isalnum(self.board[num]):
                self.board[num] = self.player
                break
        print(f"robot move: {num}")


    # def __genious_first_step__(self):
    #     self.board[4] = self.currentPlayer


    # def __genious_second_step__(self, scenario: list):
    #     if self.currentPlayer == "X":
    #         opponents_sign = "O"
    #     else:
    #         opponents_sign = "X"
    #     opponents_num = -1
    #     for i in range(0, 9):
    #         if self.board[i] == opponents_sign:
    #             opponents_num = i

    #     if opponents_num % 2 == 0:
    #         scenario.remove(6)
    #         scenario.remove(7)
    #     else:
    #         for i in range(1, 6):
    #             scenario.remove(i)

    #     if opponents_num == 0:
    #         self.board[8] = self.currentPlayer
    #     if opponents_num == 8:
    #         self.board[0] = self.currentPlayer
    #     if opponents_num == 2:
    #         self.board[6] = self.currentPlayer
    #     if opponents_num == 6:
    #         self.board[2] = self.currentPlayer

    #     if opponents_num == [1, 2]:
    #         self.board[0] = self.currentPlayer
    #     if opponents_num == [4, 5]:
    #         self.board[8] = self.currentPlayer


    # def __genious_third_step__(self, scenario: list):
    #     pass

    # def __genious_fourth_step__(self, scenario: list):
    #     pass

    # def __genious_fifth_step__(self, scenario: list):
    #     pass


    # def __robot_genious_first__(self):
    #     """"""""
    #     checkStep = 0
    #     for i in range(9):
    #         if not isalnum(self.board[i]):
    #             checkStep += 1

    #     scenario = [1, 2, 3, 4, 5, 6, 7]
    #     match checkStep:
    #         case 9:
    #             self.__genious_first_step__()
    #         case 7:
    #             self.__genious_second_step__(scenario)
    #         case 5:
    #             self.__genious_third_step__(scenario)
    #         case 3:
    #             self.__genious_fourth_step__(scenario)
    #         case 1:
    #             self.__genious_fifth_step__(scenario)


    def start_game_vs_computer(self) -> None:
        self._validate_player_info_vs_pc()
        self.__game_process()
        self._rescore()
        while self._next_game():
            self._choose_first_started()
            self._choose_sign_with_robot()
            self.__game_process()
            self._rescore()
        self._reset()
        self.show_menu()


    def _validate_input(self) -> None:
        while True:
            num = input(f"{self.currentPlayer} enter a number from 0 to 8: ")
            num = self.validate_num(num)
            if 0 <= num < 9:
                if isalnum(self.board[num]):
                    print("This cell is already taken")
                else:
                    self.board[num] = self.player
                    break
            else:
                print("This number is not in the correct range")


    def check_winner(self) -> bool:
        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] or self.board[i] == self.board[3 + i] == self.board[2 * 3 + i]:
                return True
        if self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]:
            return True
        return False

    def show_board(self) -> None:
        for i in range(3):
            print("-" * 13)
            print("| ", end="")
            for j in range(3):
                print(self.board[i * 3 + j], end=" | ")
            print()
        print("-" * 13)


if __name__ == '__main__':
    game = TicTacGame()
    try:
        game.show_menu()
    except (KeyboardInterrupt, EOFError):
        game.exit()