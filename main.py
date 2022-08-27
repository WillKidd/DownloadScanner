import watcher

if __name__ == "__main__":
    with open ("config.txt", "r") as conf:
        path = rf"{conf.readlines()[1]}"
    w = watcher.Watcher(path)
    w.run()