# CV_Challenge-3
At construction site, count the number of trucks filled by the excavator and swing analysis of the excavator.

# Algorithm:
  To achieve the swing analysis used Template Matching alogrithm from OpenCV. Here, The template used will be look like the below image.
  
![alt text](https://github.com/SaiKrishnaTheGreat/CV_Challenge-3/blob/master/templates/template_4.png)
  
  Once the template match results will be more than 70% or threshold>0.7, then swing_count will be increased by 1 and flag will be enabled. Once No Match occurs(threshold < 0.7), then flag will be disabled for swing_count increment.
  
# Result Video:
[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://www.youtube.com/watch?v=wk75WIrtwfQ&feature=youtu.be)

  
# Requirements:
  1. Ubuntu 16.04 (Application tested)
  2. OpenCV (Install it from source)
  
 
