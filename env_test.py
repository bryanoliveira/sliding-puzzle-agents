import sliding_puzzles

env = sliding_puzzles.make(w=2, h=2, render_mode="human", sparse_rewards=True)
obs = env.reset()

while True:
    env.render()
    obs, reward, done, trunc, info = env.step(None)
    print(reward)
    if done or trunc:
        print("Done!")
        break

env.close()
