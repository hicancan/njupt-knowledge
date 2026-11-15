---
title: 《计算机图形学（全英文）》OpenGL 环境配置指南
kind: 实验
course: 计算机图形学全英文
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301312C%E3%80%91%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6%EF%BC%88%E5%85%A8%E8%8B%B1%E6%96%87%EF%BC%89/OpenGL%2001.pdf
---

# 《计算机图形学（全英文）》OpenGL 环境配置指南

原件经识别和整理；“参考解答”是我们补的。

## OpenGL Configuration

### Mac User:

#### Basic Setting

1. Google homebrew -> Open Terminal -> Input `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. `brew install glfw3`
3. `brew install glew`

#### Xcode Setting

1. Open Xcode -> Create OS X Command Line Tool (Language C++)
2. Click Project Layout -> Build Setting -> Search Paths -> Header Search Paths -> add `/usr/local/include`
3. Build Phases -> Link Binary With Libraries -> add `OpenGL.framework`
4. add -> add other -> press Command+Shift+G -> input `/usr/local/Cellar/glew/1.12.0/lib/libGLEW.1.12.0.dylib` *
5. add -> add other -> press Command+Shift+G -> input `/usr/local/Cellar/glfw3/3.1.2/lib/libglfw.3.3.1dylib` *

(the number in step 4 and 5 may be changed)

Now jump to Coding Part at the bottom of this tutorial!

### Windows User:

#### Basic Setting

1. google Visual Studio and download
2. google GLEW -> download Binaries Windows 32-bit and 64-bit
3. google GLFW -> click download on top right corner -> Windows pre-compiled binaries -> 32-bit (recommended)

#### Visual Studio Setting

1. Create New Project -> Visual C++ Win32 Console Application (Empty project)
2. Add New Item -> C++ file (`main.cpp`)
3. Right Click the Project (Not the Solution) -> Property -> C/C++ -> General -> Additional Include Directories -> add (then click … button to browse) your `glew/include` (and) `glfw/include` folder
4. Linker -> General -> Additional Library Directories -> add (then click … button to browse) `glew/lib/release/win32` `glfw/lib-vc2015`
5. Input -> Additional Dependencies -> `opengl32.lib` `glew32s.lib` `glfw3.lib`
6. Copy the `glew32.dll` in your `glew/bin/release/win32` paste to the same folder of `main.cpp` file

#### Optional Setting (Relative Linking)

There is a way for relative link setting which the GLEW and GLFW are in the same folder of the project. This tutorial only mentions the different part.

3. Right Click the Project (Not the Solution) -> Property -> C/C++ -> General -> Additional Include Directories -> add and input `$(SolutionDir)/../External Libraries/GLFW/include` (and) `$(SolutionDir)/../External Libraries/GLEW/include`
4. Linker -> General -> Additional Library Directories -> add (and input) `$(SolutionDir)/../External Libraries/GLEW/lib/release/win32` (and) `$(SolutionDir)/../External Libraries/GLFW/lib-vc2015`

`$(SolutionDir)` refers to the folder which contains the `project.sln` file.

The file and folder structure is shown in the following figure.



Great!!! You should have a window and enjoy yourself!
