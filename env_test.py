import sliding_puzzles

env = sliding_puzzles.make(
    render_mode="human",
    w=3,
    h=3,
    sparse_rewards=True,
    shuffle_steps=18,
    variation="normalized",
)
obs = env.reset()

while True:
    env.render()
    obs, reward, done, trunc, info = env.step(None)
    print(reward)
    if done or trunc:
        print("Done!")
        break

env.close()
