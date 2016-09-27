##fileToCatch = io.FileIO('.txt')
##if not fileToCatch.read() == '':
##    print 'New Changes, has to restart'
##
##while True:   

class Monkey(object):
    def __init__(self):
        self._cached_stamp = 0
        self.filename = '/path/to/file'

    def ook(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
            
    def bootstreap(self):
        while True:
            pass

import io, time, os, sys, getopt, argparse
from os import walk

__filename__ = __file__.split('\\')[-1]
curDirs = '.'
script = ''

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--script', help='script file to be exdcuted', required=False)
parser.add_argument('-d', '--directory', help='Directory to be tracking', required=False)

args = parser.parse_args()

if hasattr(args,'script'):
    script = args.script or ''

if hasattr(args,'directory'):
    curDirs = args.directory or '.'
    os.chdir(curDirs)
    
print curDirs
root = os.getcwd()
##cdirInfo = os.listdir(curDirs)
walkTree = []
filesToWatch = []
 
def bootstrap():
    global walkTree, filesToWatch
    print 'Start traking '
    for (dirpath, dirnames, filenames) in walk(curDirs):
        if '\\.git' not in dirpath:
            if dirpath == '.': dirpath = ".\\"
            walkTree.extend([{'dir':dirpath, 'dirs':dirnames, 'files':filenames}])
            for filename in filenames:
                if not filename == __filename__:
                    filesToWatch.extend([{'path': dirpath, 'filename':filename, 'stamp': os.stat(dirpath+'\\'+filename).st_mtime}])

def start():
    print 'watching /> ',root, '...'
    while True:
        for fileInfo in filesToWatch:
            stamp = os.stat(fileInfo.get('path')+'\\'+fileInfo.get('filename')).st_mtime
            if not stamp == fileInfo.get('stamp'):
                ## os.system('command to execute')
                print 'This file has changed','\n----'
                print fileInfo.get('path')+'\\'+fileInfo.get('filename')
                os.system(script)
                fileInfo['stamp'] = stamp
                break
        time.sleep(.5)
        
##print sys.argv[1:]
##opts, args = getopt.getopt(sys.argv[1:], "c:")
##print opts, args


bootstrap()
start()
