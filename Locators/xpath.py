'''
Xpath :
Xpath is defined as XML path
It is a syntax or language for finding any element on the web page using XML path expression
Xpath is used to find the location of any element on the webpage using HTML DOM Structure
Xpath can be used to navigate through elements and attributes in DOM
Xpath is an address of an element
'''

'''
DOM : Document Object Model
* DOM is an API interface provided by browser
* When a webpage is loaded, the browser creates DOM of a page
* XML Expression works on the DOM and not on the HTML page >> If DOM is not loaded XML syntax 
won't work
'''
'''
Types of Xpath:
1. Absolute Xpath/Full Xpath
2. Relative Xpath/Partial Xpath

Diffrence between absolute and relative xpath:
1. Absolute xpath starts from root html node
   Relative xpath directly jumps to element on DOM
2. Absolute xpath starts with //
   Relative xpath starts with /
3. In Absolute xpath we use only nodes or tags
   In Relative xpath we use attributes
'''
'''
How to write xpath:
* Always go from element which u wanted to locate and move upwards to parent node 

Syntax for relative xpath:
//tagname[@attribute='value']
//*[@attribute='value']  >> * means it will search for all nodes whereever attribute meets it w
will directly jumps to attribute given

How to capture xpath automatically
1. Right click > Inspect > copy relative / abs xpath  >> provided by browser itself
2. Selectorshub  >> most used plugin 

2 Resons to prefer relative xpath:
1. If developer introduces new element then the absolute xpath will be broken
2. If developer changes the location of element then absolute xpath will be broken
hence absolute xpath is unstable.
'''

'''
Other ways of xpath syntax:
1. or  >> here either of the locators attributes should be matched
//tagname[@att1='val1' or @att2='val2']
2. and >> here both of the locators attributes should be matched
//tagname[@att1='val1' and @att2='val2']
3. contains(): if locators are dynamic in type then we can use this
//tagname[contains(@att,'val')]
4.starts-with: if locators are starts with definite value 
//tagname[starts-with(@att,'val')]
5. text():
//tagname[text()="partial text or full text name"]

'''