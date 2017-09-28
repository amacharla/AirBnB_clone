# <img src="https://www.holbertonschool.com/assets/holberton-logo-simplified-71b02868461c07d54553e4a7cc05d1926681a6755cc19030b0458f2d70ae9909.png" width="30"> 0x00. AirBnB clone - The console

**Authors: [Anoop Macharla](https://www.linkedin.com/in/amacharla/) and [Thomas Wang](https://www.linkedin.com/in/thomaspwang/)

<img src ="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png">

<h2>Welcome to the AirBnB clone project! (The Holberton B&amp;B)</h2>

<p>Before starting, please read the <a href="https://intranet.hbtn.io/concepts/74">AirBnB concept page</a></p>

<p>First step: Write a command interpreter to manage your AirBnB objects.</p>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration... </p>

<p>Each tasks are linked and will help you to:
- put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file
- create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>...) that inherit from <code>BaseModel</code>
- create the first abstracted storage engine of the project: File storage. 
- create all unittests to validate all our classes and storage engine</p>

<h2>What&#39;s a command interpreter?</h2>

<p>Do you remember the Shell? It&#39;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc...</li>
<li>Do operations on objects (count, compute stats, etc...)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

## Table of Contents

* [Resources](#resources)
* [What students should learn from this project](#what-students-should-learn-from-this-project)
* [Requirements](#requirements)
* [Execution](#execution)
* [Project Breakdown](#project-breakdown)

## Resources

<p>Read:</p>

<ul>
<li><a href="https://docs.python.org/3.4/library/cmd.html">cmd module</a></li>
<li><a href="https://intranet.hbtn.io/concepts/66">packages</a></li>
<li><a href="https://docs.python.org/3.4/library/uuid.html">uuid module</a></li>
<li><a href="https://docs.python.org/3.4/library/datetime.html">datetime</a></li>
<li><a href="https://docs.python.org/3.4/library/unittest.html#module-unittest">unittest module</a></li>
<li><a href="https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/">args/kwargs</a></li>
<li><a href="https://www.pythonsheets.com/notes/python-tests.html">Python test cheatsheet</a></li>
</ul>

## What students should learn from this project

<p>At the end of this project you are expected to be able to explain to anyone, without the help of Google:</p>

<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the <code>cmd</code> module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage <code>datetime</code></li>
<li>What is an <code>UUID</code></li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

## Requirements

<h3>Requirements for Python scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
</ul>

<h3>Requirements for Python unit tests</h3>

<p>For this project, you will create <strong>unit tests</strong>, not doctest:</p>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project: ex: for <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don&#39;t miss any edge case</li>
</ul>

## Execution

<p>Your shell should work like this in interactive mode:</p>

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>

<p>But also in non-interactive mode:</p>

<pre><code>$ echo &quot;help&quot; | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step0.png" alt="step0"></p>

## Project Breakdown