jobs_file = open("jobs1.txt","r") 
#if it on any anther mode with readable fancation it will be false
print(jobs_file.readable())
#print(jobs_file.read())
#print(jobs_file.readline())
#print(jobs_file.readlines())
#print(jobs_file.readlines()[1])
for job in jobs_file.readlines():
    print(job + "is my faver job")
jobs_file.close()