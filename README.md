# Netflix-Vienna-bypass
Link between A1 snd Netflix is undercapacity. At peak hours average throughput to Netflix Vienna can be under 5 mbps. A workaround to this problem is too block or redirect ports from Netflix Vienna to some other Netflix datacenter. Blocking Netflix Vienna during video playback solves the problems but breaks the UI. Redirecting all servers at Vienna datacenter to oen server at FRA2 solves the problem.

Script 
generate_vienna_hostfile_auto.py adds records to hosts file on windows to redirect Netflix Vienna
.
generate_vienna_hostfile_remove.py removes those records 

