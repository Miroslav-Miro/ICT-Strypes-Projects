class DVDPlayer:
    def on(self):
        print("Starting the DVD player")

    def off(self):
        print("Shutting down DVD player")


class Projector:
    def on(self):
        print("Turning on the projector")

    def off(self):
        print("Turning off the projector")


class SoundSystem:
    def on(self):
        print("Turning on the sound system")

    def off(self):
        print("Turning off the sound system")


class HomeTheaterFacade:
    def __init__(self, dvd, projector, sound):
        self.dvd = dvd
        self.projector = projector
        self.sound = sound

    def watch_movie(self):
        # Facade hides all these setup steps
        self.dvd.on()
        self.projector.on()
        self.sound.on()
        print("Movie is now playing...")

    def end_movie(self):
        self.dvd.off()
        self.projector.off()
        self.sound.off()


theater = HomeTheaterFacade(DVDPlayer(), Projector(), SoundSystem())
theater.watch_movie()
theater.end_movie()
