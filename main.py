from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))) #里面的参数是得到当前目录文件的父目录的路径  整个方法是把路径添加到系统path里

# print(os.path.dirname(os.path.abspath(__file__)))测试路径

execute(["scrapy","crawl","jobbole"]) #运行 scrapy crawl jobble 这个命令