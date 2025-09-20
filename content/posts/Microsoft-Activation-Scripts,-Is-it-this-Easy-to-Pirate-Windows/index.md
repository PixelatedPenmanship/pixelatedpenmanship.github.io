---
title: "Microsoft Activation Scripts: Is It This Easy To Tactically Acquire Windows?"
date: 2025-03-09
draft: false
tags:
  - Technology
  - Utilities
  - Windows
  - Powershell
---
## Windows: The Most *Tactically Acquired* Operating System In The World
Windows is by far the most popular operating system in the world. So much so that it also earns the record for the most pirated piece of software in the internet... I'm from India, and I still remember using generic product keys written on the disk for activating Windows XP, 7 and even 8(My first PC that I built had Windows 8 installed this way). At the time, that was the only way we got to experience Windows without paying the exorbitant amount for an original license(6000 rupees was a lot back then... still is now). But with Windows 11 costing as much as $200 now(close to 17k rupees) this begs the question, Is it REALLY worth it to pay this much for what is now, after the recent updates, spyware? Well, I must say, the high seas are still sailing 🏴‍☠️, and there are ways to activate Windows for FREE... Enter MAS(Microsoft Activation Scripts).

## Microsoft Activation Script: Is Microsoft Knowingly Ignoring This Tool?
Before we set sail... If you do want to have the full Windows experience, but you're seasick, then there are legit product keys available at a steep discount on grey market sites like [VIP-URCDkey](https://www.vip-urcdkey.com/), [Vendafly](https://vendafly.com/), Kinguin among many others... They stay in the mostly grey area of Windows activation. They mostly sell OEM keys meant for bulk activation. The activations are legit and Windows will work as intended, but you don't have to pay the full price to get one. But if you're ready for the high seas because of the ensh\*ttification of every single service out there, well tag along mateys'... This is going to be fun...

In my early days of *tactically acquiring* stuff (From now on, this is how we'll say pirating.. Its the politically correct way... Whatever that means🤷‍♂️) we used a bunch of things for getting keys, from dubious sites like KeyGenGuru(ah... the good old days) to using KMS activator, to activate Windows... But at the risk of sounding like an old bloke, today's tools have made it so easy to get Windows activated without spending a dime. So much so, that there are actual records of **Microsoft support staff using these tools to troubleshoot Windows activation related issues🤯** Here's one anecdote from [Reddit](https://www.reddit.com/r/techsupport/comments/5b0wyy/did_Microsoft_support_just_activate_my_Windows/). Which makes me thinking... Why are we paying for this in the first place?

Well, the tool in question is called [MAS](https://massgrave.dev/) (Microsoft Activation Scripts) which is basically a collection of tools that you can use to activate Microsoft services like Windows and office...*"But these are clearly illegal... Why aren't Microsoft banning this tool?"* you might ask... Well it does appear that Microsoft knows about it and then just ignoring... Why I say so? because the script is open-source and hosted in **github**. And do you know who owns github? **Microsoft!!!** 

My hunch is that they're more concerned with adding more users that use Windows instead of forcing people to buy a legitimate copy of Windows... Basically they're playing the long game here, as when you move up to buy a new laptop, or go to enterprise, you will be using Windows and there there is little scope for getting Windows other than the legit way, so they'll make up their lost cost that way... Plus, in my opinion, some products just work better when tactically acquired (*cough...Adobe*.).


## Okay... I've Boarded The Ship... How Do I Set Sail?
Well let's get started... For this demonstration, I'll be using a Windows11 installed on a VM. But the method works the same if you have it installed on your system.. So let's begin

***
**PSA: The following tutorial is for educational purposes only... Please use it on your personal systems and DO NOT try these scripts on your work issued or enterprise devices**
***

Before we start, just to show you, this copy of Windows is not activated...
![Image Description](/images/Pasted%20image%2020250309205234.png)

#### Step 1:    
Open terminal, by right clicking the start menu and selecting Terminal(Admin)
![Image Description](/images/Pasted%20image%2020250309205424.png)

Make sure to give admin permission when asked:
![Image Description](/images/Pasted%20image%2020250309205635.png)

#### Step 2:    
Once in the terminal, paste the below command:
```
irm https://get.activated.win | iex
```
Once entered, wait for a few seconds, and this new terminal window will pop up... this is your activation tool:
![Image Description](/images/Pasted%20image%2020250309205732.png)

#### Step 3:   
Now for activating Windows, you have 3 options [HWID](https://massgrave.dev/hwid), [TSforge](https://massgrave.dev/tsforge), and KMS(in 2 ways, [KMS38](https://massgrave.dev/kms38) and [Online KMS](https://massgrave.dev/online_kms)... So technically 4). For our demonstration, I chose the HWID method. So press 1 and hit enter... and now let the script do it's magic...

Once it is done, you'll see a screen like this:
![Image Description](/images/Pasted%20image%2020250309210256.png)
press any key in the keyboard to exit...

#### Step 4:
To verify that Windows is activated, in the script home, press 6 and hit enter... if all goes well, you should see a screen like this:
![Image Description](/images/Pasted%20image%2020250309210433.png)

#### Step 5:
Reboot the system. If all is well, congrats👏 you now have a fully activated version of Windows 11 pro.
![Image Description](/images/Pasted%20image%2020250309210634.png)


## Conclusion: The Best Price is Free
Now you've got a good idea on how you can get a fully activated Windows for free, the next step might be to get MS Office for free. Thankfully, this same script can activate office as well. And here you won't get the annoying *This license is not legtimate(or something like that)* warning everytime you open office. You can see it for yourselves by going to the official site of MAS [here](https://massgrave.dev/)
And with that congrats you've officially are a member of the *Pirates of the Tech Carrebian*. Before I let you go, please, keep your tactically acquired software for yourselves, and don't share it through public resources. And with that I bid you adieu and I'll see you all in my next post...🙋‍♂️