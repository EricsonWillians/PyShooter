from actor import enemy

class WaveManager:

    def __init__(self):
        self.max_waves = 10
        self.wave_duration = 60 # segs
        self.spawn_sequence = [
            enemy.EnemyType.WEAK_ZOMBIE
        ]