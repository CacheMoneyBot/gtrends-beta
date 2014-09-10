#!/usr/bin/python3
# encoding: utf-8

import os, time

def findProcess(processName):
    import subprocess
    ps = subprocess.Popen("ps -ef | grep "+processName,
        shell=True, stdout=subprocess.PIPE)
    output = ps.stdout.read().decode('utf-8').split('\n')
    dropboxd = [x for x in output if 'grep' not in x and x!='']
    ps.stdout.close()
    ps.wait()
    return dropboxd

if not findProcess('dropbox-dist'):
    ans = input("Start dropbox-dist service? Y/N: ")
    if ans == 'Y':
        print("Starting ~/.dropbox-dist/dropboxd process...")
        os.system("~/.dropbox-dist/dropboxd")
        time.sleep(4)

# python3 ~/Dropbox/gtrends-beta/gtrends_ioi.py


cat_codes = ['0-7', '0', '0-12', '0-7-107', '0-12-784']
categories = ['finance', 'all', 'business_industrial', 'investing', 'business-news']

# 0-7 -> finance
# 0-7-107 -> investing
# 0-12-784 -> business-news
# 0-7-37 -> banking
# 0 -> all
# 0-12-1138-1139 -> investment-banking
# 0-12: Business & Industrial


categories = list(zip(cat_codes, categories))


for ccode, category in categories:
    # Firms names
    syscall = """python3 $base_dir/google_trends/trends.py \
        --username $GMAIL_USER \
        --password justfortesting! \
        --throttle "random" \
        --cik-file $base_dir/cik-ipo/cik-ipos.csv  \
        --output $base_dir/cik-ipo/{category} \
        --category {ccode}""".format(category=category, ccode=ccode)
    os.system(syscall)



# for ccode, category in categories:
#     # Underwriters
#     syscall = """python $base_dir/google_trends/trends.py \
#         --username $GMAIL_USER \
#         --password justfortesting! \
#         --throttle "random" \
#         --quiet-io "true" \
#         --cik-file $base_dir/ipo-uw/ipo-uw.csv  \
#         --output $base_dir/ipo-uw/{category} \
#         --category {ccode}""".format(category=category, ccode=ccode)
#     os.system(syscall)




######################################################

"""
    python3 $base_dir/google_trends/trends.py \
        --username $GMAIL_USER \
        --password justfortesting! \
        --category 0 \
        --quarterly "2013-12" \
        --keyword "SolarCity"
"""


"""python3 $base_dir/google_trends/trends.py \
        --username dgtesting12@gmail.com \
        --password justfortesting! \
        --throttle "random" \
        --cik-file $base_dir/ipo-uw/ipo-uw.csv  \
        --output $base_dir/ipo-uw2/all \
        --category 0"""




