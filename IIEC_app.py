#!/usr/bin/python3 


import cgi
import subprocess as sb

print("content-type: text/html")
print()


a = cgi.FieldStorage()
cmd = a.getvalue("x")


if (("run" in cmd) or ("what" in cmd) or ("today's" in cmd) or ("execute" in cmd))and (("date" in cmd)):
    x = sb.getoutput("date")
    print(x)
    sb.getoutput("espeak-ng `date`")
elif (("month" in cmd) or ("what" in cmd) or ("execute" in cmd)or ("today's" in cmd))and (("cal" in cmd) or ("calendar" in cmd)):
    x = sb.getoutput(" cal")
    print(x)
    sb.getoutput(" espeak-ng `cal`")
elif (("hadoop" in cmd))and (("version" in cmd)):
    x = sb.getoutput("hadoop version")
    print(x)
    sb.getoutput(" espeak-ng 'hadoop version'")
elif (("java" in cmd))and (("version" in cmd)):
    x = sb.getoutput(" java -version")
    print(x)
    sb.getoutput(" espeak-ng 'java version'")
elif (("docker" in cmd))and (("version" in cmd)):
    x = sb.getoutput(" docker version")
    print(x)
    sb.getoutput(" espeak-ng 'docker version'")
elif (("python" in cmd))and (("version" in cmd)):
    x = sb.getoutput("python3 -V")
    print(x)
    sb.getoutput(" espeak-ng '`python3 -V`'")
elif (("open" in cmd))and (("firefox" in cmd)):
    x = sb.getoutput(" espeak-ng 'sorry not supported now'")
    print(x)
elif (("launch" in cmd))and (("docker" in cmd) or ("container" in cmd)):
    x = sb.getoutput("docker run -dit --name os ubuntu ")
    print(x)
    sb.getoutput(" espeak-ng 'container launched'")
elif (("show" in cmd) or ("running" in cmd))and (("docker" in cmd) or ("container" in cmd)):
    x = sb.getoutput(" docker ps")
    print(x)
    sb.getoutput(" espeak-ng 'running container'")
elif (("remove" in cmd) or ("delete" in cmd))and (("docker" in cmd) or ("container" in cmd)):
    x = sb.getoutput(" docker rm -f os")
    print(x)
    sb.getoutput(" espeak-ng 'container removed'")
elif (("initialize" in cmd) or ("install" in cmd))and (("terraform" in cmd) or ("plugins" in cmd)):
    x = sb.getoutput(" terraform init")
    print(x)
    sb.getoutput(" espeak-ng 'plugin installed'")
elif (("working" in cmd) or ("track" in cmd))and (("terraform" in cmd) or ("plan" in cmd)):
    x = sb.getoutput(" terraform plan")
    print(x)
    sb.getoutput(" espeak-ng 'good'")
elif (("validate" in cmd) or ("correct" in cmd))and (("terraform" in cmd) or ("code" in cmd)):
    x = sb.getoutput("terraform validate")
    print(x)
    sb.getoutput(" espeak-ng 'successful'")
elif (("run" in cmd) or ("apply" in cmd))and (("terraform" in cmd) or ("code" in cmd)):
    x = sb.getoutput(" terraform apply --auto-approve")
    print(x)
    sb.getoutput(" espeak-ng 'setup done'")
elif (("delete" in cmd) or ("destroy" in cmd))and (("terraform" in cmd) or ("setup" in cmd)):
    x = sb.getoutput(" terraform destroy --auto-approve")
    print(x)
    sb.getoutput(" espeak-ng 'setup removed'")
elif (("check" in cmd) or ("send" in cmd))and (("connectivity" in cmd) or ("packets" in cmd) or ("google" in cmd)):
    x = sb.getoutput(" ping -c 4 8.8.8.8")
    print(x)
    sb.getoutput(" espeak-ng 'yes it is working good'")
elif ("exit" in cmd) or ("quit" in cmd):
	x = sb.getoutput("espeak-ng 'Have a nice day sir...'")
	print("Have a nice dir sir... :)")
else:
    sb.getoutput(" espeak-ng 'your enter wrong text.'")
    print("Your Enter Wrong Text, so please enter valid text !!")
