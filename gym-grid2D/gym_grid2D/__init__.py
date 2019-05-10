from gym.envs.registration import register, registry

registereds = registry.all()

def reg(id, entry_point, timestep_limit, nondeterministic=False):
    """ Prevents a gym being registered when it already is. Prevents crash.
    
        Replace the original call to register by reg, which tests whether 
        a gym has already been registered.
    """
    registered = False
    for r in registereds:
        if id in str(r):
            registered = True
            return
    
    if not registered:
        register(id=id, entry_point=entry_point, 
                 timestep_limit=timestep_limit,
                 nondeterministic=nondeterministic)
        
    return
    
reg(
    id='grid-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvSample5x5',
    timestep_limit=2000,
)

reg(
    id='grid-sample-5x5-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvSample5x5',
    timestep_limit=2000,
)

reg(
    id='grid-random-5x5-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvRandom5x5',
    timestep_limit=2000,
    nondeterministic=True,
)

reg(
    id='grid-sample-10x10-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvSample10x10',
    timestep_limit=10000,
)

reg(
    id='grid-random-10x10-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvRandom10x10',
    timestep_limit=10000,
    nondeterministic=True,
)

reg(
    id='grid-sample-3x3-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvSample3x3',
    timestep_limit=1000,
)

reg(
    id='grid-random-3x3-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvRandom3x3',
    timestep_limit=1000,
    nondeterministic=True,
)


reg(
    id='grid-sample-100x100-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvSample100x100',
    timestep_limit=1000000,
)

reg(
    id='grid-random-100x100-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvRandom100x100',
    timestep_limit=1000000,
    nondeterministic=True,
)

reg(
    id='grid-random-10x10-plus-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvRandom10x10Plus',
    timestep_limit=1000000,
    nondeterministic=True,
)

reg(
    id='grid-random-20x20-plus-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvRandom20x20Plus',
    timestep_limit=1000000,
    nondeterministic=True,
)

reg(
    id='grid-random-30x30-plus-v0',
    entry_point='gym_grid2D.envs:Grid2DEnvRandom30x30Plus',
    timestep_limit=1000000,
    nondeterministic=True,
)
