## Ubuntu 分辨率设置
> 最近使用Ubuntu时遇到个问题，使用2k屏幕的时发现没有2560*1440分辨率，显示效果就很难受，于是查了下，发现可以使用xrandr命令设置分辨率，本文内容主要转载自[Ubuntu添加2560x1440分辨率](https://blog.jianchihu.net/ubuntu-add-2560x1440.html)
- 1.使用xrandr 查看当前显示器所有分辨率，其中virtual1 是显示器的名字
``` bash
~ xrandr
Screen 0: minimum 1 x 1, current 2560 x 1440, maximum 16384 x 16384
Virtual1 connected primary 2560x1440+0+0 (normal left inverted right x axis y axis) 0mm x 0mm
   800x600       60.00 +  60.32  
   2560x1600     59.99  
   1920x1440     60.00  
   1856x1392     60.00  
   1792x1344     60.00  
   1920x1200     59.88  
   1600x1200     60.00  
   1680x1050     59.95  
   1400x1050     59.98  
   1280x1024     60.02  
   1440x900      59.89  
   1280x960      60.00  
   1360x768      60.02  
   1280x800      59.81  
   1152x864      75.00  
   1280x768      59.87  
   1024x768      60.00  
   640x480       59.94  
   2560x1440_60.00  59.96* 

```
- 2.添加分辨率
``` bash
cvt 2560 1440
```
- 3.接着输入
``` bash
xrandr --newmode "2560x1440_60.00"  312.25  2560 2752 3024 3488  1440 1443 1448 1493 -hsync +vsync
```
- 4.添加该模式，此时就可以在display settings 中看到2560*1440 的分辨率了，选择即可
```
xrandr --addmode Virtual1 "2560x1440_60.00"
```
- 5.以上步骤完成后在Ubuntu重启后，设置的分辨率会消失，如果要使其长期有效，则将以下命令拷贝到/etc/profile 文件中即可
``` bash
cvt 2560 1440
xrandr --newmode "2560x1440_60.00"  312.25  2560 2752 3024 3488  1440 1443 1448 1493 -hsync +vsync
xrandr --addmode Virtual1 "2560x1440_60.00"
```
1920 * 1080 分辨率
``` bash
cvt 1920 1080
xrandr --newmode "1920X1080_60.00" 173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode Virtual1 "1920X1080_60.00"
xrandr --output Virtual1 --mode "1920X1080_60.00"
```
