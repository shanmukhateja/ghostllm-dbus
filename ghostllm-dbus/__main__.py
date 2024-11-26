import sys

from .server import GhostLLMDBus

if __name__ == '__main__':
    try:
        gh = GhostLLMDBus()
        gh.listen()
    except KeyboardInterrupt:
        sys.exit(0)