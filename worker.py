#!/usr/bin/python
import gearman,json,hashlib
gm_worker = gearman.GearmanWorker(['127.0.0.1:4730'])

def crack(gearman_worker, gearman_job):
    var=gearman_job.data
    var=json.loads(var)
    var['password']=var['password'].rstrip()
    var['password']=var['password'].lower()
    hash_object = hashlib.sha256(var['password'])
    hex_dig = hash_object.hexdigest()
    print var['password'],'->',hex_dig
    if hex_dig==var['hash']:
         return str(var['password'])
    return ""


# gm_worker.set_client_id is optional
gm_worker.set_client_id('python-worker1')
gm_worker.register_task('crack', crack)

# Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
gm_worker.work()