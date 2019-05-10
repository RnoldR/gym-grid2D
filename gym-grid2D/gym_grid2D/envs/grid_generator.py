import os
from gym_grid2D.envs.grid_view_2d import Grid

if __name__ == "__main__":

    # check if the folder "grid_samples" exists in the current working directory
    dir_name = os.path.join(os.getcwd(), "grid_samples")
    if not os.path.exists(dir_name):
        # create it if it doesn't
        os.mkdir(dir_name)

    # increment number until it finds a name that is not being used already (max grid_999)
    grid_path = None
    for i in range(1, 1000):
        grid_name = "grid2D_%03d.npy" % i
        grid_path = os.path.join(dir_name, grid_name)
        if not os.path.exists(grid_path):
            break
        if i == 999:
            raise ValueError("There are already 999 grids in the %s." % dir_name)

    grid = Grid(grid_size=(5, 5))
    grid.save_grid(grid_path)
    print("New grid generated and saved at %s." %  grid_path)

