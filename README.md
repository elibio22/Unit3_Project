# Unit3_Project
Assignment for Unit 3 - Introduction to Programming 

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * How to test
 * How to run
 * Maintainers

INTRODUCTION
------------

The aim of the project is to create a functional API based on the user story.
User story can be found in the project page:

The project scope is to help scientists which use lentivirus vectors for knocking down (KD) specific genes. 
The lentivirus vectors present a short sequence of nucleotides (shRNA), which is an artificial RNA molecule w that can be used to silence target gene expression via RNA interference. Gene KD is generally expressed via qPCR.
Finding the position of the shRNA into a  specific gene transcript sequence might help on improving the design of the primers for the qPCR and better evaluate the efficiency of the KD.



 * For a full description of the module, visit the project page:
   https://github.com/elibio22/Unit3_Project

 * To submit bug reports and feature suggestions, or track changes:
   https://github.com/elibio22/Unit3_Project/issues

REQUIREMENTS
------------

This module requires the following modules:

* flask
* sqlite3

INSTALLATION
------------
 
Download the database at this link and unzip the file:
* https://drive.google.com/file/d/1MfyHfumX--ZypB1K2hF5v5IIFE-1GHcZ/view?usp=sharing
 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

HOW TO TEST
---------------

```
python3 -m unittest test_api
```


HOW TO RUN
---------------

```
python3 api.py
```

Now that the server is running, you can call the route `GET /transcript/<transcript_id>/<sh_rna>` on localhost.

For example: 

* http://127.0.0.1:5000/transcript/ENST00000373425.8/TTCATTTACCTAAACAGG


MAINTAINERS
-----------

Current maintainers:
 * Elisabetta Bottaro - https://github.com/elibio22

## User story:
Elisabetta is a scientist who works in a bioengineering lab. Recently she was trying to work on Knocking - down(KD)some genes for evaluating new targets for drug therapies. The KD was carried out using a lentivirus vector (shRNA). After experimenting, two approaches have been applied for evaluating the efficiency of the KD, such as GFP expression and qPCR (relative gene expression). GFP expression in the cells transduced showed an efficient KD (higher than 70%). However, the relative gene expression showed a lower % of KD (40%), resulting in disagreement with the GFP expression result.
Therefore, improvements for the qPCR measurement method were needed to confirm the KD. 
After some literature review, some scientific articles were suggesting that the primers utilised for the qPCR should flank the shRNA sequence to improve the accuracy of the results. To design the new primers Elisabetta needed to find the position of the shRNA onto the specific transcript gene-targeted (scope 1).
In this example, the gene target is ANGPTL2. 
Afterwards, Elisabetta need to design the new primers following the standard rules (scope 2), such as:
1. Length of 18-24 bases
2. G/C content = 40%-60% ---What is GC Content? GC content is usually calculated as a percentage value and is sometimes
called G+C ratio or GC-ratio. GC-content percentage is calculated as Count(G + C)/Count(A + T + G + C) * 100%.
3. Start and end with 1-2 G/C pairs
4. Melting temperature (Tm) of 50-60°C --calculate 4°C*(# G/C nucleotides) + 2°C*(# A/T nucleotides
5. Primer pairs should have a Tm within 5°C of each other
6. Primer pairs should not have complementary regions (not addressed in this code)

## Disclaimer:
Elisabetta idea was to try to take this coding challenge as an example for her final project.
Elisabetta is completely aware that this code is just a simplification of the process to generate primers and might be not accurate. The code has been written with the only scope to be used as exercise coding and not for the real use of generating primers.
Indeed, the best method for generating primers can be found in the following link: 
https://www.ncbi.nlm.nih.gov/tools/primer-blast/primertool.cgi?ctg_time=1645310287&job_key=n5VAAR5GE-400BbVG7Uy52GuI9VMvTjITQ


