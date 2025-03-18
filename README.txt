# README
Introduction : 1. To make it easier to understand, please open folder \example\pic
               2. How to use FUKG is at the bottom of this page

# ARCHITECTURE 
FUKG best practice : ready-to-use files for each subclass of fukg methodology results
FUKG Methodologies : all the files needed to keep the dataset structured and connected
example : example of use

# FUKG BEST PRACTICES 

To support the effectiveness and efficiency of the implementation of FUKG methodologies, several best practices are applied:
1. Folder Structure:

In FUKG Best practice, each subclass modeled on the set-model graph will be the name of the folder that will store the main 
component files and the files are also taken from the set-model graph methodology, set-table csv and set-interpreter. 
The main components in each folder include
• Model Graph.png: Image file (PNG) that explains the structure of the knowledge graph for each subclass.
• subclassName_attribute.csv: Is a CSV file with the category set-table mapping university attribute data. 
  This file stores entity and attribute data for the subclass, for example, mahasiswa_attribute.csv. There is only one table 
  of this type for each subclass folder.
• subclassNamePropertyValidator.py: Is a python file to validate data in the set-table mapping university attribute data table.
• mapping_subclassName.ttl : This is a file containing RML[9] syntax for the university attribute data mapping set-table file 
  to RDF form, in this study it is also called the university attribute data mapping interpreter.
• Rx_subclass_RelationName.csv: This is a csv file with the category of university relation data mapping set-table, 
  for example R1_Mahasiswa_mengambil.csv. The requirement for data entered in this type of table is that the data 
  already exists in the subclassName_attribute.csv table of each subclass. This CSV is an implementation of the set-table 
  method and the data comes from university data collection. The number of CSV files is in accordance with the number of 
  relations in the Set-Model Graph.
• Rx_Validator.py: This is a file containing python syntax. This file will check whether the data entered in the university 
  relation data mapping set-table already exists in the university attribute data mapping set-table table. The number of 
  these files is in accordance with the number of university relation data mapping set-table tables.
• mapping_RX.ttl: Is a Turtle (TTL) file that defines attribute mapping from the university relation data mapping set-table file 
  to RDF format using RML[9], in this study also called the university relation data mapping interpreter. 
  for example, mapping_R1.ttl, mapping_R2.ttl, mapping_R3.ttl. In the subclass folder, the number of these files is uncertain 
  and according to the number of relations from the subclass or according to the number of relations defined in the subclass 
  relation schema set-table to another subclass.
• queryProperty.sparql: Is a file with the category of university attribute data mapping queries with the purpose of use as 
  explained in SPARQL query.
• queryRx.sparql: Is a file with the category of university relation data mapping queries with the purpose of use as explained 
  in SPARQL query.

2. Integration and Execution Process of FUKG Best Practices:

The integration and execution process includes several important stages:
• Data integration: Which can be executed simply by selecting the required subclass folder, for example students, lecturers, 
  and alumni. The data integration process is carried out on the set-table with the category of university attribute data 
  mapping set-table and university relation data mapping set-table.

• Data validation: Data is validated using the subclassNamePropertyValidator.py and Rx_validator.py files before being 
  converted to RDF form.

• Transformation to RDF: When the dataset is validated, the data from the university attribute data mapping set-table and 
  the university relation data mapping set-table are ready to be mapped using the university attribute data mapping interpreter and the university relation data mapping interpreter.
• SPARQL query: The user runs the university attribute data mapping sparql query and the university relation data mapping sparql query.

# FUKG METHODOLOGIES

To build formal rules of graph model on university RDF data, we propose set-model graph. To produce accurate, consistent and 
complete data conversion we propose CSV set-table and set-interpreter which contains wikidata items that are appropriate to 
university context.

1. Set-Model Graph
It is a visualization of node and edge graph of university data that focuses on subclass. 
Set-model graph consists of visualization of mainclass, subclass and its attributes and also visualization of subclass relation 
to other subclass. This visualization supports how university data has consistent type and accurate data according to subclass 
and its relation, and becomes reference of completeness of RDF data when stored in jena fuseki. Set-Model Graph involves three 
main processes, namely University Fact Finding to collect verifiable university facts, Wikidata Item Existence Check to issue 
and verify the truth of wikidata reference items involving entity position in university context; finally, we run comparison 
between data taken from both sources. This produces a graph structure image showing nodes (classes and subclasses) and edges, 
which are links that represent relationships between entities and their attributes.

2. Set-Table CSV

This is a method of storing data for each subclass that will be mapped using the set-interpreter. We use the term set-table to 
separate each category of data stored. Consists of:
• main class set-table to store a list of data that will be the main class type of the subclass. Main class set-table, 
  contains 1 column with the number of rows adjusting to the needs of the main class in the knowledge graph.

   Table 1. Example of main class Set-Table
   Class
   Mainclass1
   Mainclass2
   Mainclass3

• Main class set-table to subclass to store a list of subclass data in each main class that will be a data type named subclass 
  so that each row of university data has one subclass type. The main class set-table to subclass contains 2 columns, namely the subclass name and the wikidata item that is the reference for the subclass with the number of rows based on the total subclass modeled in the set-model graph.

   Table 2. Set-Table class Mainclass1
   Subclass_Mainclass1 wikidataItem
   Subclass1 QID
   Subclass2 QID

• Set-table subclass property, consists of set-table subclass property FUKG, we collect the names of each attribute from the subclass 
  graph model, this set-table is to store all attribute data collected and given a code or PID such as P1, P2, P3 etc. to facilitate 
  data access. Set-table subclass property FUKG contains 5 columns, namely PID, labelID, descriptionID, labelEn and descriptionEn. 
  The number of rows in this set-table adjusts to the total properties of each subclass that has been modeled in the set-model graph. 
  PID is a code given by FUKG such as P1, P2, P3 with labeling and description using Indonesian and English. Next, there is a 
  Set-table of FUKG subclass properties to wikidata to store attribute data that is also found in wikidata and is relevant to the 
  FUKG subclass attributes, this is to see how the depth of FUKG and wikidata information differs for the university context. 
  The Set-table of FUKG subclass properties to wikidata contains 2 columns, namely the PID column and the QID column of the 
  wikidata item. • Set-table of subclass relation schemes to other subclasses, consisting of 4 columns, namely   the domain subclass 
  column, the range subclass column, the relation code column and the relation code description column. If the graph model consists 
  of 29 subclasses, it means that there are 29 domain subclasses, which then have relations with other subclasses. For example, the 
  student subclass has relations with the subclasses of courses, study programs and student organizations. This means that this 
  set-table consists of Set-table R1 for relations between students and courses where the R1 label is taking, R2 for relations 
  between students and study programs where the R2 label is registered in and R3 for relations between students and student 
  organizations where the R3 label is member of. 

    Table 3. Subclass relation schema Student

    Relation ID Domain Range
    R1 takes a course Student Course
    R2 is registered in a study program Student Study program
    R3 is a member of a student organization Student Student Organization

    Table 4. Subclass relation schema Article
    Relation ID Domain Range
    R45 is in Journal Article
    R46 is used by Lecturer Article
    R47 is used by Student Article

• University attribute data mapping set-table.
    Table 5. Example of university attribute data mapping set-table for student subclass with 3 attributes
    student name nim level
    MuhImamAsyhari D082231010 S2
    Data2 Data2 Data2
    Data3 Data3 Data3

  This category consists of 29 set-tables. Each set-table will store university data and its attributes. For example, 
  a student set-table and its attributes. The university attribute data mapping set-table contains columns that refer to 
  attributes that have been visualized in the set-model graph of each subclass. Figure 1 is a set-model graph for the student 
  or university student subclass. Consists of 8 attributes, so the number of columns in this set-table is 8 columns. If there are 
  29 subclasses in the subclass definition table-set, it means that the number of set-tables for this category is 29 csv set-tables.
• Set-table mapping of university relation data,
   Table 6. Example of set-table mapping of university relation data code R1 for student subclass
   nim Course Code
   D082231010 MK102

  This category is a continuation of the set-table of subclass relation scheme to another subclass, if the set-table stores 
  the definition of the relation code, this set-table is for storing university data that has a relationship with another subclass. 
  for example there is a fact, there is data from the student subclass, namely D082231010 taking the MK102 course which is the data 
  of the course subclass. then from this fact, D082231010 will enter the domain column and MK102 will enter the range column.

3. Set-Interpreter

Set-Interpreter is part of FUKG methodologies to translate each set-model graph using RML[9] syntax and to connect each category 
of csv set-table based on the graph model of each subclass, consisting of 6 categories, namely:
• Main class interpreter for main class set-table.
• Main class to subclass interpreter for main class to subclass set-table.
• Subclass property interpreter for FUKG subclass property set-table and FUKG property mapping set-table to wikidata.
• Subclass to subclass relation schema interpreter for subclass to subclass relation set-table.
• University attribute data mapping interpreter for university attribute data mapping set-table.
• University relation data mapping interpreter for university relation data mapping set-table.

4 Triple store and SPARQL query

4.1. Triple store

The use of apache jena fuseki triple store in this study is to test the dataset that has been created at the dataset creation stage. 
The RDF NT format dataset that has been created will be uploaded to the triple store. If all data is successfully uploaded without 
losing information, this indicates that the dataset created is in accordance with expectations. At this stage, attention is focused 
on how the triple store reads and processes structured and connected datasets, which are generated from the RDF dataset creation 
stage. The triple store then generates a graph model from the dataset. The resulting graph model must be consistent and in accordance 
with the model that has been determined in the graph set-model, the graph data must be accurate with the university data stored in 
the CSV set-table and the graph data must be complete according to the set-interpreter mapping.

4.2. SPARQL query

The use of SPARQL query in this study is to test the dataset that has been uploaded to the triple store. In this study, SPARQL 
queries are used to test whether the resulting knowledge graph is correct, consistent, and complete. The SPARQL query categories 
are the same as set-interpreter. 
First, query for the main class to test the suitability of graph data with the mapping of the main class interpreter. 
Second, query for the main class to subclass to test the suitability of graph data with the mapping of the main class 
interpreter to the subclass. 
Third, query for subclass properties, to test the suitability of graph data with the mapping of the FUKG subclass property 
interpreter and the FUKG subclass property mapping interpreter to wikidata. 
Fourth, query for subclass relation schema to other subclasses to test the suitability of graph data with the mapping of the 
subclass relation schema interpreter to other subclasses. 
Fifth, query for university attribute data mapping, to test the suitability of graph data with the mapping of the university 
attribute data mapping interpreter. 
Sixth, query for university relation data mapping, to test the suitability of graph data with the mapping of the university 
relation data interpreter.



# HOW TO USE
1. Make folder project knowledge graph
2. Download FUKG
3. Download sdm-rdfizer + Install requirement sdm-rdfizer + Read first about Rdfizer if you don't know how to use it
4. Download visual studio code
4. copy folder FUKG and SDM-RDFizer to folder project
5. Open visual studio code, open folder project knowledge graph
6. Copy file set-table you want to use to folder /SDM-RDFizer/rdfizer/ 
7. copy the set-interpreter syntax from the set-table into the mapping.ttl file located in the /SDMRDFizer/Example folder
8. configure the config file according to the rdfizer rules in the /SDMRDFizzer/example folder. or read first about rdfizer
9. Run sdm-rdfizer in run sndfizer in terminal with syntax : 
   python run_rdfizer.py C:\Users\username\folderproject\rdfizer\example\config.ini
10. DatasetRDF.nt will appear in the /SDM/RDFizer/example folder
11. run apache jena fuseki
12. open microsoft edge or similar, go to apache jena fuseki's localhost page
13. upload DatasetRDF.Nt file
14. perform a query process to test the success of the knowledge graph in the triple store.

# CONTACT : ustadzchina41@gmail.com

