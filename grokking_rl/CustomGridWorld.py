class CustomGridWorld:
    def __init__(self, size=5):
        self.size = size  # size of board
        self.start = (0, 0)
        self.goal = (size - 1, size - 1)  # terminal state
        self.state = self.start # current state should be start
        self.grid = self._build_grid()
        self.actions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        self.gamma = 0.99  # Discount factor

    def _build_grid(self):
        grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        # Customize your grid with obstacles or rewards
        return grid

    def step(self, action):
        # Implement the logic to move the agent and calculate reward
        pass

    def reset(self):
        self.state = self.start
        return self.state

    def render(self):
        # Implement a way to visually display the grid
        pass









env = CustomGridWorld(size=5)
current_state = env.reset()
done = False

while not done:
    action = input("Enter action (up, down, left, right): ")
    next_state, reward, done, _ = env.step(action)
    env.render()
    print(f"Next State: {next_state}, Reward: {reward}, Done: {done}")
