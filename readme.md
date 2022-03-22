# Numerical Tic-Tac-Toe Agent
- You can play the game [here](https://www.flashgamesplayer.com/free/numeric-tic-tac-toe/play.html) to understand the rules
- Build an RL agent (using Q-learning) that learns to play Numerical Tic-Tac-Toe with odd numbers. 
- The environment is playing stochastically (randomly) with the agent, i.e. its strategy is to put an even number randomly in an empty cell. 

### Agent
The following is the layout of the agent notebook:
- Defining epsilon-greedy strategy
- Tracking state-action pairs for convergence
- Define hyperparameters for the Q-learning algorithm
- Generating episode and applying Q-update equation
- Checking convergence in Q-values

### Environment
The environment has the following functions:
- `is_winning`: lets us know if agent or environment won the game
- `is_terminal`: whether game ended (win/tie) or not
- `allowed_positions`: list of cells that have not yet been filled up
- `allowed_values`: numbers that have not yet been played. agent will have list of odd numbers while environment will have list of even numbers
- `action_space`: all possible actions i.e. combination of allowed positions and allowed values
- `state_transition`: new state from current state and action
- `step`: based on action of agent, decides if game is ended. if game is supposed to continue, then environment takes an action as well.
