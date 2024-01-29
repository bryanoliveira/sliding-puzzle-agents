import sliding_puzzles

env = sliding_puzzles.make(
    render_mode="human",
    w=2,
    h=2,
    sparse_rewards=True,
    shuffle_steps=100,
    # shuffle_target_reward=-0.5,
    # render_shuffling=True,
    variation="image",
    image_folder="imgs/mnist",
    background_color_rgb=(255, 0, 0)
)
obs = env.reset()
total_reward = 0
while True:
    env.render()
    # print(obs)
    obs, reward, done, trunc, info = env.step(None)
    total_reward += reward
    # print(reward)
    if done or trunc:
        print("Done!", info)
        print("Total reward:", total_reward)
        total_reward = 0
        break

env.close()
