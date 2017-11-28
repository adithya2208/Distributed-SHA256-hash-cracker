#!/usr/bin/python
import gearman,argparse,hashlib,json,subprocess,time

def check_request_status(job_request):

    if job_request.complete:
        if job_request.result!='':
            print "Job %s finished!  Result: %s-%s" % (job_request.job.unique, job_request.state, job_request.result)
            return 2
        return 1
    elif job_request.timed_out:
        print "Job %s timed out!" % job_request.unique
    elif job_request.state == JOB_UNKNOWN:
        print "Job %s connection failed!" % job_request.unique

def main():
        
    parser=argparse.ArgumentParser()
    parser.add_argument('wordlist',help='Enter path to worldlist')
    parser.add_argument('hash',help='Enter path to hash')
    parser.add_argument('server',help='Address of server')
    parser.add_argument('-p','--port',help='Port at the server',default='4730')
    parser.add_argument('-b','--batchsize',help='Number of items in a batch from the wordlist to send to the client')
    args=parser.parse_args()
    gm_client = gearman.GearmanClient([args.server+':'+args.port])


    queue=list()
    with open(args.hash,'r') as f:
        password=f.read()
        password=password.rstrip().lower()

    with open(args.wordlist,'r') as f:
        words=f.readlines()

    i=0
    batchsize=int(args.batchsize)
    num_of_words=len(words)
    flag=0
    while True:
        
        data_to_send=words[i:i+batchsize]
        data_to_send={"hash":password,"words":data_to_send}
        data_to_send=json.dumps(data_to_send)
        job_request = gm_client.submit_job("crack", data_to_send)
        print data_to_send
        queue.append(job_request)
        i=i+batchsize
        if i>num_of_words:
            i=num_of_words
            flag=1
        if flag:
            break
        for j in queue:
            return_val=check_request_status(j)
            if return_val==1:
                queue.remove(j)
            if return_val==2:
                return 0
                             
    print 'Password is not in the given wordfile or is not encrypted using SHA256'

if __name__=="__main__":
    main()