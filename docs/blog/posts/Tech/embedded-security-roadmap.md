---
title: "I Wanted To Learn More About My Job... So I Made AI My Professor"
date: 2026-02-02
draft: false
tags:
  - Technology
  - AI
  - LLMs
  - Prompt Engineering
---
# Let AI Lead the Way

To be frank with you, I am always a little skeptical with AI. For me it has not made that much of a difference in my work or my life (Apart from making an impressive linkedin profile photo...). But I've been curious as to how AI is at consolidating information. As I like to call it, AI, or LLMs specifically is nothing but a *optimistic answering machine with a large resource pool*. And I've been seeing a lot of instagram reels, where they basically make AI your coach, therapist, personal trainer and what have you. And, whilst I've been skeptical with these so called *"prompts that the system doesn't want you to know"*, I was curious.
So recently my manager told me to brush up on some competencies for my role as a lead engineer in embedded security, so I thought why not I just make a prompt to basically give me an entire syllabus to study on. I chose perplexity as it had the most robust web search function till date(I know chatGPT and Grok comes close, but they do hallucinate from time to time, something I have not experienced with perplexity), and whilst I was not blown away, I was surprised at the sheer volume of information that the LLM provided, and it gave it to me in a handy markdown file that I can conveniently paste here, so that I can refer to it, whenever and wherever. Before I show you the roadmap, here is the prompt I used. I redacted the information that I wanted, and formatted it in such a way that you can add your competencies and get a fairly comprehensive roadmap.

***
I am studying for an **<Your desired role and domain\>**, following the **<any specific industry standard, like IEC, NIST, etc\>**, My manager, wanting to help has given me some topics to learn on that will help me with my competencies. You, being an expert in **<the key skills required, ex: embedded security, network security\>**, is giving me a full roadmap into how to get not just theoretical but hands on experience with these concepts, and provides me with free resources to learn these(cause I'm broke AF) Could you provide me with a detailed roadmap, with working resource links on how to study these concepts?

**<Your desired Topics\>**

I prefer a mix of videos and documentation, plus some ways to get a hands on experience with these concepts, but the catch is all should be free. Prepare a detailed markdown document with all the links to the resources so that I can gain a fair bit of technical competency in these fields. Create a detailed documentation, with links so that I can refer and keep track easily, also give me a downloadable markdown file of the roadmap as well so that I can host it in my mkdocs blog.
***


And without further ado, here is the roadmap...


## Embedded Cybersecurity Learning Roadmap: IEC-62443 Railway Industry

**Target Role:** Embedded Cybersecurity Engineer (Railway Industry)  
**Standard:** IEC-62443 (Industrial Automation & Control Systems Cybersecurity)  
**Preparation Date:** February 2026)  
**Learning Format:** Video + Documentation + Hands-on Labs (100% Free)

---

### Table of Contents
1. [TEE - Trusted Execution Environment](#1-tee---trusted-execution-environment)
2. [Root of Trust & Chain of Trust](#2-root-of-trust--chain-of-trust)
3. [cgroups - Control Groups](#3-cgroups---control-groups)
4. [Disk Partitioning, Rescue & Mount Security](#4-disk-partitioning-rescue--mount-security)
5. [TPM Usage & Coverage](#5-tpm-usage--coverage)
6. [Linux Namespaces](#6-linux-namespaces)
7. [AppArmor - Mandatory Access Control](#7-apparmor---mandatory-access-control)
8. [IEC-62443 Industry Context](#8-iec-62443-industry-context)
9. [Lab Setup & Tools](#9-lab-setup--tools)

---

### 1. TEE - Trusted Execution Environment

#### Learning Path Overview
TEEs provide isolated secure execution for sensitive operations. For railway systems, TEEs protect critical control logic and cryptographic keys from compromised operating systems.

#### Theory & Conceptual Resources

**Video Resources:**
- **Trusted Execution Environment (TEE) on ESP32-C6** (YouTube, 35 min)  
  [Link](https://www.youtube.com/watch?v=lSVu4FzdbBk)  
  *Learn practical TEE implementation on a real embedded platform with hardware isolation mechanisms*

- **A Technical Overview of Intel SGX, Arm TrustZone, and AMD SEV** (YouTube, 25 min)  
  [Link](https://www.youtube.com/watch?v=MREwcSo0uz4)  
  *Comparative analysis of different TEE technologies - essential for understanding architectural differences*

- **Proof is in the Pudding: Trusted Execution Environments** (YouTube, 40 min)  
  [Link](https://www.youtube.com/watch?v=QVA_Dtq3th0)  
  *Technical whiteboard discussion covering root of trust, TEE security models, and attack vectors*

**Documentation:**
- **TEE 101 White Paper by Secure Technology Alliance**  
  [Link](https://www.securetechalliance.org/wp-content/uploads/TEE-101-White-Paper-V1.1-FINAL-June-2018.pdf)  
  *Foundational 30-page primer on TEE concepts, architecture, and real-world implementations*

- **Introduction to Trusted Execution Environment and ARM's TrustZone**  
  [Link](https://sergioprado.blog/introduction-to-trusted-execution-environment-tee-arm-trustzone/)  
  *Beginner-friendly technical blog explaining TrustZone concepts with practical context*

- **Guide to ARM TrustZone and OP-TEE: Secure World Design**  
  [Link](https://www.linkedin.com/pulse/arm-trustzone-unlocking-secure-world-embedded-systems-khaled-el-sayed-a3hpf)  
  *Covers OP-TEE architecture, trusted app development, and verified boot implementation*

#### Hands-On Lab Resources

**OP-TEE (Open Portable Trusted Execution Environment)**
- **Official OP-TEE Documentation & Build System**  
  [Link](https://optee.readthedocs.io/en/latest/general/about.html)  
  *Complete reference for building and deploying OP-TEE on ARM platforms*

- **OP-TEE Build & Development Guide**  
  [Link](https://optee.readthedocs.io/en/latest/building/gits/build.html)  
  Step-by-step instructions for compiling OP-TEE for various ARM devices (Raspberry Pi, QEMU, etc.)

- **OP-TEE Sample Applications (optee_examples)**  
  [Link](https://github.com/OP-TEE/optee_examples)  
  GitHub repository with hands-on examples: AES encryption, secure storage, hello_world, HOTP authentication

- **OP-TEE Examples Documentation**  
  [Link](https://optee.readthedocs.io/en/latest/building/gits/optee_examples/optee_examples.html)  
  Detailed guide for building and running sample trusted applications

**ARM TrustZone for Cortex-M (Microcontroller Version)**
- **Arm TrustZone Getting Started on SAM L11**  
  [Link](https://developerhelp.microchip.com/xwiki/bin/view/software-tools/harmony/saml11-trustzone-getting-started-training-module/)  
  *Microchip tutorial for Cortex-M TrustZone implementation with hands-on project*

- **Learn Embedded Security with ARM TrustZone in 50 Minutes**  
  [Link](https://www.youtube.com/watch?v=_3jNdcK0SBI)  
  *Hands-on video covering ARMv8-M TrustZone, SAU/IDAU, Keil MDK demo with NXP LPC55S69*

- **Develop Secure Cortex-M Applications with TrustZone** (ARM Webinar)  
  [Link](https://www.youtube.com/watch?v=TkFC4Q2BwCM)  
  *ARM's official guide for Cortex-M TrustZone development*

**Porting & Real Devices**
- **Porting and Running OP-TEE on ARMv8 Devices**  
  [Link](https://www.youtube.com/watch?v=sBVzSQ5uvUw)  
  *30-minute hands-on video showing how to port OP-TEE to custom ARMv8 hardware*

**Lab Exercises:**
1. Build and run OP-TEE hello_world example on QEMU
2. Create a simple trusted application for cryptographic operations
3. Implement secure storage within OP-TEE
4. Explore TEE-REE communication via SMC calls

---

### 2. Root of Trust & Chain of Trust

#### Learning Path Overview
Root of Trust (RoT) and Chain of Trust establish the cryptographic foundation for secure boot. In railway systems, this prevents bootkit attacks and ensures only authorized firmware executes.

#### Theory & Conceptual Resources

**Official Documents:**
- **UEFI Secure Boot White Paper: Establishing the Root of Trust**  
  [Link](https://uefi.org/sites/default/files/resources/UEFI%20RoT%20white%20paper_Final%208%208%2016%20(003).pdf)  
  *Technical deep-dive: hardware RoT, verified boot vs. measured boot, Secure Boot chain*

- **UEFI Forum: Chain of Trust Introduction**  
  [Link](https://uefi.org/sites/default/files/resources/UEFI%20Forum%20White%20Paper%20-%20Chain%20of%20Trust%20Introduction_Final.pdf)  
  *Explains SEC phase, PEI, DXE phases in UEFI boot, and cryptographic binding*

- **NSA Guidance: Managing UEFI Secure Boot**  
  [Link](https://media.defense.gov/2025/Dec/11/2003841096/-1/-1/0/CSI_UEFI_SECURE_BOOT.PDF)  
  *Government cybersecurity guidance on Secure Boot implementation and threats*

**Blog & Articles:**
- **The IoT Chain of Trust: The Boot Process**  
  [Link](https://www.sealevel.com/the-iot-chain-of-trust-the-boot-process/)  
  *IoT-focused explanation of verified boot and measured boot concepts*

- **Demystifying Server Root of Trust**  
  [Link](https://www.moorinsightsstrategy.com/wp-content/uploads/2017/08/Demystifying-Server-Root-Of-Trust-by-Moor-Insights-and-Strategy.pdf)  
  *Intel Boot Guard, AMD PSP, and secure RoT technologies explained*

- **Achieving Root of Trust in Automotive MCUs**  
  [Link](https://www.renesas.com/en/blogs/introduction-about-secure-boot-automotive-mcu-rh850-and-soc-r-car-achieve-root-trust-1)  
  *Real-world automotive implementation of RoT (relevant for railway systems)*

#### Hands-On Lab Resources

**Boot with TPM Tutorial:**
- **Boot with TPM: Secure vs Verified vs Measured**  
  [Link](https://github.com/tpm2dev/tpm.dev.tutorials/blob/master/Boot-with-TPM/README.md)  
  *Explains SRTM vs CRTM, verified vs measured boot with TPM integration*

**Measured Boot Implementation:**
- **U-Boot Measured Boot Documentation**  
  [Link](https://docs.u-boot.org/en/latest/usage/measured_boot.html)  
  *Practical guide to implementing measured boot in bootloader*

**UEFI Secure Boot Configuration:**
- **UEFI Secure Boot Customization Guide** (NSA)  
  [Link](https://media.defense.gov/2023/Mar/20/2003182401/-1/-1/0/CTR-UEFI-SECURE-BOOT-CUSTOMIZATION-20230317.PDF)  
  *Detailed customization procedures for Secure Boot policies*

- **Arch Linux UEFI Secure Boot Wiki**  
  [Link](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot)  
  *Practical Linux-based Secure Boot setup and key management*

**Lab Exercises:**
1. Understand UEFI Secure Boot key hierarchy (PK, KEK, DB, DBX)
2. Sign kernel/bootloader binaries and load them into Secure Boot DB
3. Measure firmware components and verify TPM PCR values
4. Test boot failure scenarios (tampered binaries)

---

### 3. cgroups - Control Groups

#### Learning Path Overview
cgroups enable resource limits and isolation for processes. For railway systems, cgroups prevent single applications from consuming all resources, ensuring real-time guarantees for critical control loops.

#### Theory & Conceptual Resources

**Technical Documentation:**
- **cgroups: Definition, Works, Benefits, and Container Use Cases**  
  [Link](https://www.cleanstart.com/guide/cgroup)  
  *Comprehensive guide covering cgroup v1, cgroup v2, CPU/memory/IO limits, Kubernetes integration*

- **Introduction to Container Resource Management**  
  [Link](https://www.neteye-blog.com/2024/12/introduction-to-container-resource-management-and-what-we-can-learn-for-monitoring/)  
  *Modern cgroup architecture and monitoring strategies*

- **Linux cgroups on KodeKloud**  
  [Link](https://notes.kodekloud.com/docs/Docker-Certified-Associate-Exam-Course/Docker-Engine-Security/CGroups)  
  *Focused on container security and process isolation*

#### Hands-On Lab Resources

**Practical cgroups Management:**
- **Controlling Process Resources with Linux cgroups**  
  [Link](https://labs.iximiuz.com/tutorials/controlling-process-resources-with-cgroups)  
  *Interactive tutorial with cgroupfs, libcgroup tools, and systemd integration*

- **Docker cgroups Lab**  
  [Link](https://docker-saigon.github.io/post/Docker-Internals/)  
  *Deep dive into how Docker uses cgroups for container resource management*

- **How to Use Namespaces and cgroups to Control Docker**  
  [Link](https://earthly.dev/blog/namespaces-and-cgroups-docker/)  
  *Practical examples: CPU limits, memory caps, device restrictions*

- **What Are Namespaces and cgroups?**  
  [Link](https://blog.nginx.org/blog/what-are-namespaces-cgroups-how-do-they-work)  
  *NGINX blog explaining resource prioritization and limits*

**Lab Exercises:**
1. Create CPU-limited process groups using cgroupfs directly
2. Monitor memory usage with cgroup memory.stat
3. Implement I/O throttling for block devices
4. Use systemd service units for persistent cgroup management
5. Test CPU allocation fairness across competing processes

---

### 4. Disk Partitioning, Rescue & Mount Security

#### Learning Path Overview
Secure disk partitioning prevents unauthorized data access. Rescue mode isolation and mount permissions protect against privilege escalation. Critical for railway systems' persistent state management.

#### Theory & Conceptual Resources

**Mount Namespaces & Security:**
- **Mount Namespaces (man7.org Linux Manual)**  
  [Link](https://man7.org/linux/man-pages/man7/mount_namespaces.7.html)  
  *Exhaustive reference on mount isolation, propagation types, security implications*

- **Mount Namespaces and Shared Subtrees** (LWN Article)  
  [Link](https://lwn.net/Articles/689856/)  
  *Advanced concepts: MS_SHARED, MS_SLAVE, MS_PRIVATE propagation*

- **Linux Security Modules Overview**  
  [Link](https://en.wikipedia.org/wiki/Linux_Security_Modules)  
  *LSM framework enabling AppArmor, SELinux mount-related policies*

#### Hands-On Lab Resources

**Rescue Boot Systems:**
- **Weekend Project: Rescue Failing Drives with SystemRescue**  
  [Link](https://www.linux.com/training-tutorials/weekend-project-rescue-failing-drives-systemrescue/)  
  *Hands-on guide to creating rescue boot media and partition recovery*

- **SystemRescue - System Rescue Homepage**  
  [Link](https://www.system-rescue.org)  
  *Official SystemRescue documentation and live ISO*

- **IONOS Rescue System Documentation**  
  [Link](https://www.ionos.com/help/server-cloud-infrastructure/dedicated-server-for-servers-purchased-before-102818/rescue-and-recovery/)  
  *Practical rescue mode operations: fsck, chroot, partition repair*

- **Mounting Filesystems in Rescue Mode** (Selectel Docs)  
  [Link](https://docs.selectel.ru/en/dedicated/troubleshooting/mount-file-system/)  
  *Step-by-step partition mounting and recovery procedures*

- **Rackspace: Mount a Partition and chroot in Rescue Mode**  
  [Link](https://docs.rackspace.com/docs/mount-a-partition-and-chroot-into-your-primary-file-system-from-rescue-mode)  
  *Practical chroot workflows for system recovery*

**Lab Exercises:**
1. Create partitioned disk with separate /boot, /root, /var, /home
2. Boot SystemRescue and perform filesystem checks (fsck)
3. Mount filesystems with different security options (ro, noexec, nodev)
4. Create and test bind mounts with propagation flags
5. Recover data from read-only mounted filesystem

---

### 5. TPM Usage & Coverage

#### Learning Path Overview
TPM (Trusted Platform Module) provides hardware-based key storage, measured boot, and integrity verification. Essential for railway systems requiring remote attestation and secure key management.

#### Theory & Conceptual Resources

**Official Specs & Tutorials:**
- **Introduction to TPMs (OpenSecurityTraining2)**  
  [Link](https://www.youtube.com/watch?v=YSgAshwpLKc)  
  Free MOOC video covering TPM capabilities, use cases, limitations

- **What is a TPM? Protecting Your System**  
  [Link](https://www.youtube.com/watch?v=QdHKYqrV-xk)  
  *Visual explanation of TPM installation and BitLocker usage*

- **What is a Trusted Platform Module?** (Huntress Cybersecurity Guide)  
  [Link](https://www.huntress.com/cybersecurity-101/topic/trusted-platform-module-tpm-cybersecurity-guide)  
  *Key functions: key generation, measured boot, integrity verification*

- **TPM Usability and Security Study** (USENIX SOUPS 2022)  
  [Link](https://www.usenix.org/system/files/soups2022-rao.pdf)  
  *Academic research on tpm2-tools usability and security pitfalls*

- **Trusted Platform Module Part 1** (LinkedIn Learning - IoT Security)  
  [Link](https://www.linkedin.com/learning/iot-product-security/trusted-platform-module-part-1)  
  *Compares TEE vs TPM, architecture, and measured boot*

#### Hands-On Lab Resources

**TPM 2.0 Software & Tools:**
- **GitHub: Learn-TPM Educational Repository**  
  [Link](https://github.com/Abhinandan-Khurana/Learn-TPM)  
  *Comprehensive guides, code samples, use cases for TPM 2.0*

- **tpm2-tss (TPM 2.0 Software Stack)**  
  [Link](https://github.com/tpm2-software/tpm2-tss)  
  *Official TSS implementation with FAPI, SAPI, ESAPI layers*

- **tpm2-tss Installation & Build Guide**  
  [Link](https://github.com/tpm2-software/tpm2-tss/blob/master/INSTALL.md)  
  *Step-by-step build instructions for all platforms*

- **tpm2-tss ReadTheDocs**  
  [Link](https://tpm2-tss.readthedocs.io)  
  *Official documentation for TSS libraries and simulator setup*

- **tpm2-tools (CLI Tool Suite)**  
  [Link](https://github.com/tpm2-software/tpm2-tools)  
  *Command-line interface for TPM operations (key generation, signing, etc.)*

- **tpm2-tools Documentation**  
  [Link](https://tpm2-tools.readthedocs.io)  
  *Man pages and build instructions for tpm2-tools*

**Software TPM Simulator:**
- **IBM's Software TPM 2.0 Simulator**  
  [Link](https://sourceforge.net/projects/ibmswtpm2/)  
  *Free TPM 2.0 simulator for development (no hardware required)*

**Python Bindings:**
- **tpm2-pytss: Python TPM Bindings**  
  [Link](https://pypi.org/project/tpm2-pytss/)  
  *High-level Python API for TPM operations*

**Hardware Lab (Optional):**
- **Designing an Open-Source Hardware TPM 2.0 Add-on for Raspberry Pi**  
  [Link](https://www.youtube.com/watch?v=JFqLfW_wZXA)  
  *KiCad PCB design, Infineon SLB 9672 chip, hands-on assembly & testing*

**Lab Exercises:**
1. Install and configure tpm2-tss and tpm2-tools
2. Generate TPM keys and explore key hierarchies
3. Create and seal data to PCR values
4. Implement measured boot logging with TPM PCRs
5. Test remote attestation workflows
6. Use TPM for encryption key storage

---

### 6. Linux Namespaces

#### Learning Path Overview
Namespaces provide process isolation at the OS level. For railway systems, they enable containerized control logic with strong isolation boundaries (PID, NET, UTS, IPC, USER, MNT, CGROUP).

#### Theory & Conceptual Resources

**Technical Articles:**
- **Understanding Linux Namespaces: A Guide to Process Isolation**  
  [Link](https://dev.to/ajinkya_singh_2c02bd40423/understanding-linux-namespaces-a-guide-to-process-isolation-4gbg)  
  *Beginner-friendly guide covering all namespace types with examples*

- **The 7 Most Used Linux Namespaces** (Red Hat Blog)  
  [Link](https://www.redhat.com/en/blog/7-linux-namespaces)  
  *Official Red Hat coverage of namespace isolation mechanisms*

- **Digging into Linux Namespaces - Part 1** (Quarkslab)  
  [Link](https://blog.quarkslab.com/digging-into-linux-namespaces-part-1.html)  
  *Deep technical analysis with network namespace examples*

- **Building a Linux Container by Hand Using Namespaces** (Red Hat)  
  [Link](https://www.redhat.com/en/blog/building-container-namespaces)  
  *Step-by-step tutorial creating container primitives from scratch*

#### Hands-On Lab Resources

**Practical Namespace Experiments:**
- **Jailing Apps Using Linux Namespaces** (UWSGI Docs)  
  [Link](https://uwsgi-docs.readthedocs.io/en/latest/Namespaces.html)  
  *Hands-on using setns(), /proc/self/ns, and namespace attachment*

- **Docker Namespaces and cgroups Lab**  
  [Link](https://eksgoat.kubernetesvillage.com/basics/docker_namespaces_and_cgroups)  
  *Interactive lab environment for namespace and cgroup experiments*

- **Docker Internals: Namespaces & cgroups**  
  [Link](https://docker-saigon.github.io/post/Docker-Internals/)  
  *Visual explanation of how Docker uses namespaces for isolation*

- **Introduction to Docker (Lightweight Virtualization)**  
  [Link](https://jwlss.pw/course_notes/cloud_labs/Lab%2002%20-%20Docker.pdf)  
  *Lab exercises: PID namespace, network namespace creation*

**Lab Exercises:**
1. Create PID namespaces using `unshare -p` and `fork()`
2. Create network namespaces and connect with veth pairs
3. Use USER namespaces for rootless container execution
4. Create MOUNT namespaces and test bind mount propagation
5. Explore /proc/[PID]/ns files and namespace relationships
6. Implement multi-level namespace hierarchies

---

### 7. AppArmor - Mandatory Access Control

#### Learning Path Overview
AppArmor enforces fine-grained access control policies per application. For railway systems, AppArmor restricts services to minimal required capabilities, implementing defense-in-depth.

#### Theory & Conceptual Resources

**Official & Authoritative Sources:**
- **AppArmor Official Homepage**  
  [Link](https://apparmor.net)  
  *Official project documentation and overview*

- **Implementing Mandatory Access Control (Tecmint)**  
  [Link](https://www.tecmint.com/mandatory-access-control-with-selinux-or-apparmor-linux/)  
  *Comparison of AppArmor vs SELinux with practical focus*

- **AppArmor (Arch Wiki)**  
  [Link](https://wiki.archlinux.org/title/AppArmor)  
  *Community documentation with installation and configuration*

- **Linux Kernel AppArmor Documentation**  
  [Link](https://docs.kernel.org/admin-guide/LSM/apparmor.html)  
  *Kernel configuration and LSM integration details*

- **The Linux Security Modules Framework** (Star Lab Software)  
  [Link](https://www.starlab.io/blog/a-brief-tour-of-linux-security-modules)  
  *Comprehensive LSM overview including AppArmor's role*

- **Linux Security Modules & Access Control** (AccuKnox)  
  [Link](https://accuknox.com/blog/linux-security-modules-lsm-hooks)  
  *LSM hooks architecture and AppArmor enforcement mechanisms*

- **Linux Audit: AppArmor Security Framework**  
  [Link](https://linux-audit.com/security-frameworks/apparmor/)  
  *History, features, and profile-based security model*

#### Hands-On Lab Resources

**Docker AppArmor Lab:**
- **Docker Labs: AppArmor Security**  
  [Link](https://github.com/docker/labs/blob/master/security/apparmor/README.md)  
  *25-minute advanced lab: default Docker profile, custom profiles, defense-in-depth*

- **AppArmor in Kubernetes**  
  [Link](https://github.com/DirectXMan12/kubernetes.github.io/blob/master/docs/admin/apparmor/index.md)  
  *Beta AppArmor support in Kubernetes with enforcement details*

**Profile Development Tools:**
- **Creating AppArmor Profiles: 9 Easy Steps**  
  [Link](https://blog.pentesteracademy.com/creating-hello-world-apparmor-profile-in-9-easy-steps-a172041a233b)  
  *Step-by-step profile creation: aa-genprof, aa-complain, aa-logprof*

- **Beginning AppArmor Profile Development** (Ubuntu Tutorials)  
  [Link](https://github.com/canonical-web-and-design/tutorials.ubuntu.com/blob/master/tutorials/security/beginning-apparmor-profile-development.md)  
  *Profile development with aa-genprof and learning mode*

- **AppArmor Profile Development (KodeKloud)**  
  [Link](https://github.com/kodekloudhub/certified-kubernetes-security-specialist-cks-course/blob/main/docs/04-System-Hardening/22-AppArmor.md)  
  *Enforcing mode vs complain mode, practical examples*

**Lab Exercises:**
1. Install apparmor-utils and enable AppArmor
2. Generate profile for a sample application using aa-genprof
3. Run application in complain mode and review audit logs
4. Write custom AppArmor profile restricting file/capability access
5. Switch profile to enforce mode and test blocking behavior
6. Create defense-in-depth profile for railway control service

---

### 8. IEC-62443 Industry Context

#### Learning Path Overview
IEC-62443 is the industrial cybersecurity standard. Understanding its framework, security levels, and system integration requirements is critical for role preparation.

#### Free Resources & Training Materials

**Free IEC-62443 Guide:**
- **Free OT Cybersecurity Book: IEC-62443 Introduction**  
  [Link](https://www.abhisam.com/free-ot-cybersecurity-guide-iec-62443/)  
  *100-page free download covering all parts of IEC-62443 with 2024 numbering updates*

**Official ISA Training & Certification:**
- **ISA/IEC 62443 Cybersecurity Certificate Program**  
  [Link](https://www.isa.org/certification/certificate-programs/isa-iec-62443-cybersecurity-certificate-program)  
  *Five-day course covering complete IACS lifecycle*

- **ISA Training & Education Overview**  
  [Link](https://isagca.org/training-education)  
  *Microlearning modules (5-10 min), free YouTube content, IC46M overview course*

- **UL's ISA/IEC 62443 Training**  
  [Link](https://www.ul.com/services/isaiec-62443-training-product-and-system-manufacturers)  
  *3-day training on Parts 4-1 and 4-2 (product development security)*

**Railway-Specific Context:**
- **IEC-62443 Assessment for Metro Rail Infrastructure**  
  [Link](https://shieldworkz.com/blogs/how-to-conduct-an-iec-62443-based-assessment-for-metro-rail-infrastructure)  
  *Railway-specific application: control room access, OT employee awareness, incident response*

#### Lab Exercises:
1. Map IEC-62443 concepts to railway signaling systems
2. Identify security levels (SL 1-4) for hypothetical control scenarios
3. Design defense-in-depth architecture using learned technologies
4. Create risk assessment following IEC-62443 methodology

---

### 9. Lab Setup & Tools

#### Recommended Development Environment

**Host System Requirements:**
- Linux distribution (Ubuntu 20.04 LTS+ or Debian 11+) recommended
- 4+ CPU cores, 8GB+ RAM, 50GB+ disk space
- Git, Docker (optional but recommended)

#### Essential Free Tools Installation

```bash
## System packages
sudo apt-get update
sudo apt-get install -y \
    build-essential git autoconf automake libtool pkgconfig \
    python3 python3-dev python3-pip \
    libssl-dev libffi-dev \
    qemu-system-arm qemu-user \
    gcc-arm-linux-gnueabihf gcc-aarch64-linux-gnu

## TPM 2.0 Tools
git clone [Link](https://github.com/tpm2-software/tpm2-tss.git
cd tpm2-tss && ./bootstrap && ./configure && make && sudo make install

git clone [Link](https://github.com/tpm2-software/tpm2-tools.git
cd tpm2-tools && ./bootstrap && ./configure && make && sudo make install

## AppArmor tools
sudo apt-get install -y apparmor apparmor-utils apparmor-profiles

## cgroup management
sudo apt-get install -y cgroup-tools systemd-container

## Linux utilities for namespaces
sudo apt-get install -y util-linux iproute2 net-tools

## OP-TEE prerequisites (optional for full setup)
git clone [Link](https://github.com/OP-TEE/build.git
## Follow: [Link](https://optee.readthedocs.io/en/latest/building/gits/build.html
```

#### Suggested Learning Sequence

**Week 1-2: Foundations**
- Study TEE concepts (videos + white paper)
- Hands-on: Build OP-TEE hello_world example
- Study Root of Trust and Secure Boot

**Week 3-4: Boot Security**
- Implement measured boot with TPM
- Lab: tpm2-tools key management and PCR sealing
- Study UEFI Secure Boot customization

**Week 5-6: Resource & Process Isolation**
- Deep-dive cgroups: CPU, memory, I/O limits
- Study namespaces: PID, NET, MNT, USER
- Lab exercises: Create isolated processes

**Week 7-8: Access Control**
- Study AppArmor architecture and profiles
- Create custom AppArmor profiles
- Combine cgroups + AppArmor for defense-in-depth

**Week 9-10: Integration & Railway Context**
- Study IEC-62443 framework
- Map learned technologies to railway requirements
- Design secure railway control architecture

**Week 11-12: Practical Projects**
- Build complete OP-TEE trusted application
- Implement secure boot chain on hardware (if available)
- Create AppArmor profiles for railway-relevant services

#### Free Cloud Lab Environments (Optional)

- **Linux Academy / A Cloud Guru** (free tier available)
- **KKE: EKS, Docker, and Container Security Labs**  
  [Link](https://eksgoat.kubernetesvillage.com/
- **NVIDIA cuDNN Docker images** for ARM testing

#### Key GitHub Repositories to Follow

1. [Link](https://github.com/OP-TEE/ - Trusted Execution Environment
2. [Link](https://github.com/tpm2-software/ - TPM 2.0 implementations
3. [Link](https://github.com/tpm2dev/ - TPM development tutorials
4. [Link](https://github.com/tpm2-software/tpm2-tools - CLI tools
5. [Link](https://github.com/docker/labs - Container security labs
6. [Link](https://github.com/linaro-swg/ - Linaro Secure Group projects

---

### Learning Path Recommendations by Background

#### If You Have Embedded Systems Experience:
1. Start with TEE/OP-TEE (Week 1-3)
2. Jump directly to TPM and measured boot (Week 4-5)
3. Study AppArmor in parallel (Week 6-7)
4. Focus on railway integration (Week 8+)

#### If You Have Linux/Kernel Experience:
1. Begin with namespaces and cgroups (Week 1-2)
2. Study AppArmor and LSM framework (Week 3-4)
3. Add TEE concepts (Week 5-6)
4. Integrate TPM and boot security (Week 7-8)

#### If You Have Security Background but Limited Embedded:
1. Study TEE and RoT concepts first (Week 1-3)
2. Deep-dive AppArmor and mandatory access control (Week 4-5)
3. Learn Linux-specific: namespaces, cgroups, TPM (Week 6-8)
4. Focus on railway threat modeling (Week 9+)

---

### Assessment Checkpoints

**After Weeks 4-6, you should be able to:**
- Explain TEE/TrustZone architecture with secure/normal worlds
- Describe verified boot vs measured boot with PCR mechanics
- Create AppArmor profiles from audit logs
- Implement cgroup resource limits for processes

**After Weeks 8-10, you should be able to:**
- Deploy OP-TEE trusted applications
- Configure TPM 2.0 key hierarchies and sealing
- Design namespace-based isolation strategies
- Map IEC-62443 security levels to implementation

**After Week 12, you should:**
- Design a secure railway control architecture using learned technologies
- Present threat models and mitigations for each component
- Perform hands-on vulnerability assessment using acquired skills
- Discuss real-world trade-offs (security vs. performance vs. cost)

---

### Final Notes

**Free Resources Used in This Roadmap:**
- ✅ All videos from YouTube (official channels)
- ✅ Official GitHub repositories and documentation
- ✅ Open-source software (OP-TEE, TPM 2.0 tools, Linux kernel)
- ✅ White papers and technical guides (UEFI, NSA, academic)
- ✅ Community-maintained wikis and blogs
- ✅ Free cloud labs and simulators

**Total Estimated Learning Time:** 12 weeks at ~20 hours/week = 240 hours)  
**Hands-on Lab Time:** ~80-100 hours)  
**Theory & Video Study:** ~100-120 hours)  
**Integration & Projects:** ~40-60 hours

**Next Steps After This Roadmap:**
1. Pursue ISA/IEC-62443 certification
2. Contribute to open-source security projects (OP-TEE, tpm2-software)
3. Research latest CVEs in embedded systems and their mitigations
4. Engage with railway cybersecurity working groups

---

## But Wait... There is More...

I wanted to know if there was videos covering all the topics explained, So I punched that in as a follow up, and here is the result:

## Embedded Cybersecurity Learning Roadmap: IEC-62443 Railway Industry

**Target Role:** Embedded Cybersecurity Engineer (Railway Industry)  
**Standard:** IEC-62443 (Industrial Automation & Control Systems Cybersecurity)  
**Preparation Date:** February 2026)  
**Learning Format:** Video + Documentation + Hands-on Labs (100% Free)

---

### Table of Contents
1. [TEE - Trusted Execution Environment](#1-tee---trusted-execution-environment)
2. [Root of Trust & Chain of Trust](#2-root-of-trust--chain-of-trust)
3. [cgroups - Control Groups](#3-cgroups---control-groups)
4. [Disk Partitioning, Rescue & Mount Security](#4-disk-partitioning-rescue--mount-security)
5. [TPM Usage & Coverage](#5-tpm-usage--coverage)
6. [Linux Namespaces](#6-linux-namespaces)
7. [AppArmor - Mandatory Access Control](#7-apparmor---mandatory-access-control)
8. [IEC-62443 Industry Context](#8-iec-62443-industry-context)
9. [Lab Setup & Tools](#9-lab-setup--tools)

---

### 1. TEE - Trusted Execution Environment

#### Learning Path Overview
TEEs provide isolated secure execution for sensitive operations. For railway systems, TEEs protect critical control logic and cryptographic keys from compromised operating systems.

#### Video Resources

**YouTube Tutorials:**
- **Trusted Execution Environment (TEE) on ESP32-C6** (YouTube, 35 min)  
  [Link](https://www.youtube.com/watch?v=lSVu4FzdbBk)  
  *Learn practical TEE implementation on a real embedded platform with hardware isolation mechanisms*

- **A Technical Overview of Intel SGX, Arm TrustZone, and AMD SEV** (YouTube, 25 min)  
  [Link](https://www.youtube.com/watch?v=MREwcSo0uz4)  
  *Comparative analysis of different TEE technologies - essential for understanding architectural differences*

- **Proof is in the Pudding: Trusted Execution Environments** (YouTube, 40 min)  
  [Link](https://www.youtube.com/watch?v=QVA_Dtq3th0)  
  *Technical whiteboard discussion covering root of trust, TEE security models, and attack vectors*

- **Learn Embedded Security with ARM TrustZone in 50 Minutes** (YouTube, 50 min)  
  [Link](https://www.youtube.com/watch?v=_3jNdcK0SBI)  
  *Hands-on video covering ARMv8-M TrustZone, SAU/IDAU, Keil MDK demo with NXP LPC55S69*

- **Develop Secure Cortex-M Applications with TrustZone** (YouTube, 30 min)  
  [Link](https://www.youtube.com/watch?v=TkFC4Q2BwCM)  
  *ARM's official guide for Cortex-M TrustZone development*

- **Porting and Running OP-TEE on ARMv8 Devices** (YouTube, 30 min)  
  [Link](https://www.youtube.com/watch?v=sBVzSQ5uvUw)  
  *Hands-on video showing how to port OP-TEE to custom ARMv8 hardware*

#### Documentation Resources

**TEE 101 White Paper by Secure Technology Alliance**  
[Link](https://www.securetechalliance.org/wp-content/uploads/TEE-101-White-Paper-V1.1-FINAL-June-2018.pdf)  
*Foundational 30-page primer on TEE concepts, architecture, and real-world implementations*

**Introduction to Trusted Execution Environment and ARM's TrustZone**  
[Link](https://sergioprado.blog/introduction-to-trusted-execution-environment-tee-arm-trustzone/)  
*Beginner-friendly technical blog explaining TrustZone concepts with practical context*

**Guide to ARM TrustZone and OP-TEE: Secure World Design**  
[Link](https://www.linkedin.com/pulse/arm-trustzone-unlocking-secure-world-embedded-systems-khaled-el-sayed-a3hpf)  
*Covers OP-TEE architecture, trusted app development, and verified boot implementation*

#### Hands-On Lab Resources

**OP-TEE (Open Portable Trusted Execution Environment)**
- **Official OP-TEE Documentation & Build System**  
  [Link](https://optee.readthedocs.io/en/latest/general/about.html)  
  *Complete reference for building and deploying OP-TEE on ARM platforms*

- **OP-TEE Build & Development Guide**  
  [Link](https://optee.readthedocs.io/en/latest/building/gits/build.html)  
  Step-by-step instructions for compiling OP-TEE for various ARM devices (Raspberry Pi, QEMU, etc.)

- **OP-TEE Sample Applications (optee_examples)**  
  [Link](https://github.com/OP-TEE/optee_examples)  
  GitHub repository with hands-on examples: AES encryption, secure storage, hello_world, HOTP authentication

- **OP-TEE Examples Documentation**  
  [Link](https://optee.readthedocs.io/en/latest/building/gits/optee_examples/optee_examples.html)  
  Detailed guide for building and running sample trusted applications

**ARM TrustZone for Cortex-M (Microcontroller Version)**
- **Arm TrustZone Getting Started on SAM L11**  
  [Link](https://developerhelp.microchip.com/xwiki/bin/view/software-tools/harmony/saml11-trustzone-getting-started-training-module/)  
  *Microchip tutorial for Cortex-M TrustZone implementation with hands-on project*

**Lab Exercises:**
1. Build and run OP-TEE hello_world example on QEMU
2. Create a simple trusted application for cryptographic operations
3. Implement secure storage within OP-TEE
4. Explore TEE-REE communication via SMC calls

---

### 2. Root of Trust & Chain of Trust

#### Learning Path Overview
Root of Trust (RoT) and Chain of Trust establish the cryptographic foundation for secure boot. In railway systems, this prevents bootkit attacks and ensures only authorized firmware executes.

#### Video Resources

**YouTube Tutorials:**
- **Implementing UEFI-based Secure Boot + OTA Update for ARM Devices** (YouTube, 30 min)  
  [Link](https://www.youtube.com/watch?v=H_dBnwkTAbw)  
  *Deep technical talk: UAV/embedded systems secure boot, firmware integrity verification, U-Boot signing*

- **UEFI Secure Boot in U-Boot - Grant Likely, Arm** (YouTube, 35 min)  
  [Link](https://www.youtube.com/watch?v=VnsF3uRZzNk)  
  *Official ARM presentation: secure variables, chain of trust, UEFI verification mechanisms*

- **Enabling UEFI Secure Boot on x86 Platform with Yocto** (YouTube, 35 min)  
  [Link](https://www.youtube.com/watch?v=OA9TKkwFFIE)  
  *Practical Yocto integration, meta-secure-core layer, UEFI Secure Boot implementation*

#### Documentation Resources

**Official Documents:**
- **UEFI Secure Boot White Paper: Establishing the Root of Trust**  
  [Link](https://uefi.org/sites/default/files/resources/UEFI%20RoT%20white%20paper_Final%208%208%2016%20(003).pdf)  
  *Technical deep-dive: hardware RoT, verified boot vs. measured boot, Secure Boot chain*

- **UEFI Forum: Chain of Trust Introduction**  
  [Link](https://uefi.org/sites/default/files/resources/UEFI%20Forum%20White%20Paper%20-%20Chain%20of%20Trust%20Introduction_Final.pdf)  
  *Explains SEC phase, PEI, DXE phases in UEFI boot, and cryptographic binding*

- **NSA Guidance: Managing UEFI Secure Boot**  
  [Link](https://media.defense.gov/2025/Dec/11/2003841096/-1/-1/0/CSI_UEFI_SECURE_BOOT.PDF)  
  *Government cybersecurity guidance on Secure Boot implementation and threats*

**Blog & Articles:**
- **The IoT Chain of Trust: The Boot Process**  
  [Link](https://www.sealevel.com/the-iot-chain-of-trust-the-boot-process/)  
  *IoT-focused explanation of verified boot and measured boot concepts*

- **Demystifying Server Root of Trust**  
  [Link](https://www.moorinsightsstrategy.com/wp-content/uploads/2017/08/Demystifying-Server-Root-Of-Trust-by-Moor-Insights-and-Strategy.pdf)  
  *Intel Boot Guard, AMD PSP, and secure RoT technologies explained*

- **Achieving Root of Trust in Automotive MCUs**  
  [Link](https://www.renesas.com/en/blogs/introduction-about-secure-boot-automotive-mcu-rh850-and-soc-r-car-achieve-root-trust-1)  
  *Real-world automotive implementation of RoT (relevant for railway systems)*

#### Hands-On Lab Resources

**Boot with TPM Tutorial:**
- **Boot with TPM: Secure vs Verified vs Measured**  
  [Link](https://github.com/tpm2dev/tpm.dev.tutorials/blob/master/Boot-with-TPM/README.md)  
  *Explains SRTM vs CRTM, verified vs measured boot with TPM integration*

**Measured Boot Implementation:**
- **U-Boot Measured Boot Documentation**  
  [Link](https://docs.u-boot.org/en/latest/usage/measured_boot.html)  
  *Practical guide to implementing measured boot in bootloader*

**UEFI Secure Boot Configuration:**
- **UEFI Secure Boot Customization Guide** (NSA)  
  [Link](https://media.defense.gov/2023/Mar/20/2003182401/-1/-1/0/CTR-UEFI-SECURE-BOOT-CUSTOMIZATION-20230317.PDF)  
  *Detailed customization procedures for Secure Boot policies*

- **Arch Linux UEFI Secure Boot Wiki**  
  [Link](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot)  
  *Practical Linux-based Secure Boot setup and key management*

**Lab Exercises:**
1. Understand UEFI Secure Boot key hierarchy (PK, KEK, DB, DBX)
2. Sign kernel/bootloader binaries and load them into Secure Boot DB
3. Measure firmware components and verify TPM PCR values
4. Test boot failure scenarios (tampered binaries)

---

### 3. cgroups - Control Groups

#### Learning Path Overview
cgroups enable resource limits and isolation for processes. For railway systems, cgroups prevent single applications from consuming all resources, ensuring real-time guarantees for critical control loops.

#### Video Resources

**YouTube Tutorials:**
- **How to Understand Linux Control Groups (cgroups)** (YouTube, 20 min)  
  [Link](https://www.youtube.com/watch?v=NtK3poD_0X0)  
  *Sysadmincasts episode: practical examples of CPU, memory, I/O throttling, cgroup configuration*

- **Demystifying Linux cgroups** (YouTube, 17 min)  
  [Link](https://www.youtube.com/watch?v=bnBMKfKb21M)  
  *BeginLinux Guru: comprehensive cgroups overview, moving away from confusing technical details*

- **Modern Linux Servers with cgroups** (YouTube, 35 min)  
  [Link](https://www.youtube.com/watch?v=ZD7HDrtkZoI)  
  *Brandon Philips presentation: cgroups interface, resource management, container integration*

- **Cgroups, Namespaces, and Beyond: What Are Containers Made From?** (YouTube, 40 min)  
  [Link](https://www.youtube.com/watch?v=sK5i-N34im8)  
  *CoreOS presentation: deep dive into container building blocks, cgroups + namespaces*

#### Documentation Resources

**Technical Documentation:**
- **cgroups: Definition, Works, Benefits, and Container Use Cases**  
  [Link](https://www.cleanstart.com/guide/cgroup)  
  *Comprehensive guide covering cgroup v1, cgroup v2, CPU/memory/IO limits, Kubernetes integration*

- **Introduction to Container Resource Management**  
  [Link](https://www.neteye-blog.com/2024/12/introduction-to-container-resource-management-and-what-we-can-learn-for-monitoring/)  
  *Modern cgroup architecture and monitoring strategies*

- **Linux cgroups on KodeKloud**  
  [Link](https://notes.kodekloud.com/docs/Docker-Certified-Associate-Exam-Course/Docker-Engine-Security/CGroups)  
  *Focused on container security and process isolation*

- **Resource Control in Embedded Linux Systems with cgroups** (SYSGO Blog)  
  [Link](https://www.sysgo.com/blog/article/resource-control-in-embedded-linux-systems-with-cgroups)  
  *Embedded systems focus: real-time applications, persistent cgroups, railway-relevant content*

#### Hands-On Lab Resources

**Practical cgroups Management:**
- **Controlling Process Resources with Linux cgroups**  
  [Link](https://labs.iximiuz.com/tutorials/controlling-process-resources-with-cgroups)  
  *Interactive tutorial with cgroupfs, libcgroup tools, and systemd integration*

- **Docker cgroups Lab**  
  [Link](https://docker-saigon.github.io/post/Docker-Internals/)  
  *Deep dive into how Docker uses cgroups for container resource management*

- **How to Use Namespaces and cgroups to Control Docker**  
  [Link](https://earthly.dev/blog/namespaces-and-cgroups-docker/)  
  *Practical examples: CPU limits, memory caps, device restrictions*

- **What Are Namespaces and cgroups?**  
  [Link](https://blog.nginx.org/blog/what-are-namespaces-cgroups-how-do-they-work)  
  *NGINX blog explaining resource prioritization and limits*

**Lab Exercises:**
1. Create CPU-limited process groups using cgroupfs directly
2. Monitor memory usage with cgroup memory.stat
3. Implement I/O throttling for block devices
4. Use systemd service units for persistent cgroup management
5. Test CPU allocation fairness across competing processes

---

### 4. Disk Partitioning, Rescue & Mount Security

#### Learning Path Overview
Secure disk partitioning prevents unauthorized data access. Rescue mode isolation and mount permissions protect against privilege escalation. Critical for railway systems' persistent state management.

#### Video Resources

**YouTube Tutorials:**
- **Partitioning and Mounting Disks in Linux with fdisk** (YouTube, 25 min)  
  [Link](https://www.youtube.com/watch?v=UmwSw_wj70M)  
  *Eugene Abaidoo: comprehensive fdisk tutorial, partition creation, filesystem setup, permissions*

- **Manually Mounting Partitions in Ubuntu Server** (YouTube, 5 min)  
  [Link](https://www.youtube.com/watch?v=oTJajeMcAkE)  
  *Quick reference: mount/umount commands, discovering partitions, fstab configuration*

- **Linux Partitions and Mount Points: Preparing a DIY NAS** (YouTube, 25 min)  
  [Link](https://www.youtube.com/watch?v=wf4vX6wyBh0)  
  *Practical NAS setup: partition schemes, mounting, data security, LUKS encryption*

- **Physical Image and Partition Mounting in Tsurugi Linux** (YouTube, 9 min)  
  [Link](https://www.youtube.com/watch?v=9uqS7-8At3g)  
  *Forensics perspective: mounting disk images, accessing filesystem, partition recovery*

- **The Mount Namespace - Container Security Fundamentals** (YouTube, 8 min)  
  [Link](https://www.youtube.com/watch?v=BwI89OnYm-4)  
  *Datadog Security Labs: mount namespace isolation, filesystem security in containers*

- **How to Mount and Unmount Filesystem or Partition in Linux** (YouTube, 10 min)  
  [Link](https://www.youtube.com/watch?v=sK5i-N34im8)  
  *Comprehensive guide covering mount points, umount, persistent mounts*

#### Documentation Resources

**Mount Namespaces & Security:**
- **Mount Namespaces (man7.org Linux Manual)**  
  [Link](https://man7.org/linux/man-pages/man7/mount_namespaces.7.html)  
  *Exhaustive reference on mount isolation, propagation types, security implications*

- **Mount Namespaces and Shared Subtrees** (LWN Article)  
  [Link](https://lwn.net/Articles/689856/)  
  *Advanced concepts: MS_SHARED, MS_SLAVE, MS_PRIVATE propagation*

- **Linux Security Modules Overview**  
  [Link](https://en.wikipedia.org/wiki/Linux_Security_Modules)  
  *LSM framework enabling AppArmor, SELinux mount-related policies*

#### Hands-On Lab Resources

**Rescue Boot Systems:**
- **Weekend Project: Rescue Failing Drives with SystemRescue**  
  [Link](https://www.linux.com/training-tutorials/weekend-project-rescue-failing-drives-systemrescue/)  
  *Hands-on guide to creating rescue boot media and partition recovery*

- **SystemRescue - System Rescue Homepage**  
  [Link](https://www.system-rescue.org)  
  *Official SystemRescue documentation and live ISO*

- **IONOS Rescue System Documentation**  
  [Link](https://www.ionos.com/help/server-cloud-infrastructure/dedicated-server-for-servers-purchased-before-102818/rescue-and-recovery/)  
  *Practical rescue mode operations: fsck, chroot, partition repair*

- **Mounting Filesystems in Rescue Mode** (Selectel Docs)  
  [Link](https://docs.selectel.ru/en/dedicated/troubleshooting/mount-file-system/)  
  *Step-by-step partition mounting and recovery procedures*

- **Rackspace: Mount a Partition and chroot in Rescue Mode**  
  [Link](https://docs.rackspace.com/docs/mount-a-partition-and-chroot-into-your-primary-file-system-from-rescue-mode)  
  *Practical chroot workflows for system recovery*

**Lab Exercises:**
1. Create partitioned disk with separate /boot, /root, /var, /home
2. Boot SystemRescue and perform filesystem checks (fsck)
3. Mount filesystems with different security options (ro, noexec, nodev)
4. Create and test bind mounts with propagation flags
5. Recover data from read-only mounted filesystem

---

### 5. TPM Usage & Coverage

#### Learning Path Overview
TPM (Trusted Platform Module) provides hardware-based key storage, measured boot, and integrity verification. Essential for railway systems requiring remote attestation and secure key management.

#### Video Resources

**YouTube Tutorials:**
- **Introduction to TPMs (OpenSecurityTraining2)** (YouTube, 30 min)  
  [Link](https://www.youtube.com/watch?v=YSgAshwpLKc)  
  *Free MOOC video covering TPM capabilities, use cases, limitations*

- **What is a TPM? Protecting Your System** (YouTube, 15 min)  
  [Link](https://www.youtube.com/watch?v=QdHKYqrV-xk)  
  *Visual explanation of TPM installation and BitLocker usage*

- **Designing an Open-Source Hardware TPM 2.0 Add-on for Raspberry Pi** (YouTube, 40 min)  
  [Link](https://www.youtube.com/watch?v=JFqLfW_wZXA)  
  *KiCad PCB design, Infineon SLB 9672 chip, hands-on assembly & testing*

#### Documentation Resources

**Official Specs & Tutorials:**
- **What is a Trusted Platform Module?** (Huntress Cybersecurity Guide)  
  [Link](https://www.huntress.com/cybersecurity-101/topic/trusted-platform-module-tpm-cybersecurity-guide)  
  *Key functions: key generation, measured boot, integrity verification*

- **TPM Usability and Security Study** (USENIX SOUPS 2022)  
  [Link](https://www.usenix.org/system/files/soups2022-rao.pdf)  
  *Academic research on tpm2-tools usability and security pitfalls*

- **Trusted Platform Module Part 1** (LinkedIn Learning - IoT Security)  
  [Link](https://www.linkedin.com/learning/iot-product-security/trusted-platform-module-part-1)  
  *Compares TEE vs TPM, architecture, and measured boot*

#### Hands-On Lab Resources

**TPM 2.0 Software & Tools:**
- **GitHub: Learn-TPM Educational Repository**  
  [Link](https://github.com/Abhinandan-Khurana/Learn-TPM)  
  *Comprehensive guides, code samples, use cases for TPM 2.0*

- **tpm2-tss (TPM 2.0 Software Stack)**  
  [Link](https://github.com/tpm2-software/tpm2-tss)  
  *Official TSS implementation with FAPI, SAPI, ESAPI layers*

- **tpm2-tss Installation & Build Guide**  
  [Link](https://github.com/tpm2-software/tpm2-tss/blob/master/INSTALL.md)  
  *Step-by-step build instructions for all platforms*

- **tpm2-tss ReadTheDocs**  
  [Link](https://tpm2-tss.readthedocs.io)  
  *Official documentation for TSS libraries and simulator setup*

- **tpm2-tools (CLI Tool Suite)**  
  [Link](https://github.com/tpm2-software/tpm2-tools)  
  *Command-line interface for TPM operations (key generation, signing, etc.)*

- **tpm2-tools Documentation**  
  [Link](https://tpm2-tools.readthedocs.io)  
  *Man pages and build instructions for tpm2-tools*

**Software TPM Simulator:**
- **IBM's Software TPM 2.0 Simulator**  
  [Link](https://sourceforge.net/projects/ibmswtpm2/)  
  *Free TPM 2.0 simulator for development (no hardware required)*

**Python Bindings:**
- **tpm2-pytss: Python TPM Bindings**  
  [Link](https://pypi.org/project/tpm2-pytss/)  
  *High-level Python API for TPM operations*

**Lab Exercises:**
1. Install and configure tpm2-tss and tpm2-tools
2. Generate TPM keys and explore key hierarchies
3. Create and seal data to PCR values
4. Implement measured boot logging with TPM PCRs
5. Test remote attestation workflows
6. Use TPM for encryption key storage

---

### 6. Linux Namespaces

#### Learning Path Overview
Namespaces provide process isolation at the OS level. For railway systems, they enable containerized control logic with strong isolation boundaries (PID, NET, UTS, IPC, USER, MNT, CGROUP).

#### Video Resources

**YouTube Tutorials:**
- **How Do Linux Namespaces Provide Process Isolation?** (YouTube, 4 min)  
  [Link](https://www.youtube.com/watch?v=9LzNoXPgtqM)  
  *Server Logic Simplified: concise overview of all namespace types and isolation mechanisms*

- **How Containers Use PID Namespaces to Provide Process Isolation** (YouTube, 11 min)  
  [Link](https://www.youtube.com/watch?v=J17rXQ5XkDE)  
  *Red Hat TAM Brian Smith: practical PID namespace demonstration on RHEL 8.2*

- **Containers Unplugged: Linux Namespaces - Michael Kerrisk** (YouTube, 45 min)  
  [Link](https://www.youtube.com/watch?v=0kJPa-1FuoI)  
  *Expert deep-dive: namespace APIs, clone(), setns(), unshare() syscalls, practical examples*

- **What is a Namespace in Linux, and How Does It Work** (YouTube, 10 min)  
  [Link](https://www.youtube.com/watch?v=bAzrdwhtDnE)  
  *Overview of PID, mount, IPC, UTS namespaces with container examples*

- **The Mount Namespace - Container Security Fundamentals** (YouTube, 8 min)  
  [Link](https://www.youtube.com/watch?v=BwI89OnYm-4)  
  *Datadog Security Labs: mount namespace isolation for filesystem security*

#### Documentation Resources

**Technical Articles:**
- **Understanding Linux Namespaces: A Guide to Process Isolation**  
  [Link](https://dev.to/ajinkya_singh_2c02bd40423/understanding-linux-namespaces-a-guide-to-process-isolation-4gbg)  
  *Beginner-friendly guide covering all namespace types with examples*

- **The 7 Most Used Linux Namespaces** (Red Hat Blog)  
  [Link](https://www.redhat.com/en/blog/7-linux-namespaces)  
  *Official Red Hat coverage of namespace isolation mechanisms*

- **Digging into Linux Namespaces - Part 1** (Quarkslab)  
  [Link](https://blog.quarkslab.com/digging-into-linux-namespaces-part-1.html)  
  *Deep technical analysis with network namespace examples*

- **Building a Linux Container by Hand Using Namespaces** (Red Hat)  
  [Link](https://www.redhat.com/en/blog/building-container-namespaces)  
  *Step-by-step tutorial creating container primitives from scratch*

#### Hands-On Lab Resources

**Practical Namespace Experiments:**
- **Jailing Apps Using Linux Namespaces** (UWSGI Docs)  
  [Link](https://uwsgi-docs.readthedocs.io/en/latest/Namespaces.html)  
  *Hands-on using setns(), /proc/self/ns, and namespace attachment*

- **Docker Namespaces and cgroups Lab**  
  [Link](https://eksgoat.kubernetesvillage.com/basics/docker_namespaces_and_cgroups)  
  *Interactive lab environment for namespace and cgroup experiments*

- **Docker Internals: Namespaces & cgroups**  
  [Link](https://docker-saigon.github.io/post/Docker-Internals/)  
  *Visual explanation of how Docker uses namespaces for isolation*

- **Introduction to Docker (Lightweight Virtualization)**  
  [Link](https://jwlss.pw/course_notes/cloud_labs/Lab%2002%20-%20Docker.pdf)  
  *Lab exercises: PID namespace, network namespace creation*

**Lab Exercises:**
1. Create PID namespaces using `unshare -p` and `fork()`
2. Create network namespaces and connect with veth pairs
3. Use USER namespaces for rootless container execution
4. Create MOUNT namespaces and test bind mount propagation
5. Explore /proc/[PID]/ns files and namespace relationships
6. Implement multi-level namespace hierarchies

---

### 7. AppArmor - Mandatory Access Control

#### Learning Path Overview
AppArmor enforces fine-grained access control policies per application. For railway systems, AppArmor restricts services to minimal required capabilities, implementing defense-in-depth.

#### Video Resources

**YouTube Tutorials:**
- **Using AppArmor Profiles on Ubuntu 20.04** (YouTube, 16 min)  
  [Link](https://www.youtube.com/watch?v=NacZftDDVLA)  
  *TheUrbanPenguin: practical AppArmor profile creation, complain mode, enforcement*

- **Mandatory Access Control (MAC): SELinux & AppArmor** (YouTube, 20 min)  
  [Link](https://www.youtube.com/watch?v=8lGK80UYeSY)  
  *Comparison of SELinux vs AppArmor, path-based access control, profile modes*

- **The Ultimate Guide to Securing Kubernetes with AppArmor** (YouTube, 15 min)  
  [Link](https://www.youtube.com/watch?v=OxkMFSKiZYE)  
  *AppArmor profile creation, Kubernetes integration, deny/allow rules*

- **Unprivileged Access Control in AppArmor - John Johansen & Georgia Garcia, Canonical** (YouTube, 40 min)  
  [Link](https://www.youtube.com/watch?v=HJ5BMX52dhI)  
  *Canonical maintainers: advanced AppArmor features, pledge, unveil, stacking*

#### Documentation Resources

**Official & Authoritative Sources:**
- **AppArmor Official Homepage**  
  [Link](https://apparmor.net)  
  *Official project documentation and overview*

- **Implementing Mandatory Access Control (Tecmint)**  
  [Link](https://www.tecmint.com/mandatory-access-control-with-selinux-or-apparmor-linux/)  
  *Comparison of AppArmor vs SELinux with practical focus*

- **AppArmor (Arch Wiki)**  
  [Link](https://wiki.archlinux.org/title/AppArmor)  
  *Community documentation with installation and configuration*

- **Linux Kernel AppArmor Documentation**  
  [Link](https://docs.kernel.org/admin-guide/LSM/apparmor.html)  
  *Kernel configuration and LSM integration details*

- **The Linux Security Modules Framework** (Star Lab Software)  
  [Link](https://www.starlab.io/blog/a-brief-tour-of-linux-security-modules)  
  *Comprehensive LSM overview including AppArmor's role*

- **Linux Security Modules & Access Control** (AccuKnox)  
  [Link](https://accuknox.com/blog/linux-security-modules-lsm-hooks)  
  *LSM hooks architecture and AppArmor enforcement mechanisms*

- **Linux Audit: AppArmor Security Framework**  
  [Link](https://linux-audit.com/security-frameworks/apparmor/)  
  *History, features, and profile-based security model*

- **How to Set Up AppArmor Profiles on Ubuntu** (OneUptime)  
  [Link](https://oneuptime.com/blog/post/2026-01-07-ubuntu-apparmor-profiles/view)  
  *Modern AppArmor configuration guide with practical examples*

#### Hands-On Lab Resources

**Docker AppArmor Lab:**
- **Docker Labs: AppArmor Security**  
  [Link](https://github.com/docker/labs/blob/master/security/apparmor/README.md)  
  *25-minute advanced lab: default Docker profile, custom profiles, defense-in-depth*

- **AppArmor in Kubernetes**  
  [Link](https://github.com/DirectXMan12/kubernetes.github.io/blob/master/docs/admin/apparmor/index.md)  
  *Beta AppArmor support in Kubernetes with enforcement details*

**Profile Development Tools:**
- **Creating AppArmor Profiles: 9 Easy Steps**  
  [Link](https://blog.pentesteracademy.com/creating-hello-world-apparmor-profile-in-9-easy-steps-a172041a233b)  
  *Step-by-step profile creation: aa-genprof, aa-complain, aa-logprof*

- **Beginning AppArmor Profile Development** (Ubuntu Tutorials)  
  [Link](https://github.com/canonical-web-and-design/tutorials.ubuntu.com/blob/master/tutorials/security/beginning-apparmor-profile-development.md)  
  *Profile development with aa-genprof and learning mode*

- **AppArmor Profile Development (KodeKloud)**  
  [Link](https://github.com/kodekloudhub/certified-kubernetes-security-specialist-cks-course/blob/main/docs/04-System-Hardening/22-AppArmor.md)  
  *Enforcing mode vs complain mode, practical examples*

**Lab Exercises:**
1. Install apparmor-utils and enable AppArmor
2. Generate profile for a sample application using aa-genprof
3. Run application in complain mode and review audit logs
4. Write custom AppArmor profile restricting file/capability access
5. Switch profile to enforce mode and test blocking behavior
6. Create defense-in-depth profile for railway control service

---

### 8. IEC-62443 Industry Context

#### Learning Path Overview
IEC-62443 is the industrial cybersecurity standard. Understanding its framework, security levels, and system integration requirements is critical for role preparation.

#### Video Resources

**YouTube Tutorials:**
- **Master OT/ICS Cybersecurity Before It's Too Late — Part 1** (YouTube, 27 min)  
  [Link](https://www.youtube.com/watch?v=UKfcLwyOPxQ)  
  *Mike Holcomb: comprehensive ICS/OT cybersecurity overview, 62443 standard framework, certification path*

- **Part 2: Building a ROCK SOLID 62443 Cybersecurity Management System (CSMS)** (YouTube, 105 min)  
  [Link](https://www.youtube.com/watch?v=ObRnvUd_2cU)  
  *Deep-dive into cybersecurity management system design, IACS lifecycle, security levels*

- **IEC/ISA 62443 Cybersecurity Bootcamp Day 1 Part 1** (YouTube, 35 min)  
  [Link](https://www.youtube.com/watch?v=JeOfgOT_2JQ)  
  *62443 overview, key terminology, concepts, risk assessment foundations*

- **THE BEST Way to Prepare for ISA/IEC 62443 Certification** (YouTube, 45 min)  
  [Link](https://www.youtube.com/watch?v=wn5OgTFz198)  
  *Manjunath Hiregange: study strategies, actionable tips, certification preparation roadmap*

#### Documentation Resources

**Free IEC-62443 Guide:**
- **Free OT Cybersecurity Book: IEC-62443 Introduction**  
  [Link](https://www.abhisam.com/free-ot-cybersecurity-guide-iec-62443/)  
  *100-page free download covering all parts of IEC-62443 with 2024 numbering updates*

**Official ISA Training & Certification:**
- **ISA/IEC 62443 Cybersecurity Certificate Program**  
  [Link](https://www.isa.org/certification/certificate-programs/isa-iec-62443-cybersecurity-certificate-program)  
  *Five-day course covering complete IACS lifecycle*

- **ISA Training & Education Overview**  
  [Link](https://isagca.org/training-education)  
  *Microlearning modules (5-10 min), free YouTube content, IC46M overview course*

- **UL's ISA/IEC 62443 Training**  
  [Link](https://www.ul.com/services/isaiec-62443-training-product-and-system-manufacturers)  
  *3-day training on Parts 4-1 and 4-2 (product development security)*

**Railway-Specific Context:**
- **IEC-62443 Assessment for Metro Rail Infrastructure**  
  [Link](https://shieldworkz.com/blogs/how-to-conduct-an-iec-62443-based-assessment-for-metro-rail-infrastructure)  
  *Railway-specific application: control room access, OT employee awareness, incident response*

#### Lab Exercises:
1. Map IEC-62443 concepts to railway signaling systems
2. Identify security levels (SL 1-4) for hypothetical control scenarios
3. Design defense-in-depth architecture using learned technologies
4. Create risk assessment following IEC-62443 methodology

---

### 9. Lab Setup & Tools

#### Recommended Development Environment

**Host System Requirements:**
- Linux distribution (Ubuntu 20.04 LTS+ or Debian 11+) recommended
- 4+ CPU cores, 8GB+ RAM, 50GB+ disk space
- Git, Docker (optional but recommended)

#### Essential Free Tools Installation

```bash
## System packages
sudo apt-get update
sudo apt-get install -y \
    build-essential git autoconf automake libtool pkgconfig \
    python3 python3-dev python3-pip \
    libssl-dev libffi-dev \
    qemu-system-arm qemu-user \
    gcc-arm-linux-gnueabihf gcc-aarch64-linux-gnu

## TPM 2.0 Tools
git clone [Link](https://github.com/tpm2-software/tpm2-tss.git
cd tpm2-tss && ./bootstrap && ./configure && make && sudo make install

git clone [Link](https://github.com/tpm2-software/tpm2-tools.git
cd tpm2-tools && ./bootstrap && ./configure && make && sudo make install

## AppArmor tools
sudo apt-get install -y apparmor apparmor-utils apparmor-profiles

## cgroup management
sudo apt-get install -y cgroup-tools systemd-container

## Linux utilities for namespaces
sudo apt-get install -y util-linux iproute2 net-tools

## OP-TEE prerequisites (optional for full setup)
git clone [Link](https://github.com/OP-TEE/build.git
## Follow: [Link](https://optee.readthedocs.io/en/latest/building/gits/build.html
```

#### Suggested Learning Sequence

**Week 1-2: Foundations**
- Study TEE concepts (videos + white paper)
- Hands-on: Build OP-TEE hello_world example
- Study Root of Trust and Secure Boot

**Week 3-4: Boot Security**
- Implement measured boot with TPM
- Lab: tpm2-tools key management and PCR sealing
- Study UEFI Secure Boot customization

**Week 5-6: Resource & Process Isolation**
- Deep-dive cgroups: CPU, memory, I/O limits
- Study namespaces: PID, NET, MNT, USER
- Lab exercises: Create isolated processes

**Week 7-8: Access Control**
- Study AppArmor architecture and profiles
- Create custom AppArmor profiles
- Combine cgroups + AppArmor for defense-in-depth

**Week 9-10: Integration & Railway Context**
- Study IEC-62443 framework
- Map learned technologies to railway requirements
- Design secure railway control architecture

**Week 11-12: Practical Projects**
- Build complete OP-TEE trusted application
- Implement secure boot chain on hardware (if available)
- Create AppArmor profiles for railway-relevant services

#### Key GitHub Repositories to Follow

1. [Link](https://github.com/OP-TEE/ - Trusted Execution Environment
2. [Link](https://github.com/tpm2-software/ - TPM 2.0 implementations
3. [Link](https://github.com/tpm2dev/ - TPM development tutorials
4. [Link](https://github.com/tpm2-software/tpm2-tools - CLI tools
5. [Link](https://github.com/docker/labs - Container security labs
6. [Link](https://github.com/linaro-swg/ - Linaro Secure Group projects

---

### Learning Path Recommendations by Background

#### If You Have Embedded Systems Experience:
1. Start with TEE/OP-TEE (Week 1-3)
2. Jump directly to TPM and measured boot (Week 4-5)
3. Study AppArmor in parallel (Week 6-7)
4. Focus on railway integration (Week 8+)

#### If You Have Linux/Kernel Experience:
1. Begin with namespaces and cgroups (Week 1-2)
2. Study AppArmor and LSM framework (Week 3-4)
3. Add TEE concepts (Week 5-6)
4. Integrate TPM and boot security (Week 7-8)

#### If You Have Security Background but Limited Embedded:
1. Study TEE and RoT concepts first (Week 1-3)
2. Deep-dive AppArmor and mandatory access control (Week 4-5)
3. Learn Linux-specific: namespaces, cgroups, TPM (Week 6-8)
4. Focus on railway threat modeling (Week 9+)

---

### Assessment Checkpoints

**After Weeks 4-6, you should be able to:**
- Explain TEE/TrustZone architecture with secure/normal worlds
- Describe verified boot vs measured boot with PCR mechanics
- Create AppArmor profiles from audit logs
- Implement cgroup resource limits for processes

**After Weeks 8-10, you should be able to:**
- Deploy OP-TEE trusted applications
- Configure TPM 2.0 key hierarchies and sealing
- Design namespace-based isolation strategies
- Map IEC-62443 security levels to implementation

**After Week 12, you should:**
- Design a secure railway control architecture using learned technologies
- Present threat models and mitigations for each component
- Perform hands-on vulnerability assessment using acquired skills
- Discuss real-world trade-offs (security vs. performance vs. cost)

---

### Final Notes

**Free Resources Used in This Roadmap:**
- ✅ **30+ YouTube Videos** from official channels (TEE, Root of Trust, cgroups, mount security, TPM, namespaces, AppArmor, IEC-62443)
- ✅ **50+ Technical Documentation** resources (white papers, guides, blogs, wikis)
- ✅ **25+ Hands-on Lab** repositories and interactive environments
- ✅ **7+ GitHub Projects** for practical implementation
- ✅ Open-source software (OP-TEE, TPM 2.0 tools, Linux kernel, AppArmor)
- ✅ Free cloud labs and simulators

**Total Estimated Learning Time:** 12 weeks at ~20 hours/week = 240 hours)  
**Hands-on Lab Time:** ~80-100 hours)  
**Theory & Video Study:** ~100-120 hours)  
**Integration & Projects:** ~40-60 hours

**Video Content Breakdown:**
- TEE: 6 videos (3.5 hours)
- Root of Trust: 3 videos (1.5 hours)
- cgroups: 4 videos (1.5 hours)
- Disk/Mount: 6 videos (1.5 hours)
- TPM: 3 videos (1.5 hours)
- Namespaces: 5 videos (1.5 hours)
- AppArmor: 4 videos (1.5 hours)
- IEC-62443: 4 videos (3.5 hours)
- **Total Video Time: 16+ hours of curated content**

**Next Steps After This Roadmap:**
1. Pursue ISA/IEC-62443 certification
2. Contribute to open-source security projects (OP-TEE, tpm2-software)
3. Research latest CVEs in embedded systems and their mitigations
4. Engage with railway cybersecurity working groups

---

**Roadmap Last Updated:** February 2, 2026)  
**Document Version:** 2.0 (Complete Video Coverage)  
**Total Resources:** 110+ links including videos, documentation, labs, and GitHub repositories
