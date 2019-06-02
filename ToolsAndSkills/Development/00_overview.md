Python Tools & Skills
=====================

**Development**

Dr. Yves J. Hilpisch | The Python Quants GmbH

Certificate Program, June 2018

(short link to this Gist: http://bit.ly/tools_skills_dev)

<img src="http://hilpisch.com/images/finaince_visual_low.png" width=300px>


Slides
------

You find the slides under:

http://hilpisch.com/tools_skills_dev.pdf


Contents
--------

This Gist contains files related to the **Development** part of Tools & Skills.


Vim Tutorial
------------

This is a nice, interactive **Vim tutorial** to get started with the basics:

http://www.openvim.com


Docker Container
----------------

Using a Docker container should simplify working with the tools presented in this part of the class. You should download and unzip the Gist content, then navigate to the folder with the files and do:

    docker run -ti -h tools -p 9999:9999 -v $(pwd):/root/gist ubuntu:latest /bin/bash

In the Docker container, to install the tools required execute:

    cd /root/gist
    bash install.sh

This also copies the Vim configuration file to the right location.

References
----------

These books are helpful for the topics covered in this part:

* Janssens, Jeroen (2015): _Data Science on the Command Line_. O'Reilly.
* Robbins, Arnold (2016): _Bash Pocket Reference_. 2nd edition, O'Reilly.
* Robbins, Arnold (2011): _vi and Vim Editors Pocket Reference_. 2nd edition, O'Reilly.
* Silverman, Richard (2013): _Git Pocket Guide_. O'Reilly.

There is a free online book about Git available:

* https://git-scm.com
* https://git-scm.com/book/en/v2

Links to package documentations:

* `doctest`: https://docs.python.org/3/library/doctest.html
* `unittest`: https://docs.python.org/3/library/unittest.html

<img src="http://hilpisch.com/tpq_logo.png" width=250px>
