**Here's the following instructions:**
```bash
pip install -r requirements.txt
python3 db_create.py
python3 run.py
```

A browser will be opened at http://127.0.0.1:5000

Go to root directory of Ubuntu and run the following commands:
```bash
cd tmp
git clone https://github.com/bast/cmake-example.git
cd cmake-example
mkdir build
cd build
cmake ..
make
ctest
```
Open http://127.0.0.1:5000 in your browser.
Click on "Projects".
Click on "New Project.
Enter any name as project name.
Enter /tmp/cmake-example/build as working directory.
Click on "Create project".

We will see a project overview page for that project. 
Click on "Add file".
In the "Add file to project" dialog, enter the filename /tmp/cmake-example/src/example.cpp.
Click "Add file".

Next to "example.cpp", click on "generate patches".
Right now, none of the check boxes are actually implemented, so you can ignore all of them - all mutations will be used by default.
Click on "Generate patches".

In the top navigation, click on "Queue". We see the 14 patches from before.
Click on "Resume" to start the execution.
When you reload the page, you see that after a few seconds, the queue is empty.

Go back to project overview of that particular project from 'Projects'.

We see a graph that describes the breakdown of the patches. click on any node to explore more
