Python Tools & Skills
=====================

**Basics**

Dr. Yves J. Hilpisch | The Python Quants GmbH

Certificate Program, May 2018

(short link to this Gist: http://bit.ly/tools_skills_basics)

(short link to Gist for cloud files: http://bit.ly/tools_skills_cloud)

<img src="http://hilpisch.com/images/finaince_visual_low.png" width=300px>


Slides
------

You find the slides under http://hilpisch.com/tools_skills_basics.pdf

<img src="http://hilpisch.com/images/finaince_logo.png" width=300px>

Useful Links
------------
* https://conda.io/miniconda.html - downloading `Miniconda`
* https://conda.io/docs/using/envs.html - managing environments with `conda`
* http://jupyter-notebook.readthedocs.io/en/stable/public_server.html - running a `Jupyter` server
* https://docs.docker.com/get-started/ - getting started with Docker
* https://m.do.co/c/fbe512dd3dac - 10 USD credit for DigitalOcean
* https://store.docker.com/editions/community/docker-ce-desktop-windows - Download Docker for Windows

Mac/Linux Tips
==============

SSH Keys on Mac/Linux
---------------------
Open the shell and type:

    ssh-keygen

Accept the defaults a couple of times or change e.g. the name of the key pair (see below). The passphrase it to secure the private key. Skip it maybe for training purposes, use it for production scenarios. The generated key pair is found by default in the folder `~/.ssh`.

An example session might look as follows:

    (base) macbookpro:~/Dropbox/Program/skills/cloud$ ssh-keygen
    Generating public/private rsa key pair.
    Enter file in which to save the key (/Users/yves/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /Users/yves/.ssh/id_rsa.
    Your public key has been saved in /Users/yves/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:bbLvvt05AOq9yRaByx0X1LA3DnLjdd9AFROszAey2BI yves@macbookpro
    The key's randomart image is:
    +---[RSA 2048]----+
    |           .ooo=+|
    |         E ..+...|
    |         .= X.B .|
    |        .++*.X =o|
    |       .S++=. o o|
    |        ++o .    |
    |       ... . .   |
    |        .ooo ... |
    |         +Oo. o. |
    +----[SHA256]-----+
    (base) macbookpro:~/Dropbox/Program/skills/cloud$ 

You can then access, for instance, the public key via (e.g. to copy it to DigitalOcean):

    (base) macbookpro:~/Dropbox/Program/skills/cloud$ vim ~/.ssh/id_rsa.pub

Droplet Set-up from Shell
-------------------------

Make sure to have downloaded and upzipped the files required for the Droplet set-up on DigitalOcean (see http://bit.ly/tools_skills_cloud). Navigate on the Shell to the folder with the files.

The do the following, where `$IP_ADDRESS` is the IP address of your droplet for which you have provided your SSH key (see above):

    bash setup.sh $IP_ADDRESS

Watch the `install.sh` script do its work. Afterwards, access the Jupyter Notebook server in the browser via `https://$IP_ADDRESS:8888` (need to maybe add a security exception).


Windows Tips
============

Vim on Windows
--------------
* https://www.vim.org/download.php - Download Vim for Windows
* http://www.expatpaul.eu/2014/04/vim-in-powershell/ - Vim in PowerShell


Scoop on Windows
----------------
See https://github.com/lukesampson/scoop. It allows you to install certain Linux(-like) packages for the PowerShell.

To install, open the PowerShell and execute (maybe as administrator):

    iex (new-object net.webclient).downloadstring('https://get.scoop.sh')

After that, check the installation via

    scoop help

You can now do e.g.:

    scoop install git
    scoop install wget
    scoop install openssh
    scoop install openssl


OpenSSH on Windows
------------------
Instead of using functionality from the Scoop installed `openssh`, it might be necessary to install `OpenSSH` directly as a `WindowsCapability` (see this [tutorial](https://blogs.msdn.microsoft.com/powershell/2017/12/15/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/)). First check availability:

    Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'

Second, install it:

    Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0


SSH Keys on Windows
---------------------
Make sure to have `OpenSSH` installed. Open the PowerShell and execute

    ssh-keygen

Accept the defaults a couple of times. The SSH key pair is found by default under `C:\Users\$USER\.ssh`. The passphrase it to secure the private key. Skip it maybe for training purposes, use it for production scenarios. An example session might look like:

    PS C:\Users\User> ssh-keygen
    Generating public/private ed25519 key pair.
    Enter file in which to save the key (C:\Users\User/.ssh/id_ed25519): 
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in C:\Users\User/.ssh/id_ed25519.
    Your public key has been saved in C:\Users\User/.ssh/id_ed25519.pub.
    The key fingerprint is:
    SHA256:cQlxOg7cWgTuV6XzMgXb/eKWk8iueap+S+avVpX7Fpo User@MACHINE@machine
    The key's randomart image is:
    +--[ED25519 256]--+
    |      ..+.o .    |
    |     o o + B .   |
    |      + * B o .. |
    |     . = = +  o. |
    |      o S o .....|
    |       .   +.o.= |
    |          o.o O..|
    |         +oo.E .o|
    |       .o+BBo  . |
    +----[SHA256]-----+
    PS C:\Users\User> ls .ssh


        Directory: C:\Users\User\.ssh


    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    -a----       27/05/2018     09:44            411 id_ed25519
    -a----       27/05/2018     09:44            103 id_ed25519.pub
    -a----       27/05/2018     10:04            292 known_hosts


    PS C:\Users\User>

To copy the public key (for use e.g. with DigitalOcean) exeute e.g.:

    notepad C:\Users\$USER\.ssh\id_ed25519.pub


Droplet Set-up from PowerShell
------------------------------

Make sure to have downloaded and upzipped the files required for the Droplet set-up on DigitalOcean (see http://bit.ly/tools_skills_cloud). Navigate on the PowerShell to the folder with the files.

From the PowerShell the `setup.sh` cannot be executed. Instead do the following, where `$IP_ADDRESS` is the IP address of your droplet for which you have provided your SSH key (see above):

    scp -v cert.key cert.pem jupyter_notebook_config.py install.sh root@$IP_ADDRESS:/root

The login in to the Droplet via `ssh`:

    ssh -v root@$IP_ADDRESS

Afterwards do:

    bash install.sh

Watch the `install.sh` script do its work. Afterwards, access the Jupyter Notebook server in the browser via `https://$IP_ADDRESS:8888` (need to maybe add a security exception).

References
----------
These books are all available on https://www.safaribooksonline.com. We recommend a subscription to this service that provides access to 100s of useful books. Books can also be downloaded to an iPad, for instance, and be read offline.

Some references for Linux OS:

* Robbins, Arnold (2016): _Bash Pocket Reference_. 2nd edition, O'Reilly.
* Matthias, Karl and Sean P. Kane (2015): _Docker: Up & Running_. O'Reilly.

Some references covering Python tools (e.g. IPython) and Python data analysis in general:

* McKinney, Wes (2017): _Python for Data Analysis_. 2nd edition, O'Reilly.
* VanderPlas, Jake (2016): _Python Data Science Handbook_. O'Reilly.



<img src="http://hilpisch.com/tpq_logo.png" width=250px>