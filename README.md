Pharmacy counting program: from a file containing drug name, cost, and prescriber data, information is given on unique prescribers and total drug cost in descending order. For similar cost, the drug name is listed in ascending order. Submitted for the Insight Data Engineering coding challenge.

Approach: The input file containing data on drug name, prescriber, and cost on each line is read using the standard csv module. After each line, a growing dictionary is created with drug name and the associated cost and number of prescribers is updated based on whether the prescriber's name was read from a previous line. 

