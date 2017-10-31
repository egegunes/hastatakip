import os.path
import glob


conffiles = glob.glob(os.path.join(os.path.dirname(__file__), 'settings', '*.conf'))
conffiles.sort()

for f in conffiles:
    exec(open(os.path.abspath(f)).read())
