#!/usr/bin/python
#coding:utf-8
import os, shutil,re, time, datetime

markdownpath = "/Users/C/code/yaccai.github.io/_posts"
meta = {
    # '/Users/C/code/leetcode' : {
    #     'sh' : {
    #         'tags' : ['leetcode'],
    #         'desc' : ''
    #     },
    #     'cpp' : {
    #         'tags' : ['leetcode']
    #     },
    #     'sql' : {
    #         'tags' : ['leetcode']
    #     }
    # },
    # '/Users/C/code/lintcode' : {
    #     'java' : {
    #         'tags' : ['lintcode']
    #     },
    #     'cpp' : {
    #         'tags' : ['lintcode']
    #     }
    # }
}


def clearMD(MDpath, postFix): 
    if not os.path.isdir(MDpath) or postFix is None:
        print 'not a folder or no postfix'
        return;
    postFix = postFix + ".md";
    count = 0
    for it in os.listdir(MDpath):
        if os.path.isfile(MDpath + '/' + it) and it.endswith(postFix):
            os.remove(MDpath + '/' + it)
            count = count + 1
    print 'clear ' + ' ' + ("%10s"%postFix) + ("   %-10d" % count)

def makeMD(sourcepath, MDpath, postFix):# like 123.cpp
    if not os.path.isdir(sourcepath) or not os.path.isdir(MDpath) or postFix is None:
        print 'error'
        return;
    count = 0
    for file in os.listdir(sourcepath):
        if file.endswith(postFix) and os.path.isfile(sourcepath + '/' + file):
            num = int( file[:file.find('.')] ) #find the str before the first dot
            Lines = open(sourcepath + '/' + file, 'r').readlines(); 
            Lines[0] = "/**\n"
            secondL = Lines[1][Lines[1].find('http'):].strip('\n').strip('\r')
            main_title = secondL.split('/')[ -2 if secondL[-1] == '/' else -1 ];

            tags = meta[sourcepath][postFix]['tags'];
            prefix = time.strftime('%Y-%m-%d',time.localtime(1430119693 - 100000 * num ))

            fmd  = open(MDpath + '/' + prefix + '-' + ("%03d"%num) + '.' + postFix + '.md','w')
            fmd.write('---\n')
            fmd.write('layout : post\n')
            fmd.write('title  : ' + tags[0] + '--' + ("%03d"%num) + '--' + main_title + '\n')
            fmd.write('Link   : ' + secondL + '\n')
            fmd.write('tags   : ' + ', '.join(tags) + '\n')
            fmd.write('---\n')
            fmd.write('\n```' + postFix + '\n\n')
            for line in Lines:
                fmd.write(line)
            fmd.write('\n\n```')
            fmd.close();

            count = count + 1
    print "created " + str(count) + ' ' + postFix + ' - markdown files'

if __name__ == "__main__":
    Extentions = set();
    for k in meta:
        Extentions.update(meta[k].keys())

    for p in Extentions:
        clearMD(markdownpath,p) #清除之前的版本
        pass;

    for dirs in meta:
        for types in meta[dirs]:
            makeMD(dirs, markdownpath, types);

    os.chdir('/Users/C/code/yaccai.github.io')
    os.system('./run.sh ' + 'p')
