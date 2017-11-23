#!/usr/bin/python
import gearman,argparse,hashlib,json,subprocess,time
def check_request_status(job_request):

    if job_request.complete:
        if job_request.result!='':
            print "Job %s finished!  Result: %s - %s" % (job_request.job.unique, job_request.state, job_request.result)
    elif job_request.timed_out:
        print "Job %s timed out!" % job_request.unique
    elif job_request.state == JOB_UNKNOWN:
        print "Job %s connection failed!" % job_request.unique





parser=argparse.ArgumentParser(description='Hello')
parser.add_argument('-w','--wordlist',help='enter path to worldlist',action='store',default=False,dest='wl')
parser.add_argument('-f','--file',help='enter path to hash',action='store',default=False,dest='hash')
args=parser.parse_args()
if args.wl==False:
    print 'Enter wordlist (-w parameter)'
    exit
if args.hash==False:
    print 'Enter hash file (-f parameter)'
    exit  
gm_client = gearman.GearmanClient(['127.0.0.1:4730'])
queue=list()
start=time.time()
with open(args.hash,'r') as f:
    password=f.read()
    password=password.lower()
with open(args.wl,'r') as f:
    for x in f:
        p1={"hash":password,"password":x}
        p1=json.dumps(p1)
        job_request = gm_client.submit_job("crack", p1)
        queue.append(job_request)

for i in queue:
    check_request_status(i)
print 'Program completed in ',time.time()-start,"Seconds"
print 'If you don\'t see the result, then the password is not in the given wordfile or is encrypted not using SHA256'