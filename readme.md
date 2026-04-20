# 🤖 Numerical Tic-Tac-Toe: Q-Learning Agent
**Surgical Reinforcement Learning for Stochastic Game Environments**

[![Tested on Gemini](https://img.shields.io/badge/Tested_on-Gemini_CLI-8E44AD?style=for-the-badge&logo=google-gemini&logoColor=white)](https://github.com/google/gemini-cli)
[![Tech Stack: Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Library: NumPy](https://img.shields.io/badge/Library-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Numerical Tic-Tac-Toe** is a reinforcement learning project that implements a **Q-Learning** agent capable of winning a variant of Tic-Tac-Toe using numbers 1-9. The agent learns to optimize its strategy against a stochastic environment through episodic exploration and exploitation.

`✅ RL Agent Training | ✅ Stochastic Environment | ✅ MIT Licensed | ✅ Jupyter Notebook Hub`

## 🏗 Architecture
The system is built with a decoupled Environment-Agent architecture, following the standard RL Markov Decision Process (MDP) framework.

```mermaid
graph TD
    A[Agent] --> B[Epsilon-Greedy Strategy]
    B --> C[Action Selection]
    C --> D[Environment]
    D --> E[State Transition]
    E --> F[Reward Calculation]
    F --> G[Q-Value Update]
    G --> A
```

### Core Components
- **Environment (`TCGame_Env.py`)**: Implements the game logic, including `is_winning`, `is_terminal`, and stochastic opponent moves.
- **Agent Hub (`TicTacToe_Agent.ipynb`)**: Contains the Q-learning algorithm, hyperparameter tuning, and convergence tracking logic.
- **State Manager**: Handles the conversion of 3x3 grid states into hashable formats for the Q-table.
- **Convergence Engine**: Tracks state-action pairs over thousands of episodes to ensure policy stability.

## 🚀 Getting Started

1. **Install Dependencies**:
   ```bash
   pip install numpy jupyter
   ```

2. **Run the Agent**:
   Open `TicTacToe_Agent.ipynb` in Jupyter Notebook and execute the cells to start training.

3. **Verify Convergence**:
   Check the plots at the end of the notebook to visualize the Q-value stabilization.

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
*Built with ❤️ for Intelligent Game Design.*
