import sliding_puzzles

env = sliding_puzzles.make(
    render_mode="human",
    w=2,
    h=2,
    sparse_rewards=True,
    sparse_mode=sliding_puzzles.env.SparseMode.invalid_and_win,
    shuffle_steps=50,

    variation="normalized",

    # variation="image",
    # image_folder="./imgs/mnist/",
)

obs = env.reset()
total_reward = 0
while True:
    env.render()
    obs, reward, done, trunc, info = env.step(None)
    total_reward += reward
    print(reward)
    if done or trunc:
        print("Done! ", total_reward)
        total_reward = 0
        obs = env.reset()

env.close()
