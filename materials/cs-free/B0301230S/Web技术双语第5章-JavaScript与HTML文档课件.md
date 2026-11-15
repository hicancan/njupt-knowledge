---
title: 《Web技术（双语）》第5章 JavaScript与HTML文档（课件）
kind: 课件
course: Web技术（双语）
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/PPT_hjy%E5%BD%95%E9%9F%B3%E7%89%88/part5-javascripthtml-voice.pptx
---

# 《Web技术（双语）》第5章 JavaScript与HTML文档（课件）

原件的每一页，下面附识别出的文字。

### Part 5

![第 1 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第1页.webp)

原文：

Part 5

JavaScript and HTML Documents

PEARSON Addison Wesley

Programming the World Wide Web

### Contents

![第 2 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第2页.webp)

原文：

Contents

• 5.1 JavaScript execution environment

• 5.2 Document object model

• 5.3 Element access in JavaScript

• 5.4 Events and events handling

• 5.5 Handing events from body elements

• 5.6 Handing events from button elements

• 5.7 Handing events from text box and password elements

• 5.9 Navigator object

Programming the World Wide Web

5-2

### • JavaScript is executing in a browser.

![第 3 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第3页.webp)

原文：

5.1 JavaScript Execution Environment(review)

• JavaScript is executing in a browser.

• The Window object represents the window on the screen where the HTML document is displayed.

• It is referred to by window property.

• The Document object represents the HTML document being displayed.

• It is denoted by the document property of Window.

Programming the World Wide Web

### Contents

![第 4 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第4页.webp)

原文：

Contents

• 5.1 JavaScript execution environment

• 5.2 Document Object Model

• 5.3 Element access in JavaScript

• 5.4 Events and events handling

• 5.5 Handing events from body elements

• 5.6 Handing events from button elements

• 5.7 Handing events from text box and password elements

• 5.9 Navigator object

Programming the World Wide Web

### 5.2 Document Object Model

![第 5 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第5页.webp)

原文：

5.2 Document Object Model

The DOM is an Application Programming Interface (API) that defines an interface between HTML documents and application programs.

• DOM describe an abstract model of how JavaScript interact with HTML documents on different browsers.

• Different languages will bind the interfaces to specific implementations.

Programming the World Wide Web

### 5.2 Document Object Model

![第 6 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第6页.webp)

原文：

5.2 Document Object Model

With the DOM, users can write code in programming languages to create documents, move around in their structures, and change, add, or delete elements and their content.

• Document in the DOM has a treelike structure.

Programming the World Wide Web

### 5.2 Document Object Model

![第 7 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第7页.webp)

原文：

5.2 Document Object Model

• The HTML document on page 196 is shown as a conceptual tree.

Programming the World Wide Web

### Programming the World Wide Web

![第 8 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第8页.webp)

原文：

Programming the World Wide Web

### 5.2 Document Object Model

![第 9 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第9页.webp)

原文：

5.2 Document Object Model

• Elements of a document correspond to JavaScript objects.

• The JavaScript object has properties and methods.

• Attributes of elements become named properties of objects.

• <input type=“text” name=“address”>

The JavaScript object representing this node will have two properties

• type property will have value “text”

• name property will have value “address”

Programming the World Wide Web

5-9

### Contents

![第 10 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第10页.webp)

原文：

Contents

• 5.1 JavaScript Execution Environment

• 5.2 Document Object Model

• 5.3 Element access in JavaScript

• 5.4 Events and events handling

• 5.5 Handing events from body elements

• 5.6 Handing events from button elements

• 5.7 Handing events from text box and password elements

• 5.9 Navigator object

Programming the World Wide Web

5-10

### 5.3 Element Access in JavaScript

![第 11 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第11页.webp)

原文：

5.3 Element Access in JavaScript

• Elements in HTML document correspond to objects in embedded JavaScript script.

• Objects can be addressed in four ways:

• forms and elements array of the Document object

• Individual elements are specified by index

• Using the name attributes for the form and its elements • name attribute is required

• Using getElementById with id attributes

• id attribute value must be unique for an element

• Implicit arrays

Programming the World Wide Web

5-11

### 5.3 Using forms array

![第 12 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第12页.webp)

原文：

5.3 Using forms array

The original way is to use the forms and elements arrays of the Document object, which is referenced through the document property of the Window object.

• Window is referenced by window.

Programming the World Wide Web

5-12

### 5.3 Using forms array

![第 13 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第13页.webp)

原文：

5.3 Using forms array

• Consider this form:

$$
\begin{array}{l} \text { <  form   action = "" > } \\ \text { <  input   type = "button"   name = "pushMe"> } \\ \text { < /form> } \end{array}
$$

The input element can be referenced as document.forms[0].elements[0]

The drawback is that the addressing can be changed due to the addition or deletion of elements.

Programming the World Wide Web

5-13

### 5.3 Using name Attributes

![第 14 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第14页.webp)

原文：

5.3 Using name Attributes

• All elements from the referenced element up to, but not including, the body must have a name attribute

Referencing the input document.myForm.pushMe

Programming the World Wide Web

5-14

### 5.3 Using id Attribute

![第 15 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第15页.webp)

原文：

5.3 Using id Attribute

• Set the id attribute of the input element <form action = ""> <input type="button" id=“turnItOn"> </form>

Then use getElementById function document.getElementById(“turnItOn")

• Example dom.html

Programming the World Wide Web

5-15

### 5.3 Using implicit arrays

![第 16 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第16页.webp)

原文：

5.3 Using implicit arrays

• For checkbox and radio buttons, they have the same name in one group.

• Each group corresponds to one implicit array, which has the same name as the group name.

Programming the World Wide Web

5-16

### 5.3 Using implicit arrays

![第 17 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第17页.webp)

原文：

5.3 Using implicit arrays

• In the following, the array of the checkboxes, named vehicles, is the property of the form.

Programming the World Wide Web

5-17

### 5.3 Using implicit arrays

![第 18 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第18页.webp)

原文：

5.3 Using implicit arrays

• The following code is to detect how many checkboxes are checked.

Programming the World Wide Web

5-18

### Exercise

![第 19 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第19页.webp)

原文：

Exercise

• Suppose an HTML has a text box and a button.

• When you input some words in the text box, show the message with the input words once the button is pressed.

• Tips:

using forms(elements) array or getElementById function; using the value property to get the input words.

Programming the World Wide Web

5-19

### Contents

![第 20 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第20页.webp)

原文：

Contents

• 5.1 JavaScript execution environment

• 5.2 Document Object Model

• 5.3 Element access in JavaScript

• 5.4 Events and Events handling

• 5.5 Handing events from body elements

• 5.6 Handing events from button elements

• 5.7 Handing events from text box and password elements

• 5.9 Navigator object

Programming the World Wide Web

5-20

### 5.4 Events and Event Handling

![第 21 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第21页.webp)

原文：

5.4 Events and Event Handling

• Event-driven programming is a style of programming in which pieces of code, event handlers, are written to be activated when certain events occur.

• Events represent activity in the environment such as moving the mouse or the completion of the loading of a document, etc.

• An event handler is a program segment designed to execute when a certain event occurs.

Programming the World Wide Web

5-21

### 5.4 Events and Event Handling

![第 22 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第22页.webp)

原文：

5.4 Events and Event Handling

• Registration is the activity of connecting the event handler to a type of event.

(1) In HTML, assign an event attribute an event handler.

(2) In JavaScript, assign a DOM node an event handler. The example will be given later.

Programming the World Wide Web

5-22

### 5.4 Events, Attributes and Tags

![第 23 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第23页.webp)

原文：

5.4 Events, Attributes and Tags

• Particular events are associated with certain attributes of HTML tags.

• The attribute for one kind of event may appear on different tags.

Programming the World Wide Web

5-23

### 5.4 Events, Attributes and Tags (pp.203)

![第 24 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第24页.webp)

原文：

5.4 Events, Attributes and Tags (pp.203)

<table><tr><td>Event</td><td>Tag Attribute</td></tr><tr><td>blur</td><td>onblur</td></tr><tr><td>change</td><td>onchange</td></tr><tr><td>click</td><td>onclick</td></tr><tr><td>focus</td><td>onfocus</td></tr><tr><td>load</td><td>onload</td></tr><tr><td>mousedown</td><td>onmousedown</td></tr><tr><td>mousemove</td><td>onmousemove</td></tr><tr><td>mouseout</td><td>onmouseout</td></tr><tr><td>mouseover</td><td>onmouseover</td></tr><tr><td>mouseup</td><td>onmouseup</td></tr><tr><td>select</td><td>onselect</td></tr><tr><td>submit</td><td>onsubmit</td></tr><tr><td>unload</td><td>onunload</td></tr></table>

Programming the World Wide Web

5-24

### Programming the World Wide Web

![第 25 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第25页.webp)

原文：

Table 5.2 Event attributes and their tags (pp.204)

<table><tr><td>Attribute</td><td>Tag</td><td>Description</td></tr><tr><td>onblur</td><td></td><td>The link loses the input focus</td></tr><tr><td></td><td></td><td>The button loses the input focus</td></tr><tr><td></td><td></td><td>The input element loses the input focus</td></tr><tr><td></td><td></td><td>The text area loses the input focus</td></tr><tr><td></td><td></td><td>The selection element loses the input focus</td></tr><tr><td>onchange</td><td></td><td>The input element is changed and loses the input focus</td></tr><tr><td></td><td></td><td>The text area is changed and loses the input focus</td></tr><tr><td></td><td></td><td>The selection element is changed and loses the input focus</td></tr><tr><td>onclick</td><td></td><td>The user clicks on the link</td></tr><tr><td></td><td></td><td>The input element is clicked</td></tr><tr><td>ondblclick</td><td>Most elements</td><td>The user double clicks the left mouse button</td></tr><tr><td>onfocus</td><td></td><td>The link acquires the input focus</td></tr><tr><td></td><td></td><td>The input element receives the input focus</td></tr><tr><td></td><td></td><td>A text area receives the input focus</td></tr><tr><td></td><td></td><td>A selection element receives the input focus</td></tr><tr><td>onkeydown</td><td>, form elements</td><td>A key is pressed down</td></tr><tr><td>onkeypress</td><td>, form elements</td><td>A key is pressed down and released</td></tr><tr><td>onkeyup</td><td>, form elements</td><td>A key is released</td></tr><tr><td>onload</td><td></td><td>The document is finished loading</td></tr></table>

Programming the World Wide Web

5-25

### 5.4 Registering a Handler

![第 26 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第26页.webp)

原文：

5.4 Registering a Handler

• Assigning the event handler script to an event tag attribute:

• A function call can be used if the handler is longer than a single statement

Programming the World Wide Web

### 5.5 Handling Events from Body Elements

![第 27 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第27页.webp)

原文：

5.5 Handling Events from Body Elements

• See the load.html example(pp.206)

This example illustrates when the page is loaded into main memory.

• The unload event is probably more useful

Programming the World Wide Web

5-27

### Programming the World Wide Web

![第 28 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第28页.webp)

原文：

Programming the World Wide Web

5-28

### 5.4 Registering a Handler

![第 29 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第29页.webp)

原文：

5.4 Registering a Handler

An event handler function could also be registered by assigning its name to the associated event property of corresponding JavaScript object, as in the following example:

document.getElementById("myButton").onclick = myButtonHandler;

Notice that only the name of the handler function is assigned to the property—it is neither a string nor a call to the function.

Programming the World Wide Web

### 5.6 Handling Events from Button Elements

![第 30 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第30页.webp)

原文：

5.6 Handling Events from Button Elements

An event can be registered for this tag in two ways.

(1)Using an event attribute in HTML

(2)Assigning function names to a property of the element node in JavaScript

freeButtonHandler;

• Note that the function name, a reference to the function, is assigned.

Programming the World Wide Web

5-30

### 5.6 Checkboxes and Radio Buttons

![第 31 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第31页.webp)

原文：

5.6 Checkboxes and Radio Buttons

• The following examples show two different methods for registration.

Example radio\_click.html (pp.207)illustrates a script that displays an alert when a radio button is clicked.

• Note: A parameter is passed to the handler function.

• In example radio\_click2.html (pp.210), a reference to the handler function is assigned to the onclick property of each element node in JavaScript.

• Note: no parameters are passed to the function when it is called by the JavaScript. The handler code must identify the element that caused the call.

Programming the World Wide Web

5-31

### Exercise (total.html)

![第 32 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第32页.webp)

原文：

Exercise (total.html)

Develop an HTML document that has checkboxes for apple(59 cents each), orange(49 cents each), and banana(39 cents each), along with a Submit button.

• Each of the checkboxes should have its own onclick event handler. These handler add the corresponding cost of each fruit to a total cost variable totalcost.

When the submit button is pressed, the message “Your total cost is \$xxx” is shown (Tips: using alert).

Programming the World Wide Web

5-32

### 5.6 Comparing Registration Methods

![第 33 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第33页.webp)

原文：

5.6 Comparing Registration Methods

Assigning to an attribute of HTML element is more flexible, allowing passing parameters during calling functions.

• Assigning to a node property helps separate HTML and the JavaScript code.

Programming the World Wide Web

5-33

### Programming the World Wide Web

![第 34 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第34页.webp)

原文：

5.7 Handling Events from Text Box and Password Elements

• Text boxes correspond to four different events: blur, focus, change and select.

• Example nochange.html illustrates ‘blurring’ a field whenever it gains focus (pp.213).

• By manipulating the focus event, the user is prevented from changing the amount in the input box.

Programming the World Wide Web

5-34

### 5.7 Validating Form Input

![第 35 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第35页.webp)

原文：

5.7 Validating Form Input

• Checking the format and completeness of input is a common application of JavaScript.

• Advantages:

• Validating data using JavaScript provides quicker interaction for the user.

• In contrast, validity checking on the server requires a round-trip for the server to check the data and then to respond with an appropriate error page.

Programming the World Wide Web

5-35

### 5.7 Validating Form Input

![第 36 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第36页.webp)

原文：

5.7 Validating Form Input

Example pswd\_chk.html illustrates validity checking (pp.216).

Programming the World Wide Web

5-36

### Password Input

![第 37 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第37页.webp)

原文：

Figure 5.5 Display of pswd\_chk.html after it has been filled out.

Password Input

Your password

Verify password

Reset

Submit Query

Programming the World Wide Web

5-37

### Programming the World Wide Web

![第 38 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第38页.webp)

原文：

Figure 5.6 Display of pswd\_chk.html after Submit Query has been clicked

Programming the World Wide Web

5-38

### Contents

![第 39 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第39页.webp)

原文：

Contents

• 5.1 JavaScript Execution Environment

• 5.2 Document Object Model

• 5.3 Element Access in JavaScript

• 5.4 Events and Events handling

• 5.5 Handing events from body elements

• 5.6 Handing events from button elements

• 5.7 Handing events from text box and password elements

• 5.9 Navigator object

Programming the World Wide Web

5-39

### 5.10 The navigator Object

![第 40 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第40页.webp)

原文：

5.10 The navigator Object

Properties of the navigator object allow the script to determine characteristics of the browser in which the script is executing.

• The appName property gives the name of the browser.

• The appVersion gives the browser version.

• Example navigate.html (pp.232)

Programming the World Wide Web

### Summay

![第 41 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第41页.webp)

原文：

Summay

• 1 Environment

• 2 DOM model

• 3 How to access elements

• 4 Event handling

• 5 navigator object

Programming the World Wide Web

5-41

### Homework

![第 42 页](Web技术双语第5章-JavaScript与HTML文档课件.assets/第42页.webp)

原文：

Homework

Develop an HTML document that collects the following information from the user:last name, first name,middle intial, age(restricted to be greater than 17), and weight (restricted to the range of 80-300). You must have event handler for the submit button.

• Message in alert window must be produced when errors are detected.

• Exercises 5.1 (pp.237)

Programming the World Wide Web

5-42
