Pharmacy counting program: from an input file containing drug name, cost, and prescriber data, an output file is written with the unique number of prescribers and total cost of the drug, sorted in descending order by the total cost of each drug. For drugs with similar cost, the drug name is listed in ascending order. Submitted for the Insight Data Engineering Coding Challenge.

Approach: The input file containing data on drug name, prescriber, and cost on each line is read using the standard csv module. The names of each drug is stored in a dictionary. From the data in each line, if the drug does not exist in the dictionary, then the entry is created, with an initial number of unique prescribers as "1" and a cost equal to the cost in the line. If the drug already exists in the dictionary, the number of prescribers is increased if the prescriber is unique, and the cost of the drug from the line is added to the total cost of the drug. When the input file is finished reading, the data is sorted by drug name and cost before being written to the output file.
