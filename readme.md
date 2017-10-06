   **ADVANCE TOPICS IN PYTHON**<br/>
   **Table to content**<br/>
* object oriented programming
* Data structures
* Functional programming 
* Meta Classes
* Exceptions
* Testing 
* Threading
* Simulations
* String bytes
* 1/0 files
* serialization
* Networking
* Web services
* Gui<hr/>

**topic 1**<br/>
<h2>object oriented programming(OOP)</h2><br/>
Objects are physical entities we can feel and touch in real life,but in software development objects are virtual representations of entities that derives it's meaning from a particlar context. <em>object oriented programming</em>(OOP) means that programs models functionalities of an object through interaction with other objects,using their data and behaviour.The way OOP represents objects is an <em>abstraction</em>.
<p><em>Encapsulation</em> is the idea that an attribute donnot need to be visualised by other objects,The attribuute are hidden from all other object except it's respective object for a better and clean code.for instance, imagine we have an object called <span style="font-family: courier">telvision</span> which has the attribute <span style="font-family: courier">capacitor</span> and <span style="font-family: courier">voltage</span>,these attributes only make sense in the <span style="font-family: courier">television</span> because objects like <span style="font-family: courier">remote</span> don't need to interact nor visualise them.
<strong>unit 1.</strong><h3>Classes</h3>
From OOP perspective,classes describes objects,and each object is an instance of a class. ref--><span style="font-family: courier">oop:oop_1.py</span>
  
<strong>unit2.</strong>
<h3>properties</h3>
Encapsulation suggest that attribute are made private,else attribute/method would be accessed by all objects,even in the presence of an interface, for convention add an underscore <span style="font-family: courier">_<span><</span>attribute/method></span> or a double underscore <span style="font-family: courier">__<span><</span>attribute/method></span> to make an attribute private and are both considered a good convention and these method is known as <span style="font-family: courier">name mangling</span>.<br/>
Properties is the python mechanism of implementing encapsulation and the interfce to interact with private attribute.That means anytime we need an attribute,we are forced to use the 
<span style="font-family: courier">set_value()</span> and <span style="font-family: courier">set_value()</span>.This approach generate us some maintainance problem.<br/>
The <span style="font-family: courier">property()</span> allows us to create property recieving as an argument the function use to  set,get and delete an attribute as <span style="font-family: courier">property(<span><</span>set_functon>,<span><</span>get_functon>,<span><</span>delete_functon>)</span>. reference:<span style="font-family: courier">oop_2-(property):property.py</span>

