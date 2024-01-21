from stable_baselines3.common.callbacks import BaseCallback

class SuccessRateCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(SuccessRateCallback, self).__init__(verbose)

    def _on_step(self) -> bool:
        return True

    def _on_rollout_end(self) -> None:
        episodes = len(self.locals["infos"])
        
        if episodes > 0:
            successes = 0
            for i_info in self.locals["infos"]:
                if i_info.get("is_success"):
                    successes += 1

            success_rate = successes / episodes
            self.logger.record("rollout/success_rate", success_rate)