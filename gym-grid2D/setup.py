from setuptools import setup

setup(name="gym_grid2D",
      version="0.1",
      url="https://github.com/rnoldr/gym_grid2D",
      author="RnoldR",
      license="MIT",
      packages=["gym_grid2D", "gym_grid2D.envs"],
      package_data = {
          "gym_grid2D.envs": ["grid_samples/*.npy"]
      },
      install_requires = ["gym", "pygame", "numpy"]
)
