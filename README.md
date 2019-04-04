# python脚本批量生成上传AppStore所需要的多个logo文件

### 使用方法

appLogo.py ---脚本文件 、Contents.json ---配置文件（AppIcon-1.appiconset文件夹下复制过来）、logo1024.png --原图标文件。
三个文件放在统一文件夹中，运行appLogo.py。结果存储在logos文件夹下面。



###依赖图片处理库 Pillow

osx mavericks 10.9  安装方式：  

			xcode-select --install
 			sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install Pillow


http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa  
http://stackoverflow.com/questions/19532125/cant-install-pil-after-mac-os-x-10-9