#sudo raspivid -t 999999 -h 720 -w 1080 -fps 25 -hf -b 2000000 -o - | sudo gst-launch-1.0 -v fdsrc ! h264parse ! omxh264dec ! omxh264enc ! mpegtsmux ! hlssink max-files=5  playlist-root=[ip] location=/usr/share/nginx/www/hlssink%05d.ts playlist-location=/usr/share/nginx/www/iplaylist.m3u8 

