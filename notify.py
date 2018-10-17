#!/usr/bin/env python3
import gi
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf
#from subprocess import Popen, PIPE
import urllib, subprocess, sys

title = str(sys.argv[1])
artist = str(sys.argv[2])
album = str(sys.argv[3])
#logic handled by calling bash script, left it maybe for future use
'''
p1 = Popen(["/home/konstantin/Documents/apps/sp", "eval"], stdout=PIPE)
p2 = Popen(["grep", "-oP", "(?<=SPOTIFY_TITLE=.).*(?=\")"], stdin=p1.stdout, stdout=PIPE)
#p1.stdout.close()
title, err = p2.communicate()
title = title.rstrip("\n")
print title

p3 = Popen(["/home/konstantin/Documents/apps/sp", "eval"], stdout=PIPE)
p4 = Popen(["grep", "-oP", "(?<=SPOTIFY_ARTIST=.).*(?=\")"], stdin=p3.stdout, stdout=PIPE)
#p3.stdout.close()
artist, err1 = p4.communicate()
artist = artist.rstrip("\n")
print artist

p5 = Popen(["/home/konstantin/Documents/apps/sp", "art"], stdout=PIPE)
coverurl, err2 = p5.communicate()
print coverurl

file = open("/tmp/url.txt", "r")
cache = file.readline();
print "Cache: " + cache
file.close

if coverurl != cache:
    file = open("/tmp/url.txt","w")
    file.write(coverurl)
    #remove old cover
    exitcode = subprocess.call(["rm", "/home/konstantin/Documents/scripts/sp-cover.png"], stdout=PIPE)
    urllib.urlretrieve(coverurl, "/home/konstantin/Documents/scripts/sp-cover.png")
    print "Cover downloaded"

'''
Notify.init("Spotify Notification")
summary = artist + " - " + album
notification = Notify.Notification.new(
    title,
    summary)

# Use GdkPixbuf to create the proper image type
image = GdkPixbuf.Pixbuf.new_from_file("/home/konstantin/.icons/sp-cover.png")

# Use the GdkPixbuf image
notification.set_icon_from_pixbuf(image)
notification.set_image_from_pixbuf(image)

notification.show()
