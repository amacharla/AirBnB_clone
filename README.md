# <img src="https://www.holbertonschool.com/assets/holberton-logo-simplified-71b02868461c07d54553e4a7cc05d1926681a6755cc19030b0458f2d70ae9909.png" width="30"> 0x00. AirBnB clone - The console

**Authors: [Anoop Macharla](https://www.linkedin.com/in/amacharla/) and [Thomas Wang](https://www.linkedin.com/in/thomaspwang/)**

<img src ="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png" width='500'>

## Getting Started

<p>This is the first step towards building our first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because we will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration... </p>

<p>Each tasks are linked and will help you to:
- put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file
- create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>...) that inherit from <code>BaseModel</code>
- create the first abstracted storage engine of the project: File storage. 
- create all unittests to validate all our classes and storage engine</p>

<h2>What&#39;s a command interpreter?</h2>

<p>It&#39;s like a shell command interpreter the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc...</li>
<li>Do operations on objects (count, compute stats, etc...)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

### Prerequisites
<ul>
<li><a href="https://docs.python.org/3.4/library/cmd.html">cmd module</a></li>
<li><a href="https://intranet.hbtn.io/concepts/66">packages</a></li>
<li><a href="https://docs.python.org/3.4/library/uuid.html">uuid module</a></li>
<li><a href="https://docs.python.org/3.4/library/datetime.html">datetime</a></li>
<li><a href="https://docs.python.org/3.4/library/unittest.html#module-unittest">unittest module</a></li>
<li><a href="https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/">args/kwargs</a></li>
<li><a href="https://www.pythonsheets.com/notes/python-tests.html">Python test cheatsheet</a></li>
</ul>

### Execution

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

### Project Breakdown

#### 0. README, AUTHORS

#### 1. Be PEP8 compliant!

#### 2. Unittests

#### 3. BaseModel

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

#### 4. Create BaseModel from dictionary 

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

#### 5. Store first object

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

#### 6. Console 0.0.1

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

#### 7. Console 0.1 

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

#### 8. First User 

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

#### 9. More classes!

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

#### 10. Console 1.0

<p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of all our new classes: <code>Place</code>, <code>State</code>, <code>City</code>, <code>Amenity</code> and <code>Review</code></p>

<p>Update your command interpreter (<code>console.py</code>) to allow those actions: <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> with all classes created previously.</p>

<p>Enjoy your first console!</p>

<p><strong>No unittests needed for the console</strong></p>