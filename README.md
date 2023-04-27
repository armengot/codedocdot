# Code, doc & dot

In this simple [script](doc2dot.py) you will find a powerfull tool to visualize the code files relationship of an entire large project in a nutshell.

The output of the recursive search through the files can be parsed by [Graphviz](https://graphviz.org/) command line  ```dot``` tool to obtain a PNG or PS image.

## Usage

If ```project``` is the name of the root folder of your project. You could do:
```
python3 doc2dot.py project h cpp 2> project.dot
```

Where first parameter ("project") specifies the root folder to start the search and after that, a list of target extensions of source code can be added.
Standard output is reserved to verbose activity, so the standard error output is used here to get the final ```.dot``` file.

After that, calling ```dot``` from Graphviz can parse the previous output.
```
dot project.dot -Tpng > project.png
```

## Idea 💡

In most of programming languages the libraries we write are called from other files. The doc2dot.py script uses that string appearances to build the list of edges of a tree. The drawing work can be done by Graphviz ```dot```.

![example](example.png)
