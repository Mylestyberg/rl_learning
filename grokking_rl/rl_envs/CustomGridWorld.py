class CustomGridWorld:
    def __init__(self, size=5):
        self.size = size
        self.start = (0, 0)
        self.goal = (size - 1, size - 1)
        self.state = self.start
        self.obstacles = [(1, 1), (2, 2), (3, 3)]  # Example obstacles
        self.actions = ['up', 'down', 'left', 'right'] # possible actions by agen
        # Discount factor, i.e are we myopic or farsighted
        self.gamma = 0.99
        self.grid = self._build_grid()

    def _build_grid(self):
        grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for obstacle in self.obstacles:
            grid[obstacle[0]][obstacle[1]] = -1  # Mark obstacles
        grid[self.goal[0]][self.goal[1]] = 1  # Mark the goal
        return grid

    def step(self, action):
        # Calculate the next state based on the action
        delta = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        next_state = (self.state[0] + delta[action][0], self.state[1] + delta[action][1])

        # Check if the next state is out of bounds or an obstacle
        if 0 <= next_state[0] < self.size and 0 <= next_state[1] < self.size and self.grid[next_state[0]][next_state[1]] != -1:
            self.state = next_state
        reward = -1  # Default reward for each step
        done = self.state == self.goal
        if done:
            reward = 0  # Reward for reaching the goal
        return self.state, reward, done, {}

    def reset(self):
        self.state = self.start
        return self.state

    def render(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.state:
                    print("A", end=" ")  # Agent's current position
                elif (i, j) == self.goal:
                    print("G", end=" ")  # Goal
                elif (i, j) in self.obstacles:
                    print("O", end=" ")  # Obstacles
                else:
                    print(".", end=" ")  # Empty space
            print()  # New line for the next row

