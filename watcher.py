import time
from virustotal import uploadFile
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class Watcher:
    def __init__(self, path, patterns="*.*"):
        self.observer = Observer()
        self.path = path
        self.patterns = patterns

    def run(self):
        event_handler = Handler(self.patterns)
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()


class Handler(PatternMatchingEventHandler):
    def __init__(self, patterns):
        super(Handler, self).__init__(
            patterns=[patterns],
            ignore_patterns=[".tmp", ".file"],
            ignore_directories=True,
            case_sensitive=False,

        )

    def on_created(self, event):
        import virustotal
        uploadFile(event.src_path)
