import numpy as np

import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_grid2D.envs.grid_view_2d import GridView2D


class GridEnv(gym.Env):
    metadata = {
        "render.modes": ["human", "rgb_array"],
    }

    ACTION = ["N", "S", "E", "W"]

    def __init__(self, grid_file=None, grid_size=None, mode=None):

        self.viewer = None

        if grid_file:
            self.grid_view = GridView2D(grid_name="OpenAI Gym - Grid (%s)" % grid_file,
                                        grid_file_path=grid_file,
                                        screen_size=(640, 640))
        elif grid_size:
            if mode == "plus":
                has_loops = True
                n_mushrooms = int(round(min(grid_size)/3))
            else:
                has_loops = False
                n_mushrooms = 0

            self.grid_view = GridView2D(grid_name="OpenAI Gym - Grid (%d x %d)" % grid_size,
                                        grid_size=grid_size, screen_size=(640, 640),
                                        has_loops=has_loops, n_mushrooms=n_mushrooms)
        else:
            raise AttributeError("One must supply either a grid_file path (str) or the grid_size (tuple of length 2)")

        self.grid_size = self.grid_view.grid_size

        # forward or backward in each dimension
        self.action_space = spaces.Discrete(2*len(self.grid_size))

        # observation is the x, y coordinate of the grid
        low = np.zeros(len(self.grid_size), dtype=int)
        high =  np.array(self.grid_size, dtype=int) - np.ones(len(self.grid_size), dtype=int)
        self.observation_space = spaces.Box(low, high)

        # initial condition
        self.state = None
        self.steps_beyond_done = None

        # Simulation related variables.
        self._seed()
        self._reset()

        # Just need to initialize the relevant attributes
        self._configure()

    def __del__(self):
        self.grid_view.quit_game()

    def _configure(self, display=None):
        self.display = display

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        if isinstance(action, int):
            self.grid_view.move_robot(self.ACTION[action])
        else:
            self.grid_view.move_robot(action)

        if np.array_equal(self.grid_view.robot, self.grid_view.goal):
            reward = 1
            done = True
        else:
            reward = -0.1/(self.grid_size[0]*self.grid_size[1])
            done = False

        self.state = self.grid_view.robot

        info = {}

        return self.state, reward, done, info

    def _reset(self):
        self.grid_view.reset_robot()
        self.state = np.zeros(2)
        self.steps_beyond_done = None
        self.done = False
        return self.state

    def is_game_over(self):
        return self.grid_view.game_over

    def _render(self, mode="human", close=False):
        if close:
            self.grid_view.quit_game()

        return self.grid_view.update(mode)

## Class: GridEnv ##

class GridEnvSample5x5(GridEnv):

    def __init__(self):
        super(GridEnvSample5x5, self).__init__(grid_file="grid2d_5x5.npy")


class GridEnvRandom5x5(GridEnv):

    def __init__(self):
        super(GridEnvRandom5x5, self).__init__(grid_size=(5, 5))


class GridEnvSample10x10(GridEnv):

    def __init__(self):
        super(GridEnvSample10x10, self).__init__(grid_file="grid2d_10x10.npy")


class GridEnvRandom10x10(GridEnv):

    def __init__(self):
        super(GridEnvRandom10x10, self).__init__(grid_size=(10, 10))


class GridEnvSample3x3(GridEnv):

    def __init__(self):
        super(GridEnvSample3x3, self).__init__(grid_file="grid2d_3x3.npy")


class GridEnvRandom3x3(GridEnv):

    def __init__(self):
        super(GridEnvRandom3x3, self).__init__(grid_size=(3, 3))


class GridEnvSample100x100(GridEnv):

    def __init__(self):
        super(GridEnvSample100x100, self).__init__(grid_file="grid2d_100x100.npy")


class GridEnvRandom100x100(GridEnv):

    def __init__(self):
        super(GridEnvRandom100x100, self).__init__(grid_size=(100, 100))


class GridEnvRandom10x10Plus(GridEnv):

    def __init__(self):
        super(GridEnvRandom10x10Plus, self).__init__(grid_size=(10, 10), mode="plus")


class GridEnvRandom20x20Plus(GridEnv):

    def __init__(self):
        super(GridEnvRandom20x20Plus, self).__init__(grid_size=(20, 20), mode="plus")


class GridEnvRandom30x30Plus(GridEnv):
    def __init__(self):
        super(GridEnvRandom30x30Plus, self).__init__(grid_size=(30, 30), mode="plus")
