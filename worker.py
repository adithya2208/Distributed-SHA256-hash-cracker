#!/usr/bin/python
import gearman,json,hashlib,argparse

parser=argparse.ArgumentParser()
parser.add_argument('server',help='Address of server')
parser.add_argument('-p','--port',help='Port at the server',default='4730')
args=parser.parse_args()


def crack(gearman_worker, gearman_job):
    var=gearman_job.data
    var=json.loads(var)
    hash=var['hash']
    words=var['words']
    for i in words:
        word=i.rstrip().lower()
        hash_object = hashlib.sha256(word)
        hex_dig = hash_object.hexdigest()
        print 'Word:'+i+'Hash:'+hex_dig+'\n'
        if hex_dig==hash:
            return str(word)
    return ""

gm_worker = gearman.GearmanWorker([args.server+':'+args.port])
gm_worker.register_task('crack', crack)
gm_worker.work()