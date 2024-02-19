class ValueIteration:
    def __init__(self, env, theta=0.0001, gamma=0.99):
        self.env = env
        self.theta = theta  # A small threshold for determining convergence
        self.gamma = gamma  # Discount factor
        self.V = [[0 for _ in range(env.size)] for _ in range(env.size)]  # Initialize state values to zero

    def run(self):
        while True:
            delta = 0  # Initialize delta to zero for this iteration
            for i in range(self.env.size):
                for j in range(self.env.size):
                    v = self.V[i][j]  # Save the current value of the state
                    self.V[i][j] = self.calculate_state_value((i, j))  # Update the state value
                    delta = max(delta, abs(v - self.V[i][j]))  # Check if this is the largest change in value
            if delta < self.theta:  # Check for convergence
                break

    def calculate_state_value(self, state):
        if state == self.env.goal:
            return 0  # Goal state value is zero
        value = float('-inf')  # Initialize value to negative infinity
        for action in self.env.actions:
            self.env.state = state  # Set environment to the current state
            next_state, reward, done, _ = self.env.step(action)  # Take the action
            # Calculate the value as the max of the current value and the reward + value of next state
            value = max(value, reward + self.gamma * self.V[next_state[0]][next_state[1]])
        return value

    def get_values(self):
        return self.V

    def print_values(self):
        for row in self.V:
            print(' '.join(f'{value:.2f}' for value in row))









