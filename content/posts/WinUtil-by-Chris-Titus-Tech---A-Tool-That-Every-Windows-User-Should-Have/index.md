---
title: "WinUtil by Chris Titus Tech: A Tool That Every Windows User Should Have"
date: 2025-03-08
draft: false
tags:
  - Technology
  - Windows
  - Utilities
  - Powershell
---
If you use a computer, chances are that you use Windows. That operating system by Microsoft, that for the last few years many people love to hate, but afraid of switching because...well...most of us just want to have something that just works... And Windows, even with it's inconveniences does work and work well... especially if you're anything like me and use programs and games from the early 2000s (Mostly games, because... well... I'm a dinosaur). However, not all things about Windows is sunshine and rainbows, The latest update... Windows11, has it's flaws... with the redone UI, the TERRIBLE settings app, and the most recent *"feature"*, **Windows Recall**... Which is basically Microsoft Saying *"Well... We want to train our AI model, so we're just gonna spy on how you use your PC and use that data to make copilot even more annoying..."*. What!!! Other than nuking Windows for a more privacy respecting operating system (*cough... Linux*), Most people just want Windows without the privacy nightmare, and also solve some of the inconveniences that there is in the way Windows work... Thankfully, there is a solution...

Video Link: [Windows Utility in 2025](https://www.youtube.com/watch?v=IuaNw8Tpn7Q)

## The WinUtil by CTT
I've been a big fan of the youtube channel ["Chris Titus Tech"](https://www.youtube.com/@ChrisTitusTech). The guy mainly focuses on advanced tech stuff, Linux and privacy and security related stuff, and this is where I found out a way to "debloat" Windows, to make your Windows run faster. This was almost 4-5 years ago and I've been following his chronicles of making this utility since it's inception... And been using this extensively for a while. Here is what the tool does from the lion's mouth himself:
***
*"This utility is a compilation of Windows tasks I perform on each Windows system I use. It is meant to streamline _installs_, debloat with _tweaks_, troubleshoot with _config_, and fix Windows _updates_. I am extremely picky about any contributions to keep this project clean and efficient."*
<div style="text-align: right">-Chris Titus Tech</div>   

***

So let's break down the features one-by-one.

## How to Run the Thing?
Well, If you're not that tech savvy, it is going to be a bit of work, but trust me, it isn't that bad... If you're used to clicking Next...Next...Next while installing a program on Windows, then you can easily do this one as well.

First thing you need to do is to open Powershell/Terminal(Depending on if you run Windows 10 or 11). For that right click the start menu icon(on the botton left on Windows 10 or the windows icon on Windows 11, on the bottom center or bottom left corner) and select *Powershell/Terminal(Admin)*, be sure to select the one with **Admin** written in parenthesis.

![Image Description](/images/Pasted%20image%2020250308100617.png)

Once you open, click on yes on the window asking for administrator privileges, and enter the password(if asked). PSA: **Do NOT use this tool on your work issued computer**. once you're in the terminal. paste the below command.   
```
irm "https://christitus.com/win" | iex   
```   
once you hit enter... this screen will pop up and you'll be greeted with the Windows utility:   
![Image Description](/images/Pasted%20image%2020250308101125.png)
![Image Description](/images/Pasted%20image%2020250308101158.png)
***
***Note***: Future updates might change the UI a bit here and there, but the overall functionality will still remain the same
***
Now that we have the tool up and running, let's go through some of the features...

## App Installation: Just a Click Away
When you first open this script, you're greeted with a screen that looks like this...
![Image Description](/images/Pasted%20image%2020250308101602.png)
It's not bad per say, it has neatly categorized your apps into different sections and you can select each category to find the apps you need... But I prefer a more expanded view, so I change the compact view to expanded view by switching the option on the *Actions* menu. 
![Image Description](/images/Pasted%20image%2020250308101920.png)

From here, select the apps that you need, and just hit "*Install/Upgrade Selected*" in the top. And just wait... No need to download the program from the website, no need to sit through pushing Next... Next... Next. just one click, and that's it.  

if you look at the terminal that you opened, you'll be able to see what is happening in the background:
![Image Description](/images/Pasted%20image%2020250308102313.png)
From here you can also upgrade your installed programs... just click on "*Get Installed*" in the Action menu, wait a couple of seconds to get all your install packages, and then click on "*Install/Upgrade Selected*" 
![Image Description](/images/Pasted%20image%2020250308102752.png)
If you want to uninstall the program, same drill... just select the programs you want to remove and click on Uninstall selected... Done and dusted...
If you know about ninite.. this is kinda that on roids. The way this works is by using a **package manager.** If you're from the Linux space, you will be familiar. This uses one of two available for Windows: [WinGet](https://learn.microsoft.com/en-us/Windows/package-manager/winget/) or [Chocolatey](https://chocolatey.org/), depending on which you choose... and it manages the programs you require in one go... A major convenience boost.

## Tweaks: Making Windows Take on a Crash Diet
This section deals with debloating, and tweaking Windows to make it sun smoother and also more private, you may not know it, but Windows does take a whole lot of [telemetry](https://www.sumologic.com/glossary/telemetry/) about how you use your system, what programs you use and so much more... That also tanks your system performance if you run a relatively low end system or a laptop,  or both... like me... This can make Windows more usable, by eliminating the unnecessary background processes, and also make it more privacy respecting..
![Image Description](/images/Pasted%20image%2020250308104356.png)

For the average joe, I'd recommend the standard tweaks, as this makes sure to take away all the fluff while maintaining the usability of Windows... if you know what you're doing, by all means try out the other tweaks present... I've personally used the Standard tweaks along with a couple more options like:
- Disable Recall
- Set Hibernation as default(since my main system is a laptop)
- Change Windows terminal default
- Debloat edge
- Set classic right click menu(I HATE the new Windows 11 right click menu)
- Set the DNS to cloudflare   

But I still remain, the standard tweaks are good enough for most, and if you do run into any issues, you can always undo the tweaks, by selecting them and hitting "*Undo Selected Tweaks*".

## Tweaks: For the Advanced Folks Out There
I'm not going to delve a lot into this screen, as these are the tweaks that only like 20% of Windows users care about... But since I am one of those 20% I'll talk about it...   
![Image Description](/images/Pasted%20image%2020250308105413.png)
This panel let's you install various features in Windows. One that I recommend everyone to do is the first tweak, which is "*All .Net Framework*". Some programs require the .NET framework to run, and this ensures all relevant versions of the .NET framework is installed. You can also check out other features like Windows Subsystem for Linux(WSL), that lets you run Linux inside Windows (Shocker 🤯 I know right).   
Also, another feature of note, is to bring up the old school control panel options that Windows completely nuked in Windows 11(by nuking, I mean completely hid it from the user). This lets you take control of your settings in a more familiar and granular way instead of using the god-awful settings app (I can see the sysdamins scrreeching with joy...).
![Image Description](/images/Pasted%20image%2020250308110417.png)

## Updates: Prevent Windows from Forcing Stuff Down Your Throat
Windows Update.... The fewer I say about it the better... I mean the proof that microsoft is tracking us can be seen here... When we're doing something extremely critical... Here comes Windows saying "Wait for an hour.. I've got some updating to do"....🤬. Thankfully, there is a solution. Enter the updates tab:   
![Image Description](/images/Pasted%20image%2020250308112609.png)   
Here you can choose what updates come to you. I's personally recommend the **Security Settings**, as it blocks any new features that nobody will use from coming, but keeps your security patches up-to-date. Which is less annoying than your regular updates. For the adventurous out there, you *can* disable updates entirely, but do so at your own risk. Not getting patched for the gazillion vulnerabilities that pop up every now and then is not an ideal place to be in. I personally use the Security Settings option and it works like a charm, and makes Windows less annoying and lets you actually complete your work on time.

## MicroWin: Get Windows Debloated Right from the Start
![Image Description](/images/Pasted%20image%2020250308113238.png)

Introduced not that long ago, MicroWin allows you to make a debloated version of Windows, for installing on a fresh system. For anyone familiar with [Windows AME](https://ameliorated.io/), or the other custom debloated ISOs, this is kind of that but not going too extreme. MicroWin  tries to achieve a balance between usability, security and lightweight performance. You can download the latest Windows iso, and make it yourself, or let the tool do all the work for you, by downloading the latest Windows iso, and make the debloated version for you. Now you can enjoy a lightweight, privacy respecting version of Windows. And you don't need a Microsoft account to use it... How cool is that?!

## Conclusion: Reclaim Your Windows Experience
Windows, for all its quirks and privacy concerns, remains a reliable workhorse for many. The WinUtil by Chris Titus Tech offers a powerful way to tailor your Windows experience, striking a balance between functionality, privacy, and performance. Whether you're a tech novice looking for a smoother experience or a seasoned user wanting granular control, this utility provides a valuable toolkit.

From simplifying app installations to minimizing telemetry and managing updates, WinUtil allows you to take charge of your operating system and reduce the annoyances that often plague Windows. And with MicroWin, you can even start with a debloated base, ensuring a clean and efficient system from the get-go.

While alternatives like Linux exist, switching can be a daunting task. WinUtil provides a practical alternative, allowing you to stay within the familiar Windows ecosystem while significantly enhancing its privacy and performance. So, if you're looking to make Windows "just work" better, give the WinUtil a try. You might be surprised at the level of control you can achieve. Remember to proceed with caution, understand the implications of each tweak, and most importantly, **do not use this tool on your work-issued computer**. Now go forth and reclaim your Windows experience!