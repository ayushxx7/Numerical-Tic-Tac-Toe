import numpy as np
import random
from itertools import groupby
from itertools import product



class TicTacToe():

    def __init__(self):
        """initialise the board"""

        # initialise state as an array (board positions)
        self.state = [np.nan for _ in range(9)]

        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)]

        self.reset()


    def is_winning(self, curr_state):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        winning_pattern = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

        for pattern in winning_pattern:
            if not np.isnan(curr_state[pattern[0]]) and not np.isnan(curr_state[pattern[1]]) and not np.isnan(curr_state[pattern[2]]):
                pattern_state = curr_state[pattern[0]] + curr_state[pattern[1]] + curr_state[pattern[2]]
                if pattern_state == 15:
                    return True
        return False

    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up

        if self.is_winning(curr_state) == True:
            return True, 'Win'

        elif len(self.allowed_positions(curr_state)) == 0:
            return True, 'Tie'

        else:
            return False, 'Resume'


    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]

        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)



    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        # print('state trans. curr_state:', curr_state, 'curr_action:', curr_action)
        curr_state[curr_action[0]] = curr_action[1]
        # print('after applying', curr_state)
        return curr_state


    def step(self, curr_state, curr_action):
        """Takes current state and action and returns the next state, reward and whether the state is terminal. Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""

        agent_move = self.state_transition(curr_state, curr_action)
        # print('STEP::curr state', curr_state, 'curr action', curr_action)
        if self.is_winning(agent_move):
            return (agent_move, 10, True)

        elif len(self.allowed_positions(agent_move)) == 0:
            return (agent_move, 0, True)

        else:
            env_move = random.choice(self.allowed_positions(agent_move))
            env_action = random.choice(self.allowed_values(agent_move)[1])
            env_move = self.state_transition(curr_state, [env_move, env_action])
            if self.is_winning(env_move):
                return (env_move, -10, True)

            elif len(self.allowed_positions(env_move)) == 0:
                return (env_move, 0, True)

            else:
                return (env_move, -1, False)


    def reset(self):
        return self.state


if __name__ == "__main__":
    nan = np.nan
    inp = [9, 2, nan, nan, nan, nan, nan, nan, nan]
    action = [2, 4]

    tic_tac_toe = TicTacToe()

    tic_tac_toe.state = inp

    print(tic_tac_toe.state)

    o = tic_tac_toe.step(tic_tac_toe.state, action)

    print(o)
