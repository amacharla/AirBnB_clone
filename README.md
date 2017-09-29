# <img src="https://www.holbertonschool.com/assets/holberton-logo-simplified-71b02868461c07d54553e4a7cc05d1926681a6755cc19030b0458f2d70ae9909.png" width="30"> 0x00. AirBnB clone - The console

**Authors: [Anoop Macharla](https://www.linkedin.com/in/amacharla/) and [Thomas Wang](https://www.linkedin.com/in/thomaspwang/)**

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

### 0. README, AUTHORS
<li>Write a <code>README.md</code>:

<ul>
<li>description of the project</li>
<li>description of the command interpreter:

<ul>
<li>how to start it</li>
<li>how to use it</li>
<li>examples</li>
</ul></li>
</ul></li>
<li>You should have an <code>AUTHORS</code> file at the root of your repository, listing all individuals having contributed content to the repository. Format, see <a href="https://github.com/docker/docker/blob/master/AUTHORS">Docker</a></li>
</ul>

### 1. Be PEP8 compliant! 
Write a beautiful code that passes the PEP8 checks

### 2. Unittests 
  <p>All your files, classes, functions must be tested with unit tests</p>

<p>Tips for testing the console: <a href="http://stackoverflow.com/questions/30056986/create-automated-tests-for-interactive-shell-based-on-pythons-cmd-module">Mock test to redirect stdin/stdout</a></p>

<pre><code>guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
</code></pre>

<p><em>Note that this is just an example, the number of tests you create can be different from the above example</em>.</p>

### 3. BaseModel
<p>Write a class <code>BaseModel</code> that defines all common attributes/methods for other classes:</p>

<ul>
<li><code>models/base_model.py</code></li>
<li>Public instance attributes: 

<ul>
<li><code>id</code>: string - assign with an <code>uuid</code> when an instance is created:

<ul>
<li>you can use <code>uuid.uuid4()</code> to generate unique <code>id</code> but don&#39;t forget to convert to a string</li>
<li>the goal is to have unique <code>id</code> for each <code>BaseModel</code></li>
</ul></li>
<li><code>created_at</code>: datetime - assign with the current datetime when an instance is created</li>
<li><code>updated_at</code>: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object</li>
</ul></li>
<li><code>__str__</code>: should print: <code>[&lt;class name&gt;] (&lt;self.id&gt;) &lt;self.__dict__&gt;</code></li>
<li>Public instance methods:

<ul>
<li><code>save(self)</code>: updates the public instance attribute <code>updated_at</code> with the current datetime</li>
<li><code>to_dict(self)</code>: returns a dictionary containing all keys/values of <code>__dict__</code> of the instance:

<ul>
<li>a key <code>__class__</code> must be added to this dictionary with the class name of the object</li>
<li><code>created_at</code> and <code>updated_at</code> must be converted to string object in ISO format:

<ul>
<li>format: <code>%Y-%m-%dT%H:%M:%S.%f</code> (ex: <code>2017-06-14T22:31:03.285259</code>) </li>
<li>you can use <code>isoformat()</code> of <code>datetime</code> object</li>
</ul></li>
<li>This method will be the first piece of the serialization/deserialization process: create a dictionary representation with &quot;simple object type&quot; of our <code>BaseModel</code></li>
</ul></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = &quot;Holberton&quot;
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print(&quot;JSON of my_model:&quot;)
for key in my_model_json.keys():
    print(&quot;\t{}: ({}) - {}&quot;.format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {&#39;my_number&#39;: 89, &#39;name&#39;: &#39;Holberton&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), &#39;id&#39;: &#39;b6a6e15c-c67d-4312-9a75-9d084935e579&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {&#39;my_number&#39;: 89, &#39;name&#39;: &#39;Holberton&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), &#39;id&#39;: &#39;b6a6e15c-c67d-4312-9a75-9d084935e579&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{&#39;my_number&#39;: 89, &#39;name&#39;: &#39;Holberton&#39;, &#39;__class__&#39;: &#39;BaseModel&#39;, &#39;updated_at&#39;: &#39;2017-09-28 21:05:54.119572&#39;, &#39;id&#39;: &#39;b6a6e15c-c67d-4312-9a75-9d084935e579&#39;, &#39;created_at&#39;: &#39;2017-09-28 21:05:54.119427&#39;}
JSON of my_model:
    my_number: (&lt;class &#39;int&#39;&gt;) - 89
    name: (&lt;class &#39;str&#39;&gt;) - Holberton
    __class__: (&lt;class &#39;str&#39;&gt;) - BaseModel
    updated_at: (&lt;class &#39;str&#39;&gt;) - 2017-09-28 21:05:54.119572
    id: (&lt;class &#39;str&#39;&gt;) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (&lt;class &#39;str&#39;&gt;) - 2017-09-28 21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
</code></pre>

### 4. Create BaseModel from dictionary 
<p>Previously we create a method to generate a dictionary representation of an instance (method <code>to_dict()</code>).</p>

<p>Now it&#39;s time to re-create an instance with this dictionary representation.</p>

<pre><code>&lt;class &#39;BaseModel&#39;&gt; -&gt; to_dict() -&gt; &lt;class &#39;dict&#39;&gt; -&gt; &lt;class &#39;BaseModel&#39;&gt;
</code></pre>

<p>Update <code>models/base_model.py</code>:</p>

<ul>
<li><code>__init__(self, *args, **kwargs)</code>: 

<ul>
<li>you will use <code>*args, **kwargs</code> arguments for the constructor of a <code>BaseModel</code>. <a href="https://intranet.hbtn.io/concepts/74">More detail</a></li>
<li><code>*args</code> won&#39;t be used</li>
<li>if <code>kwargs</code> is not empty:

<ul>
<li>each key of this dictionary is an attribute name</li>
<li>each value of this dictionary is the value of this attribute name</li>
<li><strong>Warning</strong>: <code>created_at</code> and <code>updated_at</code> are strings in this dictionary, but inside your <code>BaseModel</code> instance is working with <code>datetime</code> object. You have to convert these strings into <code>datetime</code> object. Tip: you know the string format of these datetime</li>
</ul></li>
<li>otherwise:

<ul>
<li>create <code>id</code> and <code>created_at</code> as you did previously (new instance)</li>
</ul></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = &quot;Holberton&quot;
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print(&quot;--&quot;)
my_model_json = my_model.to_dict()
print(my_model_json)
print(&quot;JSON of my_model:&quot;)
for key in my_model_json.keys():
    print(&quot;\t{}: ({}) - {}&quot;.format(key, type(my_model_json[key]), my_model_json[key]))

print(&quot;--&quot;)
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print(&quot;--&quot;)
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {&#39;id&#39;: &#39;56d43177-cc5f-4d6c-a0c1-e167f8c27337&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), &#39;my_number&#39;: 89, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), &#39;name&#39;: &#39;Holberton&#39;}
&lt;class &#39;datetime.datetime&#39;&gt;
--
{&#39;id&#39;: &#39;56d43177-cc5f-4d6c-a0c1-e167f8c27337&#39;, &#39;created_at&#39;: &#39;2017-09-28 21:03:54.052298&#39;, &#39;__class__&#39;: &#39;BaseModel&#39;, &#39;my_number&#39;: 89, &#39;updated_at&#39;: &#39;2017-09-28 21:03:54.052302&#39;, &#39;name&#39;: &#39;Holberton&#39;}
JSON of my_model:
    id: (&lt;class &#39;str&#39;&gt;) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (&lt;class &#39;str&#39;&gt;) - 2017-09-28 21:03:54.052298
    __class__: (&lt;class &#39;str&#39;&gt;) - BaseModel
    my_number: (&lt;class &#39;int&#39;&gt;) - 89
    updated_at: (&lt;class &#39;str&#39;&gt;) - 2017-09-28 21:03:54.052302
    name: (&lt;class &#39;str&#39;&gt;) - Holberton
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {&#39;id&#39;: &#39;56d43177-cc5f-4d6c-a0c1-e167f8c27337&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), &#39;my_number&#39;: 89, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), &#39;name&#39;: &#39;Holberton&#39;}
&lt;class &#39;datetime.datetime&#39;&gt;
--
False
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

### 5. Store first object
<p>Now we can recreate a <code>BaseModel</code> from another one by using a dictionary representation:</p>

<pre><code>&lt;class &#39;BaseModel&#39;&gt; -&gt; to_dict() -&gt; &lt;class &#39;dict&#39;&gt; -&gt; &lt;class &#39;BaseModel&#39;&gt;
</code></pre>

<p>It&#39;s great but it&#39;s still not persistent: every time you launch the program, you don&#39;t restore all objects created before... The first way you will see here is to save these objects to a file.</p>

<p>Writing the dictionary representation to a file won&#39;t be relevant:</p>

<ul>
<li>Python doesn&#39;t know how to convert a string to a dictionary (easily)</li>
<li>It&#39;s not human readable</li>
<li>Using this file with another program in Python or other language will be hard.</li>
</ul>

<p>So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, human can read and all programming languages have JSON reader and writer.</p>

<p>Now the flow of serialization-deserialization will be:</p>

<pre><code>&lt;class &#39;BaseModel&#39;&gt; -&gt; to_dict() -&gt; &lt;class &#39;dict&#39;&gt; -&gt; JSON dump -&gt; &lt;class &#39;str&#39;&gt; -&gt; FILE -&gt; &lt;class &#39;str&#39;&gt; -&gt; JSON load -&gt; &lt;class &#39;dict&#39;&gt; -&gt; &lt;class &#39;BaseModel&#39;&gt;
</code></pre>

<p>Magic right?</p>

<p>Terms:</p>

<ul>
<li><strong>simple Python data structure</strong>: Dictionaries, arrays, number and string. ex: <code>{ &#39;12&#39;: { &#39;numbers&#39;: [1, 2, 3], &#39;name&#39;: &quot;John&quot; } }</code></li>
<li><strong>JSON string representation</strong>: String representing a simple data structure in JSON format. ex: <code>&#39;{ &quot;12&quot;: { &quot;numbers&quot;: [1, 2, 3], &quot;name&quot;: &quot;John&quot; } }&#39;</code></li>
</ul>

<p>Write a class <code>FileStorage</code> that serializes instances to a JSON file and deserializes JSON file to instances:</p>

<ul>
<li><code>models/engine/file_storage.py</code></li>
<li>Private class attributes:

<ul>
<li><code>__file_path</code>: string - path to the JSON file (ex: <code>file.json</code>)</li>
<li><code>__objects</code>: dictionary - empty but will store all objects by <code>&lt;class name&gt;.id</code> (ex: to store a <code>BaseModel</code> object with <code>id=12121212</code>, the key will be <code>BaseModel.12121212</code>)</li>
</ul></li>
<li>Public instance methods:

<ul>
<li><code>all(self)</code>: returns the dictionary <code>__objects</code></li>
<li><code>new(self, obj)</code>: sets in <code>__objects</code> the <code>obj</code> with key <code>&lt;obj class name&gt;.id</code></li>
<li><code>save(self)</code>: serializes <code>__objects</code> to the JSON file (path: <code>__file_path</code>)</li>
<li><code>reload(self)</code>: deserializes the JSON file to <code>__objects</code> (only if the JSON file exists ; otherwise, do nothing)</li>
</ul></li>
</ul>

<p>Update <code>models/__init__.py</code>: to create a unique <code>FileStorage</code> instance for your application</p>

<ul>
<li>import <code>file_storage.py</code></li>
<li>create the variable <code>storage</code>, an instance of <code>FileStorage</code></li>
<li>call <code>reload()</code> method on this variable</li>
</ul>

<p>Update <code>models/base_model.py</code>: to link your <code>BaseModel</code> to <code>FileStorage</code> by using the variable <code>storage</code></p>

<ul>
<li>import the variable <code>storage</code></li>
<li>in the method <code>save(self)</code>:

<ul>
<li>call <code>save(self)</code> method of <code>storage</code></li>
</ul></li>
<li><code>__init__(self, *args, **kwargs)</code>: 

<ul>
<li>if it&#39;s a new instance (not from a dictionary representation), add a call to the method <code>new(self)</code> on <code>storage</code></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print(&quot;-- Reloaded objects --&quot;)
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print(&quot;-- Create a new object --&quot;)
my_model = BaseModel()
my_model.name = &quot;Holberton&quot;
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {&#39;my_number&#39;: 89, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), &#39;name&#39;: &#39;Holberton&#39;, &#39;id&#39;: &#39;ee49c413-023a-4b49-bd28-f2936c95460d&#39;}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d&quot;: {&quot;my_number&quot;: 89, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:07:25.047381&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:07:25.047372&quot;, &quot;name&quot;: &quot;Holberton&quot;, &quot;id&quot;: &quot;ee49c413-023a-4b49-bd28-f2936c95460d&quot;}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {&#39;name&#39;: &#39;Holberton&#39;, &#39;id&#39;: &#39;ee49c413-023a-4b49-bd28-f2936c95460d&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), &#39;my_number&#39;: 89, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {&#39;name&#39;: &#39;Holberton&#39;, &#39;id&#39;: &#39;080cce84-c574-4230-b82a-9acb74ad5e8c&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), &#39;my_number&#39;: 89, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {&#39;id&#39;: &#39;080cce84-c574-4230-b82a-9acb74ad5e8c&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), &#39;name&#39;: &#39;Holberton&#39;, &#39;my_number&#39;: 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {&#39;id&#39;: &#39;ee49c413-023a-4b49-bd28-f2936c95460d&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), &#39;name&#39;: &#39;Holberton&#39;, &#39;my_number&#39;: 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {&#39;id&#39;: &#39;e79e744a-55d4-45a3-b74a-ca5fae74e0e2&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), &#39;name&#39;: &#39;Holberton&#39;, &#39;my_number&#39;: 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;e79e744a-55d4-45a3-b74a-ca5fae74e0e2&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:08:06.151750&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:08:06.151711&quot;, &quot;name&quot;: &quot;Holberton&quot;, &quot;my_number&quot;: 89}, &quot;BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;080cce84-c574-4230-b82a-9acb74ad5e8c&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:07:51.973308&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:07:51.973301&quot;, &quot;name&quot;: &quot;Holberton&quot;, &quot;my_number&quot;: 89}, &quot;BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;ee49c413-023a-4b49-bd28-f2936c95460d&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:07:25.047381&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:07:25.047372&quot;, &quot;name&quot;: &quot;Holberton&quot;, &quot;my_number&quot;: 89}}
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

### 6. Console 0.0.1
<p>Write a program called <code>console.py</code> that contains the entry point of the command interpreter:</p>

<ul>
<li>You must use the module <code>cmd</code></li>
<li>Your class definition must be: <code>class HBNBCommand(cmd.Cmd):</code></li>
<li>Your command interpreter should implement:

<ul>
<li><code>quit</code> and <code>EOF</code> to exit the program</li>
<li><code>help</code> (this action is provided by default by <code>cmd</code> but you should keep it updated and documented)</li>
<li>a custom prompt: <code>(hbnb)</code></li>
<li>an empty line + <code>ENTER</code> shouldn&#39;t execute anything</li>
</ul></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

<p><strong>No unittests needed</strong></p>

### 7. Console 0.1 
<p>Update your command interpreter (<code>console.py</code>) to have these commands:</p>

<ul>
<li><code>create</code>: Creates a new instance of <code>BaseModel</code>, saves it (to the JSON file) and prints the <code>id</code>. Ex: <code>$ create BaseModel</code> 

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ create</code>)</li>
<li>If the class name doesn&#39;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ create MyModel</code>)</li>
</ul></li>
<li><code>show</code>: Prints the string representation of an instance based on the class name and <code>id</code>. Ex: <code>$ show BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ show</code>)</li>
<li>If the class name doesn&#39;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ show MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ show BaseModel</code>)</li>
<li>If the instance of the class name doesn&#39;t exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ show BaseModel 121212</code>)</li>
</ul></li>
<li><code>destroy</code>: Deletes an instance based on the class name and <code>id</code> (save the change into the JSON file). Ex: <code>$ destroy BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ destroy</code>)</li>
<li>If the class name doesn&#39;t exist, print <code>** class doesn&#39;t exist ** (ex:</code>$ destroy MyModel<code>)</code></li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ destroy BaseModel</code>)</li>
<li>If the instance of the class name doesn&#39;t exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ destroy BaseModel 121212</code>)</li>
</ul></li>
<li><code>all</code>: Prints all string representation of all instances based or not on the class name. Ex: <code>$ all BaseModel</code> or <code>$ all</code>.

<ul>
<li>If the class name doesn&#39;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ all MyModel</code>)</li>
</ul></li>
<li><code>update</code>: Updates an instance based on the class name and <code>id</code> by adding or updating attribute (save the change into the JSON file). Ex: <code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@holbertonschool.com&quot;</code>.

<ul>
<li>Usage: <code>update &lt;class name&gt; &lt;id&gt; &lt;attribute name&gt; &quot;&lt;attribute value&gt;&quot;</code></li>
<li>Only one attribute can be updated at the time</li>
<li>The attribute value must be casted to the attribute type </li>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ update</code>)</li>
<li>If the class name doesn&#39;t exist, print <code>** class doesn&#39;t exist **</code> (ex: <code>$ update MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ update BaseModel</code>)</li>
<li>If the instance of the class name doesn&#39;t exist for the <code>id</code>, print <code>** no instance found **</code>  (ex: <code>$ update BaseModel 121212</code>)</li>
<li>If the attribute name is missing, print <code>** attribute name missing **</code> (ex: <code>$ update BaseModel existing-id</code>)</li>
<li>If the value for the attribute name doesn&#39;t exist, print <code>** value missing **</code> (ex: <code>$ update BaseModel existing-id first_name</code>)</li>
<li>All other arguments should not be used (Ex: <code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@holbertonschool.com&quot; first_name &quot;Betty&quot;</code> = <code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@holbertonschool.com&quot;</code>)</li>
</ul></li>
</ul>

<p>Let&#39;s add some rules:</p>

<ul>
<li>You can assume arguments are always in the right order</li>
<li>Each arguments are separated by a space</li>
<li>A string argument with a space must be between double quote</li>
<li>The error management starts from the first argument to the last one<br></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn&#39;t exist **
(hbnb) all BaseModel
[]
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
ad0fc007-cd06-47d2-83ed-e388e658a02c
(hbnb) show BaseModel ad0fc007-cd06-47d2-83ed-e388e658a02c
[BaseModel] (ad0fc007-cd06-47d2-83ed-e388e658a02c) {&#39;id&#39;: &#39;ad0fc007-cd06-47d2-83ed-e388e658a02c&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 9, 2, 745270), &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 9, 2, 745258)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel ad0fc007-cd06-47d2-83ed-e388e658a02c first_name &quot;Betty&quot;
(hbnb) show BaseModel ad0fc007-cd06-47d2-83ed-e388e658a02c
[BaseModel] (ad0fc007-cd06-47d2-83ed-e388e658a02c) {&#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 9, 31, 854263), &#39;first_name&#39;: &#39;Betty&#39;, &#39;id&#39;: &#39;ad0fc007-cd06-47d2-83ed-e388e658a02c&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 9, 2, 745258)}
(hbnb) destroy BaseModel ad0fc007-cd06-47d2-83ed-e388e658a02c
(hbnb) show BaseModel ad0fc007-cd06-47d2-83ed-e388e658a02c
** no instance found **
(hbnb) 
</code></pre>

<p><strong>No unittests needed</strong></p>

### 8. First User 
<p>Write a class <code>User</code> that inherits from <code>BaseModel</code>:</p>

<ul>
<li><code>models/user.py</code></li>
<li>Public class attributes:

<ul>
<li><code>email</code>: string - empty string</li>
<li><code>password</code>: string - empty string</li>
<li><code>first_name</code>: string - empty string</li>
<li><code>last_name</code>: string - empty string</li>
</ul></li>
</ul>

<p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of <code>User</code>.</p>

<p>Update your command interpreter (<code>console.py</code>) to allow <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> used with <code>User</code>.</p>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print(&quot;-- Reloaded objects --&quot;)
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print(&quot;-- Create a new User --&quot;)
my_user = User()
my_user.first_name = &quot;Betty&quot;
my_user.last_name = &quot;Holberton&quot;
my_user.email = &quot;airbnb@holbertonshool.com&quot;
my_user.password = &quot;root&quot;
my_user.save()
print(my_user)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:14.333862&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:14.333852&quot;}, &quot;BaseModel.a42ee380-c959-450e-ad29-c840a898cfce&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;a42ee380-c959-450e-ad29-c840a898cfce&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:15.504296&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:15.504287&quot;}, &quot;BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:12.971544&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:12.971521&quot;}, &quot;BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:13.753347&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:13.753337&quot;}, &quot;BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;9bf17966-b092-4996-bd33-26a5353cccb4&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:14.963058&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:14.963049&quot;}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {&#39;id&#39;: &#39;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {&#39;id&#39;: &#39;9bf17966-b092-4996-bd33-26a5353cccb4&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {&#39;id&#39;: &#39;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {&#39;id&#39;: &#39;a42ee380-c959-450e-ad29-c840a898cfce&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {&#39;id&#39;: &#39;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&#39;id&#39;: &#39;38f22813-2753-4d42-b37c-57a17f1e4f88&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &#39;email&#39;: &#39;airbnb@holbertonshool.com&#39;, &#39;first_name&#39;: &#39;Betty&#39;, &#39;last_name&#39;: &#39;Holberton&#39;, &#39;password&#39;: &#39;root&#39;}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;: {&quot;id&quot;: &quot;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:12.971544&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:12.971521&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;: {&quot;id&quot;: &quot;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:13.753347&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:13.753337&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4&quot;: {&quot;id&quot;: &quot;9bf17966-b092-4996-bd33-26a5353cccb4&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:14.963058&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:14.963049&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;: {&quot;id&quot;: &quot;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:14.333862&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:14.333852&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.a42ee380-c959-450e-ad29-c840a898cfce&quot;: {&quot;id&quot;: &quot;a42ee380-c959-450e-ad29-c840a898cfce&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:15.504296&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:15.504287&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;User.38f22813-2753-4d42-b37c-57a17f1e4f88&quot;: {&quot;id&quot;: &quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:42.848279&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:42.848291&quot;, &quot;email&quot;: &quot;airbnb@holbertonshool.com&quot;, &quot;first_name&quot;: &quot;Betty&quot;, &quot;__class__&quot;: &quot;User&quot;, &quot;last_name&quot;: &quot;Holberton&quot;, &quot;password&quot;: &quot;root&quot;}}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {&#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), &#39;id&#39;: &#39;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {&#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), &#39;id&#39;: &#39;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {&#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), &#39;id&#39;: &#39;9bf17966-b092-4996-bd33-26a5353cccb4&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {&#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), &#39;id&#39;: &#39;a42ee380-c959-450e-ad29-c840a898cfce&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {&#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), &#39;id&#39;: &#39;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&#39;password&#39;: &#39;63a9f0ea7bb98050796b649e85481845&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &#39;email&#39;: &#39;airbnb@holbertonshool.com&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &#39;last_name&#39;: &#39;Holberton&#39;, &#39;id&#39;: &#39;38f22813-2753-4d42-b37c-57a17f1e4f88&#39;, &#39;first_name&#39;: &#39;Betty&#39;}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {&#39;password&#39;: &#39;root&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), &#39;email&#39;: &#39;airbnb@holbertonshool.com&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), &#39;last_name&#39;: &#39;Holberton&#39;, &#39;id&#39;: &#39;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&#39;, &#39;first_name&#39;: &#39;Betty&#39;}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;: {&quot;updated_at&quot;: &quot;2017-09-28 21:11:12.971544&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:12.971521&quot;}, &quot;User.38f22813-2753-4d42-b37c-57a17f1e4f88&quot;: {&quot;password&quot;: &quot;63a9f0ea7bb98050796b649e85481845&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:42.848279&quot;, &quot;email&quot;: &quot;airbnb@holbertonshool.com&quot;, &quot;id&quot;: &quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;last_name&quot;: &quot;Holberton&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:11:42.848291&quot;, &quot;first_name&quot;: &quot;Betty&quot;, &quot;__class__&quot;: &quot;User&quot;}, &quot;BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4&quot;: {&quot;updated_at&quot;: &quot;2017-09-28 21:11:14.963058&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;9bf17966-b092-4996-bd33-26a5353cccb4&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:14.963049&quot;}, &quot;BaseModel.a42ee380-c959-450e-ad29-c840a898cfce&quot;: {&quot;updated_at&quot;: &quot;2017-09-28 21:11:15.504296&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;a42ee380-c959-450e-ad29-c840a898cfce&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:15.504287&quot;}, &quot;BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;: {&quot;updated_at&quot;: &quot;2017-09-28 21:11:13.753347&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:13.753337&quot;}, &quot;BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;: {&quot;updated_at&quot;: &quot;2017-09-28 21:11:14.333862&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:11:14.333852&quot;}, &quot;User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;: {&quot;password&quot;: &quot;root&quot;, &quot;created_at&quot;: &quot;2017-09-28 21:12:19.611352&quot;, &quot;email&quot;: &quot;airbnb@holbertonshool.com&quot;, &quot;id&quot;: &quot;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;, &quot;last_name&quot;: &quot;Holberton&quot;, &quot;updated_at&quot;: &quot;2017-09-28 21:12:19.611363&quot;, &quot;first_name&quot;: &quot;Betty&quot;, &quot;__class__&quot;: &quot;User&quot;}}
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

<p><strong>No unittests needed for the console</strong></p>

### 9. More classes!
<p>Write all those classes that inherit from <code>BaseModel</code>:</p>

<ul>
<li><code>State</code> (<code>models/state.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>City</code> (<code>models/city.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>state_id</code>: string - empty string: it will be the <code>State.id</code></li>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Amenity</code> (<code>models/amenity.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Place</code> (<code>models/place.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>city_id</code>: string - empty string: it will be the <code>City.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>name</code>: string - empty string</li>
<li><code>description</code>: string - empty string</li>
<li><code>number_rooms</code>: integer - 0</li>
<li><code>number_bathrooms</code>: integer - 0</li>
<li><code>max_guest</code>: integer - 0</li>
<li><code>price_by_night</code>: integer - 0</li>
<li><code>latitude</code>: float - 0.0</li>
<li><code>longitude</code>: float - 0.0</li>
<li><code>amenity_ids</code>: list of string - empty list: it will be the list of <code>Amenity.id</code> later</li>
</ul></li>
</ul></li>
<li><code>Review</code> (<code>models/review.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>place_id</code>: string - empty string: it will be the <code>Place.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>text</code>: string - empty string</li>
</ul></li>
</ul></li>
</ul>

### 10. Console 1.0
<p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of all our new classes: <code>Place</code>, <code>State</code>, <code>City</code>, <code>Amenity</code> and <code>Review</code></p>

<p>Update your command interpreter (<code>console.py</code>) to allow those actions: <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> with all classes created previously.</p>

<p>Enjoy your first console!</p>

<p><strong>No unittests needed for the console</strong></p>